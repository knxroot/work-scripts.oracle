#!/usr/bin/env python

import os.path
import datetime

from fabric.api import *

#from config import *
import config as c
from common import *

def _stop(instance):
    vrun("""env ORACLE_SID="""+instance+""" sqlplus / as sysdba <<-EOI
shutdown immediate;
EOI""")

def _start_as_logical_master(instance):
    vrun("""lsnrctl start""")
    vrun("""env ORACLE_SID="""+instance+""" sqlplus / as sysdba <<-EOI
startup;
EOI""")

def _start_as_logical_slave(instance):
    vrun("""lsnrctl start""")
    vrun("""env ORACLE_SID="""+instance+""" sqlplus / as sysdba <<-EOI
startup mount;
alter database open;
alter database start logical standby apply immediate;
EOI""")

def _start_as_physical_master(instance):
    vrun("""lsnrctl start""")
    vrun("""env ORACLE_SID="""+instance+""" sqlplus / as sysdba <<-EOI
startup;
EOI""")

def _start_as_physical_slave(instance):
    vrun("""lsnrctl start""")
    vrun("""env ORACLE_SID="""+instance+""" sqlplus / as sysdba <<-EOI
startup nomount;
alter database mount standby database;
alter database recover managed standby database using current logfile disconnect from session;
EOI""")

def _stop_with_listener(instance):
    vrun("""lsnrctl stop""")
    vrun("""env ORACLE_SID="""+instance+""" sqlplus / as sysdba <<-EOI
shutdown immediate;
EOI""")

def _switch_log(instance_name):
    runsql(instance_name,"ALTER SYSTEM SWITCH LOGFILE;")

def _set_archive_mode(instance_name,reopen=True):
    # 1.Enable Forced Logging
    runsql(instance_name,"""SHUTDOWN IMMEDIATE;
STARTUP MOUNT;
ALTER DATABASE ARCHIVELOG;""")
    if reopen:
        runsql(instance_name,"""ALTER DATABASE OPEN;
alter system archive log current;""")

def _set_flashback_mode(instance_name):
    # 1.Enable flashback
    runsql(instance_name,"""SHUTDOWN IMMEDIATE;
STARTUP MOUNT;
ALTER DATABASE FLASHBACK ON;
ALTER DATABASE OPEN;""")

def _set_forcelogging_mode(instance_name):
    # 1.Enable Forced Logging
    runsql(instance_name,"""ALTER DATABASE FORCE LOGGING;""")

def _setup_as_standby(oracle_base,pri_instance):
    runsql(pri_instance,"""ALTER DATABASE ADD STANDBY LOGFILE GROUP 11 '"""+oracle_base+"""/oradata/"""+pri_instance+"""/standby_redo11.log' size 50M;  
ALTER DATABASE ADD STANDBY LOGFILE GROUP 12 '"""+oracle_base+"""/oradata/"""+pri_instance+"""/standby_redo12.log' size 50M;  
ALTER DATABASE ADD STANDBY LOGFILE GROUP 13 '"""+oracle_base+"""/oradata/"""+pri_instance+"""/standby_redo13.log' size 50M;  
ALTER DATABASE ADD STANDBY LOGFILE GROUP 14 '"""+oracle_base+"""/oradata/"""+pri_instance+"""/standby_redo14.log' size 50M;""")
    _set_archive_mode(pri_instance,False)
    runsql(pri_instance,"""ALTER SYSTEM SET LOG_ARCHIVE_DEST_9 = 'LOCATION=USE_DB_RECOVERY_FILE_DEST VALID_FOR=(STANDBY_LOGFILE,STANDBY_ROLE)';
ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_9 = ENABLE;
""")


def config_standby_pri(oracle_base,oracle_home,slv_ip,pri_instance,slv_instance,pri_tns,slv_tns):
    # 1.Enable Forced Logging
    _set_forcelogging_mode(pri_instance)

    # 3.Configuring an Oracle Database to Receive Redo Data
    _setup_as_standby(oracle_base,pri_instance)

    # 4.Set Primary Database Initialization Parameters
    _setup_pri_sp(pri_instance,slv_instance,pri_tns,slv_tns)

    # 5.Enable Archiving
    _set_archive_mode(pri_instance)

    _setup_listener(oracle_home,env.host,pri_instance)
    _setup_tns(oracle_home,env.host,slv_ip,pri_instance,slv_instance,pri_tns,slv_tns)

def prepare_dup_slave(oracle_base,oracle_home,pri_ip,pri_instance,slv_instance,pri_tns,slv_tns):
    _setup_listener(oracle_home,env.host,slv_instance)
    _setup_tns(oracle_home,pri_ip,env.host,pri_instance,slv_instance,pri_tns,slv_tns)
    _startup_instance(oracle_home,slv_instance)
    _setup_db_dirs(oracle_base,slv_instance)
    _copy_orapwfile("oracle",pri_ip,oracle_home,pri_instance,slv_instance)

def _copy_orapwfile(pri_user,pri_ip,oracle_home,pri_instance,slv_instance):
    vrun("""scp """+pri_user+"""@"""+pri_ip+""":"""+oracle_home+"""/dbs/orapw"""+pri_instance+""" """+oracle_home+"""/dbs/orapw"""+slv_instance)

def _startup_instance(oracle_home,instance):
    vrun("""echo 'DB_NAME="""+instance+"""' > """+oracle_home+"""/dbs/init"""+instance+""".ora""")
    vrun("""env ORACLE_SID="""+instance+""" sqlplus /nolog <<-EOI
conn / as sysdba;
startup nomount;
EOI""")

def _setup_db_dirs(oracle_base,slv_instance):
    vrun("""mkdir -p """+oracle_base+"""/admin/"""+slv_instance+"""/{adump,dpdump,pfile,scripts}""")
    vrun("""mkdir -p """+oracle_base+"""/oradata/"""+slv_instance+"""  
mkdir -p """+oracle_base+"""/fast_recovery_area/"""+slv_instance)

def dup_m2m_onslave(oracle_base,ora_pw,pri_tns,slv_tns,pri_in,slv_in):
    vrun("""rman target sys/"""+ora_pw+"""@"""+pri_tns+""" auxiliary sys/"""+ora_pw+"""@"""+slv_tns+""" <<-EOI
duplicate target database to orcl from active database nofilenamecheck;
EOI""")

def _setup_pri_sp(pri_instance,slv_instance,pri_tnsname,slv_tnsname):
    #ORA-32016: parameter "db_name" cannot be updated in SPFILE
    runsql(pri_instance,"""ALTER SYSTEM SET DB_NAME = """+pri_instance+""" SCOPE=SPFILE;
ALTER SYSTEM SET DB_UNIQUE_NAME = """+pri_instance+""" SCOPE=SPFILE;""")

    _setup_pri_sp_log_archieve(pri_instance,[slv_instance],[slv_tnsname])

    runsql(pri_instance,"""ALTER SYSTEM SET FAL_SERVER="""+slv_tnsname+""" SCOPE=SPFILE;
ALTER SYSTEM SET STANDBY_FILE_MANAGEMENT=AUTO SCOPE=SPFILE;""")
    runsql(pri_instance,"""ALTER SYSTEM SET DB_FILE_NAME_CONVERT='"""+slv_instance+"""','"""+pri_instance+"""' SCOPE=SPFILE;
ALTER SYSTEM SET LOG_FILE_NAME_CONVERT= '"""+slv_instance+"""','"""+pri_instance+"""' SCOPE=SPFILE;""")

def _setup_pri_sp_log_archieve(pri_instance,slv_instances,slv_tnsnames):
    # ORA-16179: incremental changes to "log_archive_dest_1" not allowed with SPFILE
    runsql(pri_instance,"""ALTER SYSTEM SET LOG_ARCHIVE_DEST_1 = 'LOCATION=USE_DB_RECOVERY_FILE_DEST VALID_FOR=(ALL_LOGFILES,ALL_ROLES) DB_UNIQUE_NAME="""+pri_instance+"""' SCOPE=SPFILE;""")
    runsql(pri_instance,"""ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_1 = ENABLE SCOPE=SPFILE;""")

    runsql(pri_instance,"""ALTER SYSTEM SET LOG_ARCHIVE_CONFIG = 'DG_CONFIG=("""+pri_instance+""","""+",".join(slv_instances)+""")' SCOPE=SPFILE;""")
    runsql(pri_instance,"""ALTER SYSTEM SET REMOTE_LOGIN_PASSWORDFILE = EXCLUSIVE SCOPE=SPFILE;""")

    for i in range(len(slv_instances)):
        runsql(pri_instance,"""ALTER SYSTEM SET LOG_ARCHIVE_DEST_"""+str(i+2)+""" = 'SERVICE="""+slv_tnsnames[i]+""" ASYNC VALID_FOR=(ONLINE_LOGFILES,PRIMARY_ROLE) DB_UNIQUE_NAME="""+slv_instances[i]+"""' SCOPE=SPFILE;""")
        runsql(pri_instance,"""ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_"""+str(i+2)+""" = ENABLE SCOPE=SPFILE;""")

    return 1+2

def _setup_pri_prepare_files(datafiles):
    _prepare_data_files(datafiles)
    #_prepare_control_files()
    #_prepare_parameter_file()

def _prepare_data_files(datafiles):
    for datafile in datafiles:
        vrun("cp "+datafile+" ")

def create_standby_onslave(oracle_base,ora_pw,pri_tns,slv_tns,pri_in,slv_in):
    #ORA-16179: incremental changes to "log_archive_dest_1" not allowed with SPFILE
#SET LOG_ARCHIVE_DEST_1='LOCATION= USE_DB_RECOVERY_FILE_DEST VALID_FOR=(ALL_LOGFILES,ALL_ROLES) DB_UNIQUE_NAME="""+slv_in+"""'
    dest_states=""
    for i in range(3,32):
        dest_states += "\nSET LOG_ARCHIVE_DEST_STATE_"+str(i)+"='DEFER'"
    dest_states+="\n"
    vrun("""rman target sys/"""+ora_pw+"""@"""+pri_tns+""" auxiliary sys/"""+ora_pw+"""@"""+slv_tns+""" <<-EOI
RUN {
ALLOCATE CHANNEL C1 TYPE DISK;
ALLOCATE CHANNEL C2 TYPE DISK;
ALLOCATE AUXILIARY CHANNEL STBY TYPE DISK;
DUPLICATE TARGET DATABASE FOR STANDBY NOFILENAMECHECK FROM ACTIVE DATABASE 
DORECOVER
SPFILE
PARAMETER_VALUE_CONVERT '"""+pri_in+"""','"""+slv_in+"""'
SET DB_NAME='"""+pri_in+"""'
SET DB_UNIQUE_NAME='"""+slv_in+"""'
SET LOG_ARCHIVE_DEST_2='SERVICE="""+pri_tns+""" ASYNC VALID_FOR=(ONLINE_LOGFILE,PRIMARY_ROLE) DB_UNIQUE_NAME="""+pri_in+"""'"""+dest_states+
"""SET STANDBY_FILE_MANAGEMENT='AUTO'
SET FAL_SERVER='"""+pri_tns+"""'
SET DB_FILE_NAME_CONVERT='"""+pri_in+"""','"""+slv_in+"""'
SET LOG_FILE_NAME_CONVERT= '"""+pri_in+"""','"""+slv_in+"""';
RELEASE CHANNEL C1;
RELEASE CHANNEL C2;
RELEASE CHANNEL STBY;
}
QUIT
EOI""")
    runsql(slv_in,"""alter database recover managed standby database using current logfile disconnect;""")

def _setup_tns(oracle_home,pri_ip,slv_ip,pri_in,slv_in,pri_tns,slv_tns):
    vrun("""cat <<-EOI >"""+oracle_home+"""/network/admin/tnsnames.ora
"""+pri_tns+""" =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = """+pri_ip+""")(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = """+pri_in+""")
    )
  )

"""+slv_tns+""" =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = """+slv_ip+""")(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = """+slv_in+""")
    )
  )
EOI""")
    vrun("tnsping "+pri_tns)
    vrun("tnsping "+slv_tns)

def _add_tns(oracle_home,slv_ip,slv_in,slv_tns):
    vrun("""cat <<-EOI >>"""+oracle_home+"""/network/admin/tnsnames.ora
"""+slv_tns+""" =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = """+slv_ip+""")(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = """+slv_in+""")
    )
  )
EOI""")
    vrun("tnsping "+slv_tns)

def _setup_listener(oracle_home,ip,instance_name):
    vrun("""cat <<-EOI >"""+oracle_home+"""/network/admin/listener.ora
LISTENER =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = """+ip+""")(PORT = 1521))
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
    )
  )

SID_LIST_LISTENER =
  (SID_LIST =
    (SID_DESC =
      (GLOBAL_DBNAME = """+instance_name+""")
      (ORACLE_HOME = """+oracle_home+""")
      (SID_NAME = """+instance_name+""")
    )
    (SID_DESC =
      (GLOBAL_DBNAME = """+instance_name+"""_DGMGRL)
      (ORACLE_HOME = """+oracle_home+""")
      (SID_NAME = """+instance_name+""")
    )
  )
EOI""")
    #vrun("lsnrctl reload")
    vrun("lsnrctl stop; lsnrctl start")

def _stop_redo_apply(instance):
    runsql(instance,"ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;")

def _prepare_to_support_logical(pri_instance,dest_number):
    runsql(pri_instance,"""ALTER SYSTEM SET LOG_ARCHIVE_DEST_1 = 'LOCATION=USE_DB_RECOVERY_FILE_DEST VALID_FOR=(ONLINE_LOGFILES,ALL_ROLES) DB_UNIQUE_NAME="""+pri_instance+"""' SCOPE=BOTH;""")
    runsql(pri_instance,"""ALTER SYSTEM SET LOG_ARCHIVE_DEST_"""+str(dest_number)+""" = 'LOCATION=USE_DB_RECOVERY_FILE_DEST VALID_FOR=(STANDBY_LOGFILES,STANDBY_ROLE) DB_UNIQUE_NAME="""+pri_instance+"""' SCOPE=BOTH;
ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_"""+str(dest_number)+""" = ENABLE SCOPE=BOTH;""")
    runsql(pri_instance,"""EXECUTE DBMS_LOGSTDBY.BUILD;""")

def _transition_to_logical(pri_instance,slv_instance,pri_tns):
    runsql(slv_instance,"""ALTER DATABASE RECOVER TO LOGICAL STANDBY """+slv_instance+""";
SHUTDOWN IMMEDIATE;
STARTUP MOUNT;""")

    runsql(slv_instance,"""ALTER SYSTEM SET LOG_ARCHIVE_DEST_1 = 'LOCATION=USE_DB_RECOVERY_FILE_DEST VALID_FOR=(ALL_LOGFILES, ALL_ROLES) DB_UNIQUE_NAME="""+slv_instance+"""' SCOPE=BOTH;
ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_1 = ENABLE SCOPE=BOTH;
ALTER SYSTEM SET LOG_ARCHIVE_DEST_2 = 'SERVICE="""+pri_tns+""" ASYNC VALID_FOR=(ONLINE_LOGFILES,PRIMARY_ROLE) DB_UNIQUE_NAME="""+pri_instance+"""' SCOPE=BOTH;
ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_2 = ENABLE SCOPE=BOTH;
""")
#    runsql(slv_instance,"""ALTER SYSTEM SET LOG_ARCHIVE_DEST_1 = 'LOCATION=USE_DB_RECOVERY_FILE_DEST VALID_FOR=(ONLINE_LOGFILES,ALL_ROLES) DB_UNIQUE_NAME="""+slv_instance+"""' SCOPE=BOTH;
#ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_1 = ENABLE SCOPE=BOTH;
#ALTER SYSTEM SET LOG_ARCHIVE_DEST_2 = 'SERVICE="""+pri_tns+""" ASYNC VALID_FOR=(ONLINE_LOGFILES,PRIMARY_ROLE) DB_UNIQUE_NAME="""+pri_instance+"""' SCOPE=BOTH;
#ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_2 = ENABLE SCOPE=BOTH;
#ALTER SYSTEM SET LOG_ARCHIVE_DEST_3 = 'LOCATION=USE_DB_RECOVERY_FILE_DEST VALID_FOR=(STANDBY_LOGFILES,STANDBY_ROLE) DB_UNIQUE_NAME="""+slv_instance+"""' SCOPE=BOTH;
#ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_3 = ENABLE SCOPE=BOTH;""")

    runsql(slv_instance,"""ALTER DATABASE OPEN RESETLOGS;
ALTER DATABASE START LOGICAL STANDBY APPLY IMMEDIATE;""")

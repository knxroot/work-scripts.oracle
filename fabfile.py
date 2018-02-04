#import os.path as path
#from os.path import *
#from config import *
from common import *

from fabric.api import *
from oracon import Orac
from orarac import Oracc
from fabric.colors import green

import config as c
import oraadmin as admin
import oradg as dg
import sqls as sqls

################################################################################
db_master=Orac("gjzspt","12345678","10.0.50.161","orcl")
db_slave=Orac("gjzspt","12345678","10.0.50.162","slave")

db_master_sys=Orac("sys","oracle","10.0.50.161","orcl")
db_master_sys_sp=Oracc("sys","oracle","10.0.50.161","orcl")
db_master_jcfx=Orac("jcfx","12345678","10.0.50.161","orcl")
db_master_pub_jcfx=Orac("jcfx","12345678","218.89.222.117","orcl",1523)
db_slave_sys=Orac("sys","oracle","10.0.50.162","slave")

db_rac=Oracc("sys","oracle","10.0.52.199","orcl")
db_rac_jcfx=Oracc("jcfx","12345678","10.0.52.199","orcl")

db_weiq=Oracc("sys","123456789","172.16.7.116","oracle")
db_weiq_jcfx=Oracc("jcfx","12345678","172.16.7.116","oracle")

db_163_sys=Orac("sys","oracle","10.0.50.163","orcl")
db_163_gjzspt=Orac("gjzspt","12345678","10.0.50.163","orcl")
db_165_sys=Orac("sys","oracle","10.0.50.165","slave")
db_165_gjzspt=Orac("gjzspt","12345678","10.0.50.165","slave")

db_dev_sys=Orac("sys","Oe123qwe###","192.168.21.249","gjzs")
db_test_sys=Orac("sys","oracle","10.0.52.1","orcl")
################################################################################
def newserver_isalive():
    db_163_sys.run_query("select * from dual")

def newserver_popu():
    execute(_setup,hosts=["10.0.50.163"])

def _setup():
    c.remoteFile = admin._backup("oracle","gjzspt")
    admin._dropdb("orcl","gjzspt")
    admin._create_user("orcl","gjzspt","12345678")
    admin._imp_with_localfile("oracle","gjzspt","gjzspt","./dmpfiles/dev_gjzspt_20170309_wd.dmp",'N','N')
    admin._imp_with_remotefile("oracle","gjzspt","gjzspt",c.remoteFile,'Y','Y')

################################################################################
@hosts(["10.0.50.161"])
def quanwei_add_pri():
    admin._grant_additional_priviliges("orcl","jcfx")

def quanwei_check():
    sql="select EXTENDED_TIMESTAMP,OS_USER,userhost,os_process,DB_USER,OBJECT_SCHEMA,OBJECT_NAME,RETURNCODE,STATEMENT_TYPE,SQL_TEXT,AUDIT_TYPE from DBA_COMMON_AUDIT_TRAIL order by EXTENDED_TIMESTAMP desc,LOGOFF_TIME desc"
    db_master_sys.run_query(sql)
    #db_slave_sys.run_query(sql)

@roles('standby.master')
def quanwei_enable_audit():
    admin._enable_audit("orcl")
    runsql("orcl","audit all by jcfx;")
    runsql("orcl","AUDIT ALL PRIVILEGES;")
    admin._restart("orcl")

def quanwei_import_test_db():
    execute(_exp2,hosts=['192.168.21.249'])
    execute(_imp2,hosts=["10.0.50.161"])

def _exp2():
    day=datetime.datetime.now().strftime("%Y%m%d")
    c.localFile = "./dmpfiles/gjzspt"+day+"wd.dmp"
    admin._backup_to_localfile("Oe123qwe###","gjzspt",c.localFile)

def _imp2():
    admin._dropdb("orcl","jcfx")
    admin._create_user("orcl","jcfx","12345678")
    admin._grant_mv_priviliges("orcl","jcfx")
    admin._imp_with_localfile("oracle","gjzspt","jcfx",c.localFile,'Y','N')

################################################################################
def quanwei_setup_env_mv():
    execute(_setup_master_env_mv)

#@roles('standby.master')
def _setup_master_env_mv():
    admin._dropdb("orcl","jcfx")
    admin._create_user("orcl","jcfx","12345678")
    admin._grant_mv_priviliges("orcl","jcfx")
    dg._switch_log("orcl")

def a_setup_master_env_sample_table():
    db_master_jcfx.run_statement("""DROP TABLE emp""")
    db_master_jcfx.run_statement("""CREATE TABLE emp (
empno
NUMBER(5) PRIMARY KEY,
ename
VARCHAR2(15) NOT NULL,
ssn
NUMBER(9),
job
VARCHAR2(10),
mgr
NUMBER(5),
hiredate
DATE DEFAULT (SYSDATE),
sal
NUMBER(7,2),
comm
NUMBER(7,2),
deptno
NUMBER(3) NOT NULL)""")

def quanwei_verify_env_mv():
    a_setup_master_env_sample_table()
    db_master_jcfx.run_statement("""CREATE MATERIALIZED VIEW LOG ON emp""")
    db_master_jcfx.run_statement("""DROP MATERIALIZED VIEW test_mv""")
    db_master_jcfx.run_statement("""CREATE MATERIALIZED VIEW test_mv
BUILD IMMEDIATE
REFRESH FAST ON COMMIT
ENABLE QUERY REWRITE
AS
SELECT *
 FROM emp""")
    db_master_jcfx.run_statement("""SELECT * FROM emp""")
    db_master_jcfx.run_statement("""SELECT * from test_mv""")

################################################################################
def verify_weiq():
    db_weiq._exec(sqls._create_user('jcfx','12345678'))
    db_weiq_jcfx._exec("select * from dual;")

################################################################################
def verify_rac():
    db_rac._exec(sqls._create_table_ws_log())
    db_rac._exec("insert into t_dgap_ws_log(ID,METHOD_NAME,INVOKE_START_DATE) values ('DATA_GUARD_TESTING','data guard test',CURRENT_TIMESTAMP);")
    db_rac._exec("select * from t_dgap_ws_log;")
    db_rac._exec(sqls._drop_table("t_dgap_ws_log"))

    db_rac._exec(sqls._dropdb("jcfx"))
    db_rac._exec(sqls._create_user("jcfx","12345678"))
    db_rac._exec(sqls._grant_mv_priviliges("jcfx"))

    db_rac_jcfx._exec(sqls._create_table_ws_log())
    db_rac_jcfx._exec("insert into t_dgap_ws_log(ID,METHOD_NAME,INVOKE_START_DATE) values ('DATA_GUARD_TESTING','data guard test',CURRENT_TIMESTAMP);")
    db_rac_jcfx._exec("select * from t_dgap_ws_log;")
    db_rac_jcfx._exec(sqls._drop_table("t_dgap_ws_log"))

################################################################################
def dataguard_logical_start():
    with settings(warn_only=True):
        execute(dg._start_as_logical_slave, "slave", hosts=["10.0.50.165"])
        execute(dg._start_as_logical_master, "orcl", hosts=["10.0.50.163"])

def dataguard_logical_stop():
    execute(dg._stop, "orcl", hosts=["10.0.50.163"])
    execute(dg._stop, "slave", hosts=["10.0.50.165"])

def dataguard_new_phisical_standby():
    execute(dg.config_standby_pri,c.oracle_base,c.oracle_home,"10.0.50.165",c.pri_instance,c.slave_instance,c.pri_tnsname,c.slave_tnsname,hosts=["10.0.50.163"])
    execute(dg.prepare_dup_slave,c.oracle_base,c.oracle_home,"10.0.50.163",c.pri_instance,c.slave_instance,c.pri_tnsname,c.slave_tnsname,hosts=["10.0.50.165"])
    execute(dg.create_standby_onslave,c.oracle_base,c.oracle_password,c.pri_tnsname,c.slave_tnsname,c.pri_instance,c.slave_instance,hosts=["10.0.50.165"])

def dataguard_new_logical_standby():
    execute(dg._stop_redo_apply,c.slave_instance,hosts=['10.0.50.165'])
    NEXT_DEST_NUMBER = 4
    execute(dg._prepare_to_support_logical,c.pri_instance,NEXT_DEST_NUMBER,hosts=['10.0.50.163'])
    execute(dg._transition_to_logical,c.pri_instance,c.slave_instance,c.pri_tnsname,hosts=['10.0.50.165'])

def dataguard_new_disallowed():
    db_163_sys.run_query("SELECT OWNER, TABLE_NAME FROM DBA_LOGSTDBY_NOT_UNIQUE WHERE (OWNER, TABLE_NAME) NOT IN  (SELECT DISTINCT OWNER, TABLE_NAME FROM DBA_LOGSTDBY_UNSUPPORTED)  AND BAD_COLUMN = 'Y'")

def dataguard_new_switchlog():
    execute(dg._switch_log,"orcl",hosts=['10.0.50.163'])

def dataguard_new_grants():
    #execute(admin._grant_dg_priviliges,"orcl","gjzspt",hosts=['10.0.50.163'])
    execute(admin._grant_dg_priviliges,"slave","gjzspt",hosts=['10.0.50.165'])

def dataguard_new_verify():
    db_163_gjzspt.run_statement("delete from t_dgap_ws_log where id in ('DATA_GUARD_TESTING')")
    execute(dg._switch_log,"orcl",hosts=['10.0.50.163'])
    db_163_gjzspt.run_query("select * from t_dgap_ws_log where id='DATA_GUARD_TESTING'")
    db_165_gjzspt.run_query("select * from t_dgap_ws_log where id='DATA_GUARD_TESTING'")

    db_163_gjzspt.run_statement("insert into t_dgap_ws_log(ID,METHOD_NAME,INVOKE_START_DATE) values ('DATA_GUARD_TESTING','data guard test',CURRENT_TIMESTAMP)")
    execute(dg._switch_log,"orcl",hosts=['10.0.50.163'])
    db_163_gjzspt.run_query("select * from t_dgap_ws_log where id='DATA_GUARD_TESTING'")
    db_165_gjzspt.run_query("select * from t_dgap_ws_log where id='DATA_GUARD_TESTING'")

def dataguard_new_check():
    execute(admin._view_db,"orcl",hosts=["10.0.50.163"])
    execute(admin._tail_alert_log,c.oracle_base,"orcl",hosts=["10.0.50.163"])
    _view_database(db_163_sys)
    execute(admin._view_db,"slave",hosts=["10.0.50.165"])
    execute(admin._tail_alert_log,c.oracle_base,"slave",hosts=["10.0.50.165"])
    _view_database(db_165_sys)

def dataguard_new_check_redo_transport():
    db_163_sys.run_query("SELECT DESTINATION, STATUS, ARCHIVED_THREAD#, ARCHIVED_SEQ# FROM V$ARCHIVE_DEST_STATUS WHERE STATUS <> 'DEFERRED' AND STATUS <> 'INACTIVE'")
    db_163_sys.run_query("select guard_status from v$database")

def dataguard_new_check_apply():
    db_165_sys.run_query("SELECT FILE_NAME, SEQUENCE# AS SEQ#, FIRST_CHANGE# AS F_SCN#, NEXT_CHANGE# AS N_SCN#, TIMESTAMP, DICT_BEGIN AS BEG, DICT_END AS END, THREAD# AS THR#, APPLIED FROM DBA_LOGSTDBY_LOG  ORDER BY SEQUENCE#")
    db_165_sys.run_query("SELECT NAME, VALUE, UNIT FROM V$DATAGUARD_STATS")
    db_165_sys.run_query("SELECT * FROM V$LOGSTDBY_STATE")
    #db_165_sys.run_query("SELECT SUBSTR(name, 1, 40) AS NAME, SUBSTR(value,1,32) AS VALUE FROM V$LOGSTDBY_STATS")
    db_165_sys.run_query("SELECT APPLIED_SCN, LATEST_SCN, MINING_SCN, RESTART_SCN FROM V$LOGSTDBY_PROGRESS")
    db_165_sys.run_query("SELECT APPLIED_TIME, LATEST_TIME, MINING_TIME, RESTART_TIME FROM V$LOGSTDBY_PROGRESS")
    db_163_sys.run_query("select guard_status from v$database")

################################################################################
def dataguard_setup_logical_standby():
    execute(dg._stop_redo_apply,c.slave_instance2,hosts=['10.0.50.163'])
    NEXT_DEST_NUMBER = 4
    execute(dg._prepare_to_support_logical,c.pri_instance,NEXT_DEST_NUMBER,hosts=['10.0.50.161'])
    execute(dg._transition_to_logical,c.pri_instance,c.slave_instance2,c.pri_tnsname,hosts=['10.0.50.163'])

def dataguard_add_physical_standby():
    execute(dg._add_tns,c.oracle_home,"10.0.50.163",c.slave_instance2,c.slave_tnsname2,hosts=['10.0.50.161'])
    execute(dg._setup_pri_sp_log_archieve,c.pri_instance,[c.slave_instance,c.slave_instance2],[c.slave_tnsname,c.slave_tnsname2],hosts=['10.0.50.161'])
    execute(dg._setup_pri_sp_log_archieve,c.pri_instance,[c.slave_instance,c.slave_instance2],[c.slave_tnsname,c.slave_tnsname2],hosts=['10.0.50.161'])
    #execute(dg._setup_pri_prepare_files,c.pri_instance,[c.slave_instance,c.slave_instance2],[c.slave_tnsname,c.slave_tnsname2],hosts=['10.0.50.161'])

    execute(dg.prepare_dup_slave,c.oracle_base,c.oracle_home,"10.0.50.161",c.pri_instance,c.slave_instance2,c.pri_tnsname,c.slave_tnsname2,hosts=['10.0.50.163'])
    execute(dg.create_standby_onslave,c.oracle_base,c.oracle_password,c.pri_tnsname,c.slave_tnsname2,c.pri_instance,c.slave_instance2,hosts=['10.0.50.163'])

################################################################################
def dataguard_physical_start():
    execute(dg._start_as_physical_slave, "slave", hosts=["10.0.50.162"])
    execute(dg._start_as_physical_master, "orcl", hosts=["10.0.50.161"])

def dataguard_physical_stop():
    execute(dg._stop_as_physical_master, "orcl", hosts=["10.0.50.161"])
    execute(dg._stop_as_physical_slave, "slave", hosts=["10.0.50.162"])

def dataguard_physical_vlog():
    execute(admin._tail_alert_log,c.oracle_base,"slave",hosts=["10.0.50.162"])
    execute(admin._tail_alert_log,c.oracle_base,"orcl",hosts=["10.0.50.161"])

def dataguard_create_phisical_standby():
    execute(_prepare_dg_master)
    execute(_setup_dg_slave)

@roles('standby.master')
def _prepare_dg_master():
    dg.config_standby_pri(c.oracle_base,c.oracle_home,"10.0.50.162",c.pri_instance,c.slave_instance,c.pri_tnsname,c.slave_tnsname)

@roles('standby.slave')
def _setup_dg_slave():
    dg.prepare_dup_slave(c.oracle_base,c.oracle_home,"10.0.50.161",c.pri_instance,c.slave_instance,c.pri_tnsname,c.slave_tnsname)
    dg.create_standby_onslave(c.oracle_base,c.oracle_password,c.pri_tnsname,c.slave_tnsname,c.pri_instance,c.slave_instance)

def v_standby():
    _view_pri(db_master_sys)
    #_view_parameter(db_master_sys,"file")
    #print green("################################################################################")
    #execute(admin._view_db,"orcl",hosts=["10.0.50.161"])
    print green("################################################################################")
    _view_database(db_slave_sys)
    #print green("################################################################################")
    #execute(admin._view_db,"slave",hosts=["10.0.50.162"])

def verify_standby():
    db_master.run_statement("delete from t_dgap_ws_log where id in ('DATA_GUARD_TESTING')")
    execute(dg._switch_log,"orcl",hosts=['10.0.50.161'])
    db_master.run_query("select * from t_dgap_ws_log where id='DATA_GUARD_TESTING'")
    db_slave.run_query("select * from t_dgap_ws_log where id='DATA_GUARD_TESTING'")
    db_master.run_statement("insert into t_dgap_ws_log(ID,METHOD_NAME,INVOKE_START_DATE) values ('DATA_GUARD_TESTING','data guard test',CURRENT_TIMESTAMP)")
    execute(dg._switch_log,"orcl",hosts=['10.0.50.161'])
    db_master.run_query("select * from t_dgap_ws_log where id='DATA_GUARD_TESTING'")
    db_slave.run_query("select * from t_dgap_ws_log where id='DATA_GUARD_TESTING'")

def _view_pri(conn):
    _view_database(conn)

    conn.run_query("select DEST_ID, STATUS, DESTINATION, ERROR from V$ARCHIVE_DEST where DEST_ID <= 2")
    conn.run_query("select dest_name,status,error from v$archive_dest where dest_id <= 2")
    conn.run_query("select DEST_ID,DEST_NAME,STATUS,TARGET,DESTINATION from V$ARCHIVE_DEST where dest_id <=2")
    conn.run_query("select STATUS, GAP_STATUS from V$ARCHIVE_DEST_STATUS where DEST_ID <= 2")
    conn.run_query("select SEQUENCE#, FIRST_TIME, NEXT_TIME, APPLIED, ARCHIVED from V$ARCHIVED_LOG order by FIRST_TIME")

def _view_parameter(conn,name_pattern):
    conn.run_query("SELECT name, value, isdefault FROM v$parameter where name like '%"+name_pattern+"%'")

def _view_database(conn):
    conn.run_query("select INSTANCE_NAME, STATUS, DATABASE_STATUS from v$instance")
    conn.run_query("select name, force_logging from v$database") 
    conn.run_query("select open_mode,database_role,db_unique_name from v$database")
    conn.run_query("select LOG_MODE FROM V$DATABASE")

##############################################################################

def dupli_testdb():
    execute(_setup_ori_master,hosts=["10.0.52.1"])
    execute(_setup_new_master,hosts=["10.0.50.161"])

def _setup_ori_master():
    dg._setup_tns(c.oracle_home,env.host,"10.0.50.161","orcl","orcl","master","slave")
    dg._set_archive_mode()

def _setup_new_master():
    dg.prepare_dup_slave(c.oracle_base,c.oracle_home,"10.0.52.1","orcl","orcl")
    dg.dup_m2m_onslave(c.oracle_base,c.oracle_password,c.pri_tnsname,c.slave_tnsname,"orcl","orcl")

def v_dup():
    execute(_view_master)
    execute(_view_new_master)

@roles("dup.db_master")
def _view_master():
    admin._view_db("orcl")

@roles('dup.db_new_master')
def _view_new_master():
    admin._view_db("orcl")

##############################################################################
def disasotr_recovery_db_create():
    execute(admin._createdb,"orcl","gjzspt","12345678",hosts=['10.0.52.2'])
    execute(admin._imp_with_localfile,"oracle","gjzspt","gjzspt","./dmpfiles/dev_gjzspt_20170324_wd.dmp","Y","Y",hosts=['10.0.52.2'])

##############################################################################
def demo_compare_dev():
    db_dev_sys.run_query(sqls._table_count("GJZSPT")[:-1])
    db_test_sys.run_query(sqls._table_count("GJZSPT_DEMO")[:-1])
    t1 = db_dev_sys.run_query(sqls._table_names("GJZSPT")[:-1])
    t2 = db_test_sys.run_query(sqls._table_names("GJZSPT_DEMO")[:-1])
#    print t1.sub(t2)
#    print t2.sub(t1)

def demo_compare_test():
    db_test_sys.run_query(sqls._table_count("GJZSPT")[:-1])
    db_test_sys.run_query(sqls._table_count("GJZSPT_DEMO")[:-1])
    t1 = db_test_sys.run_query(sqls._table_names("GJZSPT")[:-1])
    t2 = db_test_sys.run_query(sqls._table_names("GJZSPT_DEMO")[:-1])

def demo_backup():
    execute(_exp,"oracle","gjzspt_demo","backup",hosts=['10.0.52.1'])

def demo_impdb():
    execute(_exp,"Oe123qwe###","gjzspt","dev",hosts=['192.168.21.249'])
    execute(_backup2,"oracle","gjzspt",hosts=['10.0.52.1'])
    execute(admin._dropdb_forceful,"orcl","gjzspt_demo",hosts=['10.0.52.1'])
    execute(admin._createdb,"orcl","gjzspt_demo","12345678",hosts=['10.0.52.1'])
    execute(admin._imp_with_localfile,"oracle","gjzspt","gjzspt_demo",c.localFile,"N","N",hosts=['10.0.52.1'])
    execute(admin._imp_with_remotefile,"oracle","gjzspt","gjzspt_demo",c.remoteFile,"Y","Y",hosts=['10.0.52.1'])

def _backup2(db_password, schema):
    c.remoteFile = admin._backup(db_password, schema)

def demo2_impdb():
    execute(admin._dropdb_forceful,"orcl","gjzspt_demo2",hosts=['10.0.52.1'])
    execute(admin._createdb,"orcl","gjzspt_demo2","12345678",hosts=['10.0.52.1'])
    #execute(admin._imp_with_localfile,"oracle","gjzspt","gjzspt_demo2","/home/helong/TencentFiles/2898132719/FileRecv/gjzspt20180115.dmp","Y","Y",hosts=['10.0.52.1'])

def dirty_impdb():
    #execute(admin._dropdb_forceful,"orcl","gjzspt_dirty",hosts=['10.0.52.1'])
    #execute(admin._createdb,"orcl","gjzspt_dirty","12345678",hosts=['10.0.52.1'])
    execute(admin._imp_with_localfile,"oracle","gjzspt","gjzspt_dirty","/home/helong/TencentFiles/2898132719/FileRecv/gjzspt20180123.dmp","Y","Y",hosts=['10.0.52.1'])

def jcfx2_impdb():
    execute(admin._dropdb_forceful,"orcl","jcfx2",hosts=['10.0.52.1'])
    execute(admin._createdb,"orcl","jcfx2","12345678",hosts=['10.0.52.1'])
    execute(admin._imp_with_localfile,"oracle","jcfx","jcfx2","/home/helong/TencentFiles/2898132719/FileRecv/jcfx20171117.dmp","Y","Y",hosts=['10.0.52.1'])
##############################################################################
#yibing db migration
def yibing_migration():
    execute(_exp,"Oe123qwe###","sofn_sx","dev",hosts=['10.0.53.139'])
    #execute(admin._createdb,"orcl","sofn_sx","sofn_sx",hosts=['106.14.196.8'])
    #execute(admin._imp_with_localfile,"Gjzspt630","sofn_sx","sofn_sx",c.localFile,"Y","Y",hosts=['106.14.196.8'])

##############################################################################
def gjzspt_portal_new():
    execute(admin._createdb,"gjzs","gjzspt_portal","12345678",hosts=['192.168.21.249'])

##############################################################################
def bps_new():
    execute(admin._createdb,"gjzs","bps","12345678",hosts=['192.168.21.249'])

##############################################################################
def test_start():
    with settings(warn_only=True):
        execute(admin._startup,"orcl",hosts=["10.0.52.1"])

def test_syncdb_verify():
    db_dev_sys.run_query(sqls._table_count("GJZSPT")[:-1])
    db_test_sys.run_query(sqls._table_count("GJZSPT")[:-1])
    t1 = db_dev_sys.run_query(sqls._table_names("GJZSPT")[:-1])
    t2 = db_test_sys.run_query(sqls._table_names("GJZSPT")[:-1])

def test_syncdb():
    execute(_exp,"Oe123qwe###","gjzspt","dev",hosts=['192.168.21.249'])
    execute(_backup,hosts=['10.0.52.1'])
    execute(_recreatedb,hosts=['10.0.52.1'])
    execute(_imp,hosts=['10.0.52.1'])

def _exp(db_password,schema_name,dbname):
    day=datetime.datetime.now().strftime("%Y%m%d")
    c.localFile = "./dmpfiles/"+dbname+"_"+schema_name+"_"+day+"_wd.dmp"
    admin._backup_to_localfile(db_password,schema_name,c.localFile)
    print c.localFile

def _backup():
    c.remoteFile = admin._backup("oracle","gjzspt")

def _recreatedb():
    admin._dropdb_forceful("orcl","gjzspt")
    admin._createdb("orcl","gjzspt","12345678")

def _imp():
    admin._imp_with_localfile("Oe123qwe###","gjzspt","gjzspt",c.localFile,'N','N')
    #admin._imp_with_localfile("oracle","gjzspt","gjzspt",c.localFile,'N','N')
    #admin._imp_with_remotefile("oracle","gjzspt","gjzspt",c.remoteFile,'Y','Y')

##############################################################################
def test_newdev():
    execute(_createdb2,hosts=['10.0.52.1'])
    execute(_imp2,hosts=['10.0.52.1'])

def _createdb2():
    admin._createdb("orcl","gjzspt_dev","12345678")

def _imp2():
    admin._imp_with_localfile("Oe123qwe###","gjzspt","gjzspt_dev",'./dmpfiles/dev_gjzspt_20170914_wd.dmp','Y','N')

##############################################################################
def dev_new():
    execute(_createdb3,hosts=['192.168.21.249'])
    execute(_imp3,hosts=['192.168.21.249'])

def _createdb3():
    admin._createdb("gjzs","gjzspt","12345678")

def _imp3():
    admin._imp_with_localfile("Oe123qwe###","gjzspt","gjzspt",'./dmpfiles/dev_gjzspt_20170914_wd.dmp','Y','N')

##############################################################################
def dev_start():
    with settings(warn_only=True):
        execute(admin._startup,"gjzs",hosts=["192.168.21.249"])

def dev_backup():
    execute(_exp,"Oe123qwe###","gjzspt","dev",hosts=['192.168.21.249'])

def dev_restore():
    execute(_restore_db,"Oe123qwe###","gjzspt","gjzspt","./dmpfiles/dev_gjzspt_20170309_wd.dmp",hosts=['192.168.21.249'])

def dev_restart():
    execute(admin._restart,"gjzs",hosts=['192.168.21.249'])

def dev_enable_audit():
    execute(_enable_audit,"gjzs","gjzspt",hosts=['192.168.21.249'])

def _restore_db(db_password,schema,from_schema,filepath):
    admin._imp_with_localfile(db_password,schema,from_schema,filepath,'Y','Y')

def _enable_audit(instance_name,schema_name):
    admin._enable_audit2(instance_name,schema_name)
    admin._restart(instance_name)


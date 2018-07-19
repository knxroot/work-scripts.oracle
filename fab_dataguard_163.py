#import os.path as path
#from os.path import *
#from config import *
from common import *

from fabric.api import *
from oracon import Orac
from orarac import Oracc
from fabric.colors import green

from dataguard_ import *
from dataguard_ import _setup,_view_database

import config as c
import oraadmin as admin
import oradg as dg
import sqls as sqls

################################################################################
db_163_sys=Orac("sys","oracle","10.0.50.163","orcl")
db_163_gjzspt=Orac("gjzspt","12345678","10.0.50.163","orcl")
db_165_sys=Orac("sys","oracle","10.0.50.165","slave")
db_165_gjzspt=Orac("gjzspt","12345678","10.0.50.165","slave")

################################################################################
def newserver_isalive():
    db_163_sys.run_query("select * from dual")

def newserver_popu():
    execute(_setup,hosts=["10.0.50.163"])

################################################################################
@task
def dataguard_logical_start():
    with settings(warn_only=True):
        execute(dg._start_as_logical_slave, "slave", hosts=["10.0.50.165"])
        execute(dg._start_as_logical_master, "orcl", hosts=["10.0.50.163"])

@task
def dataguard_logical_stop():
    execute(dg._stop, "orcl", hosts=["10.0.50.163"])
    execute(dg._stop, "slave", hosts=["10.0.50.165"])

################################################################################
@task
def dataguard_new_phisical_standby():
    execute(dg.config_standby_pri,c.oracle_base,c.oracle_home,"10.0.50.165",c.pri_instance,c.slave_instance,c.pri_tnsname,c.slave_tnsname,hosts=["10.0.50.163"])
    execute(dg.prepare_dup_slave,c.oracle_base,c.oracle_home,"10.0.50.163",c.pri_instance,c.slave_instance,c.pri_tnsname,c.slave_tnsname,hosts=["10.0.50.165"])
    execute(dg.create_standby_onslave,c.oracle_base,c.oracle_password,c.pri_tnsname,c.slave_tnsname,c.pri_instance,c.slave_instance,hosts=["10.0.50.165"])

@task
def dataguard_new_logical_standby():
    execute(dg._stop_redo_apply,c.slave_instance,hosts=['10.0.50.165'])
    NEXT_DEST_NUMBER = 4
    execute(dg._prepare_to_support_logical,c.pri_instance,NEXT_DEST_NUMBER,hosts=['10.0.50.163'])
    execute(dg._transition_to_logical,c.pri_instance,c.slave_instance,c.pri_tnsname,hosts=['10.0.50.165'])

@task
def dataguard_new_disallowed():
    db_163_sys.run_query("SELECT OWNER, TABLE_NAME FROM DBA_LOGSTDBY_NOT_UNIQUE WHERE (OWNER, TABLE_NAME) NOT IN  (SELECT DISTINCT OWNER, TABLE_NAME FROM DBA_LOGSTDBY_UNSUPPORTED)  AND BAD_COLUMN = 'Y'")

@task
def dataguard_new_switchlog():
    execute(dg._switch_log,"orcl",hosts=['10.0.50.163'])

@task
def dataguard_new_grants():
    #execute(admin._grant_dg_priviliges,"orcl","gjzspt",hosts=['10.0.50.163'])
    execute(admin._grant_dg_priviliges,"slave","gjzspt",hosts=['10.0.50.165'])

@task
def dataguard_new_verify():
    db_163_gjzspt.run_statement("delete from t_dgap_ws_log where id in ('DATA_GUARD_TESTING')")
    execute(dg._switch_log,"orcl",hosts=['10.0.50.163'])
    db_163_gjzspt.run_query("select * from t_dgap_ws_log where id='DATA_GUARD_TESTING'")
    db_165_gjzspt.run_query("select * from t_dgap_ws_log where id='DATA_GUARD_TESTING'")

    db_163_gjzspt.run_statement("insert into t_dgap_ws_log(ID,METHOD_NAME,INVOKE_START_DATE) values ('DATA_GUARD_TESTING','data guard test',CURRENT_TIMESTAMP)")
    execute(dg._switch_log,"orcl",hosts=['10.0.50.163'])
    db_163_gjzspt.run_query("select * from t_dgap_ws_log where id='DATA_GUARD_TESTING'")
    db_165_gjzspt.run_query("select * from t_dgap_ws_log where id='DATA_GUARD_TESTING'")

@task
def dataguard_new_check():
    execute(admin._view_db,"orcl",hosts=["10.0.50.163"])
    execute(admin._tail_alert_log,c.oracle_base,"orcl",hosts=["10.0.50.163"])
    _view_database(db_163_sys)
    execute(admin._view_db,"slave",hosts=["10.0.50.165"])
    execute(admin._tail_alert_log,c.oracle_base,"slave",hosts=["10.0.50.165"])
    _view_database(db_165_sys)

@task
def dataguard_new_check_redo_transport():
    db_163_sys.run_query("SELECT DESTINATION, STATUS, ARCHIVED_THREAD#, ARCHIVED_SEQ# FROM V$ARCHIVE_DEST_STATUS WHERE STATUS <> 'DEFERRED' AND STATUS <> 'INACTIVE'")
    db_163_sys.run_query("select guard_status from v$database")

@task
def dataguard_new_check_apply():
    db_165_sys.run_query("SELECT FILE_NAME, SEQUENCE# AS SEQ#, FIRST_CHANGE# AS F_SCN#, NEXT_CHANGE# AS N_SCN#, TIMESTAMP, DICT_BEGIN AS BEG, DICT_END AS END, THREAD# AS THR#, APPLIED FROM DBA_LOGSTDBY_LOG  ORDER BY SEQUENCE#")
    db_165_sys.run_query("SELECT NAME, VALUE, UNIT FROM V$DATAGUARD_STATS")
    db_165_sys.run_query("SELECT * FROM V$LOGSTDBY_STATE")
    #db_165_sys.run_query("SELECT SUBSTR(name, 1, 40) AS NAME, SUBSTR(value,1,32) AS VALUE FROM V$LOGSTDBY_STATS")
    db_165_sys.run_query("SELECT APPLIED_SCN, LATEST_SCN, MINING_SCN, RESTART_SCN FROM V$LOGSTDBY_PROGRESS")
    db_165_sys.run_query("SELECT APPLIED_TIME, LATEST_TIME, MINING_TIME, RESTART_TIME FROM V$LOGSTDBY_PROGRESS")
    db_163_sys.run_query("select guard_status from v$database")

################################################################################
@task
def dataguard_setup_logical_standby():
    execute(dg._stop_redo_apply,c.slave_instance2,hosts=['10.0.50.163'])
    NEXT_DEST_NUMBER = 4
    execute(dg._prepare_to_support_logical,c.pri_instance,NEXT_DEST_NUMBER,hosts=['10.0.50.161'])
    execute(dg._transition_to_logical,c.pri_instance,c.slave_instance2,c.pri_tnsname,hosts=['10.0.50.163'])

@task
def dataguard_add_physical_standby():
    execute(dg._add_tns,c.oracle_home,"10.0.50.163",c.slave_instance2,c.slave_tnsname2,hosts=['10.0.50.161'])
    execute(dg._setup_pri_sp_log_archieve,c.pri_instance,[c.slave_instance,c.slave_instance2],[c.slave_tnsname,c.slave_tnsname2],hosts=['10.0.50.161'])
    execute(dg._setup_pri_sp_log_archieve,c.pri_instance,[c.slave_instance,c.slave_instance2],[c.slave_tnsname,c.slave_tnsname2],hosts=['10.0.50.161'])
    #execute(dg._setup_pri_prepare_files,c.pri_instance,[c.slave_instance,c.slave_instance2],[c.slave_tnsname,c.slave_tnsname2],hosts=['10.0.50.161'])

    execute(dg.prepare_dup_slave,c.oracle_base,c.oracle_home,"10.0.50.161",c.pri_instance,c.slave_instance2,c.pri_tnsname,c.slave_tnsname2,hosts=['10.0.50.163'])
    execute(dg.create_standby_onslave,c.oracle_base,c.oracle_password,c.pri_tnsname,c.slave_tnsname2,c.pri_instance,c.slave_instance2,hosts=['10.0.50.163'])


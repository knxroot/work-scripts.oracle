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

def _setup():
    c.remoteFile = admin._backup("oracle","gjzspt")
    admin._dropdb("orcl","gjzspt")
    admin._create_user("orcl","gjzspt","12345678")
    admin._imp_with_localfile("oracle","gjzspt","gjzspt","./dmpfiles/dev_gjzspt_20170309_wd.dmp",'N','N')
    admin._imp_with_remotefile("oracle","gjzspt","gjzspt",c.remoteFile,'Y','Y')

def v_standby():
    _view_pri(db_master_sys)
    #print green("################################################################################")
    #execute(admin._view_db,"orcl",hosts=["10.0.50.161"])
    print green("################################################################################")
    _view_standby(db_slave_sys)
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

def _view_standby(conn):
    _view_database(conn)
    conn.run_query("SELECT SEQUENCE#,APPLIED FROM V$ARCHIVED_LOG ORDER BY SEQUENCE#")

def _view_parameter(conn,name_pattern):
    conn.run_query("SELECT name, value, isdefault FROM v$parameter where name like '%"+name_pattern+"%'")

def _view_database(conn):
    conn.run_query("select INSTANCE_NAME, STATUS, DATABASE_STATUS from v$instance")
    conn.run_query("select name, force_logging from v$database") 
    conn.run_query("select open_mode,database_role,db_unique_name from v$database")
    conn.run_query("select LOG_MODE FROM V$DATABASE")

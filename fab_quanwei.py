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
db_master_jcfx=Orac("jcfx","12345678","10.0.50.161","orcl")
db_master_pub_jcfx=Orac("jcfx","12345678","218.89.222.117","orcl",1523)

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


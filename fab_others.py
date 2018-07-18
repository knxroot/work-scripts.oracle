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
'''
def verify_weiq():
    db_weiq._exec(sqls._create_user('jcfx','12345678'))
    db_weiq_jcfx._exec("select * from dual;")
'''

################################################################################
'''
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
'''

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

@task
def demo2_impdb():
    execute(admin._dropdb_forceful,"orcl","gjzspt_demo2",hosts=['10.0.52.1'])
    execute(admin._createdb,"orcl","gjzspt_demo2","Oe123qwe###",hosts=['10.0.52.1'])
    execute(admin._imp_with_localfile,"oracle","gjzspt","gjzspt_demo2","/home/helong/TencentFiles/2898132719/FileRecv/165.dmp","Y","Y",hosts=['10.0.52.1'])

def temp_impdb():
    execute(admin._dropdb_forceful,"orcl","gjzspt_temp",hosts=['10.0.52.8'])
    execute(admin._createdb,"orcl","gjzspt_temp","12345678",hosts=['10.0.52.8'])
    execute(admin._imp_with_localfile,"oracle","gjzspt","gjzspt_temp","/home/helong/TencentFiles/2898132719/FileRecv/dev_gjzspt_20180423_wd.dmp","Y","N",hosts=['10.0.52.8'])

def dirty_impdb():
    #execute(admin._dropdb_forceful,"orcl","gjzspt_dirty",hosts=['10.0.52.1'])
    #execute(admin._createdb,"orcl","gjzspt_dirty","12345678",hosts=['10.0.52.1'])
    execute(admin._imp_with_localfile,"oracle","gjzspt","gjzspt_dirty","/home/helong/TencentFiles/2898132719/FileRecv/gjzspt20180123.dmp","Y","Y",hosts=['10.0.52.1'])

def bj_165_impdb():
    execute(admin._dropdb_forceful,"orcl","gjzspt_bj_165",hosts=['10.0.52.1'])
    execute(admin._createdb,"orcl","gjzspt_bj_165","12345678",hosts=['10.0.52.1'])
    execute(admin._imp_with_localfile,"oracle","gjzspt","gjzspt_bj_165","/home/helong/TencentFiles/2898132719/FileRecv/gjzspt0118.dmp","Y","Y",hosts=['10.0.52.1'])

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


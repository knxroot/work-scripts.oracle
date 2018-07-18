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
db_test_sys=Orac("sys","oracle","10.0.52.1","orcl")

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


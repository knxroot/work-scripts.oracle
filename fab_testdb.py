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
from utils import *
from utils import _exp,_imp,_backup,_recreatedb

################################################################################
db_test_sys=Orac("sys","oracle","10.0.52.1","orcl")

##############################################################################
@task
def test_backup():
    execute(_exp,"Oe123qwe###","gjzspt_demo2","testdb",hosts=['10.0.52.8'])

@task
def start():
    with settings(warn_only=True):
        execute(admin._startup,"orcl",hosts=["10.0.52.1"])

def syncdb_verify():
    db_dev_sys.run_query(sqls._table_count("GJZSPT")[:-1])
    db_test_sys.run_query(sqls._table_count("GJZSPT")[:-1])
    t1 = db_dev_sys.run_query(sqls._table_names("GJZSPT")[:-1])
    t2 = db_test_sys.run_query(sqls._table_names("GJZSPT")[:-1])

@task
def syncdb():
    execute(_exp,"Oe123qwe###","gjzspt","dev",hosts=['192.168.21.249'])
    execute(_backup,hosts=['10.0.52.1'])
    execute(_recreatedb,hosts=['10.0.52.1'])
    execute(_imp,hosts=['10.0.52.1'])

##############################################################################
def newdev():
    execute(admin._createdb,"orcl","gjzspt_dev","12345678",hosts=['10.0.52.1'])
    execute(admin._imp_with_localfile,"Oe123qwe###","gjzspt","gjzspt_dev",'./dmpfiles/dev_gjzspt_20170914_wd.dmp','Y','N',hosts=['10.0.52.1'])

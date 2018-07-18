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
db_dev_sys=Orac("sys","Oe123qwe###","192.168.21.249","gjzs")
db_test_sys=Orac("sys","oracle","10.0.52.1","orcl")

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
#########################################52.7####################################
def dev_2_52dot7():
    #execute(_exp,"Oe123qwe###","gjzspt","dev",hosts=['192.168.21.249'])
    execute(admin._createdb,"orcl","gjzspt_test","Oe123qwe###",hosts=['10.0.52.7'])
    execute(admin._imp_with_localfile,"oracle","gjzspt","gjzspt_test","/home/helong/he/lky/share/sjgxpt/script/db/dmpfiles/dev_gjzspt_20180303_wd.dmp","Y","Y",hosts=['10.0.52.7'])

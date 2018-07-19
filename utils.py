#!/usr/bin/env python

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

#db_rac=Oracc("sys","oracle","10.0.52.199","orcl")
#db_rac_jcfx=Oracc("jcfx","12345678","10.0.52.199","orcl")

#db_weiq=Oracc("sys","123456789","172.16.7.116","oracle")
#db_weiq_jcfx=Oracc("jcfx","12345678","172.16.7.116","oracle")

db_163_sys=Orac("sys","oracle","10.0.50.163","orcl")
db_163_gjzspt=Orac("gjzspt","12345678","10.0.50.163","orcl")
db_165_sys=Orac("sys","oracle","10.0.50.165","slave")
db_165_gjzspt=Orac("gjzspt","12345678","10.0.50.165","slave")

db_dev_sys=Orac("sys","Oe123qwe###","192.168.21.249","gjzs")
db_test_sys=Orac("sys","oracle","10.0.52.1","orcl")

################################################################################
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


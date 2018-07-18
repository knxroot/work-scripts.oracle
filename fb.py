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
import quanwei
import others
import dev

import fab_dataguard_161 as dg161
import fab_dataguard_163 as dg163


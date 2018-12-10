#import os.path as path
#from os.path import *
#from config import *
from common import *
from utils import *
from utils import _exp

from fabric.api import *
from oracon import Orac
from orarac import Oracc
from fabric.colors import green

import config as c
import oraadmin as admin
import oradg as dg
import sqls as sqls

################################################################################
@task
def old_test_backup():
    execute(_exp,"Oe123qwe###","gjzspt_demo2","test-master",hosts=['10.0.52.8'])
    execute(_exp,"Oe123qwe###","dgap_pre","test-pre",hosts=['10.0.52.1'])

@task
def daoshuju_impdb():
    execute(admin._dropdb_forceful,"orcl","gjzspt_demo2",hosts=['10.0.52.1'])
    execute(admin._createdb,"orcl","gjzspt_demo2","Oe123qwe###",hosts=['10.0.52.1'])
    execute(admin._imp_with_localfile,"oracle","gjzspt","gjzspt_demo2","/home/helong/TencentFiles/2898132719/FileRecv/dmp/20181023_165.dmp","Y","Y",hosts=['10.0.52.1'])

@task
def daoshuju_impdb2():
    execute(admin._dropdb_forceful,"orcl","gjzspt_demo2",hosts=['10.0.52.1'])
    execute(admin._createdb,"orcl","gjzspt_demo2","Oe123qwe###",hosts=['10.0.52.1'])
    execute(admin._imp_with_localfile,"oracle","gjzspt","gjzspt_demo2","/home/helong/TencentFiles/2898132719/FileRecv/20181205-165.dmp","Y","Y",hosts=['10.0.52.1'])

    execute(admin._dropdb_forceful,"orcl","dgap_pre",hosts=['10.0.52.8'])
    execute(admin._createdb,"orcl","dgap_pre","12345678",hosts=['10.0.52.8'])
    execute(admin._imp_with_localfile,"oracle","dgap_pre","dgap_pre","/home/helong/TencentFiles/2898132719/FileRecv/20181205-175-pre.dmp","Y","Y",hosts=['10.0.52.8'])

    execute(admin._dropdb_forceful,"orcl","dgap_dw",hosts=['10.0.52.8'])
    execute(admin._createdb,"orcl","dgap_dw","12345678",hosts=['10.0.52.8'])
    execute(admin._imp_with_localfile,"oracle","dgap_dw","dgap_dw","/home/helong/TencentFiles/2898132719/FileRecv/20181205-175-dw.dmp","Y","Y",hosts=['10.0.52.8'])

@task
def daoshuju_import_pre_step2():
    execute(admin._dropdb_forceful,"orcl","dgap_pre",hosts=['10.0.52.8'])
    execute(admin._createdb,"orcl","dgap_pre","12345678",hosts=['10.0.52.8'])
    #execute(admin._imp_with_localfile,"oracle","dgap_pre","dgap_pre","/home/helong/he/lky/share/sjgxpt/script/db/dmpfiles/test-pre_dgap_pre_20180929_wd.dmp","Y","Y",hosts=['10.0.52.8'])
    execute(admin._imp_with_localfile,"oracle","dgap_pre","dgap_pre","/home/helong/TencentFiles/2898132719/FileRecv/dmp/20181023_pre.dmp","Y","Y",hosts=['10.0.52.8'])

@task
def daoshuju_export_dmp():
    execute(_exp,"Oe123qwe###","gjzspt_demo2","OK",hosts=['10.0.52.1'])

@task
def zaoshuju_impdb():
    execute(admin._dropdb_forceful,"orcl","gjzspt_yang",hosts=['10.0.52.8'])
    execute(admin._createdb,"orcl","gjzspt_yang","12345678",hosts=['10.0.52.8'])
    execute(admin._imp_with_localfile,"oracle","gjzspt","gjzspt_yang","/home/helong/TencentFiles/2898132719/FileRecv/165_20180929_2.dmp","Y","Y",hosts=['10.0.52.8'])


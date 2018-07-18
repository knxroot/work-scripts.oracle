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
from dataguard_ import *

##############################################################################
@task
def dupli_testdb():
    execute(_setup_ori_master,hosts=["10.0.52.1"])
    execute(_setup_new_master,hosts=["10.0.50.161"])

def _setup_ori_master():
    dg._setup_tns(c.oracle_home,env.host,"10.0.50.161","orcl","orcl","master","slave")
    dg._set_archive_mode()

def _setup_new_master():
    dg.prepare_dup_slave(c.oracle_base,c.oracle_home,"10.0.52.1","orcl","orcl")
    dg.dup_m2m_onslave(c.oracle_base,c.oracle_password,c.pri_tnsname,c.slave_tnsname,"orcl","orcl")

def v_dup():
    execute(_view_master)
    execute(_view_new_master)

@roles("dup.db_master")
def _view_master():
    admin._view_db("orcl")

@roles('dup.db_new_master')
def _view_new_master():
    admin._view_db("orcl")

################################################################################
@task
def dataguard_physical_start():
    execute(dg._start_as_physical_slave, "slave", hosts=["10.0.50.162"])
    execute(dg._start_as_physical_master, "orcl", hosts=["10.0.50.161"])

@task
def dataguard_physical_stop():
    execute(dg._stop_with_listener, "orcl", hosts=["10.0.50.161"])
    execute(dg._stop_with_listener, "slave", hosts=["10.0.50.162"])

@task
def dataguard_physical_vlog():
    execute(admin._tail_alert_log,c.oracle_base,"slave",hosts=["10.0.50.162"])
    execute(admin._tail_alert_log,c.oracle_base,"orcl",hosts=["10.0.50.161"])

@task
def dataguard_create_phisical_standby():
    execute(_prepare_dg_master)
    execute(_setup_dg_slave)

@roles('standby.master')
def _prepare_dg_master():
    dg.config_standby_pri(c.oracle_base,c.oracle_home,"10.0.50.162",c.pri_instance,c.slave_instance,c.pri_tnsname,c.slave_tnsname)

@roles('standby.slave')
def _setup_dg_slave():
    dg.prepare_dup_slave(c.oracle_base,c.oracle_home,"10.0.50.161",c.pri_instance,c.slave_instance,c.pri_tnsname,c.slave_tnsname)
    dg.create_standby_onslave(c.oracle_base,c.oracle_password,c.pri_tnsname,c.slave_tnsname,c.pri_instance,c.slave_instance)


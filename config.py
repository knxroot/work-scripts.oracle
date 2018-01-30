#!/usr/bin/env python

from fabric.api import *
from fabric.contrib.console import confirm

import os.path
import datetime

#dryrun=confirm("dry run?")
dryrun=env.has_key("dryrun") and env["dryrun"]=="True"
#if dryrun:
#    print "dryrun True"
#else:
#    print "dryrun False"

#################################################
#now=str(datetime.datetime.now())
now=datetime.datetime.now()
now=now.strftime("%Y%m%d_%H:%M")
#print "now:"+now

localFile="./dmpfiles/gjzspt2017-02-14_wd.dmp"
remoteFile="~/backup_gjzspt_20170215_11:39.dmp"

env.roledefs = {
        'dup.db_master': ['10.0.52.1'],
        'dup.db_new_master': ['10.0.50.161'],
        'standby.master': ['10.0.50.161'],
        'standby.slave': ['10.0.50.162'],
        'sync.db_src': ['192.168.21.249'],
        'sync.db_target': ['10.0.52.1']
        }
#env.hosts = ['10.0.52.1']
env.user = 'oracle'
env.password = 'oracle'
#env.user = 'root'
#env.password = 'sofn@123'

#################################################
#oracle_base="/opt/app/oracle"
#oracle_home="/opt/app/oracle/product/11.2.0/oracle"
oracle_base="/u01/app/oracle"
oracle_home="/u01/app/oracle/product/11.2.0/dbhome_1"
oracle_password="oracle"
pri_instance="orcl"
slave_instance="slave"
slave_instance2="slave2"
pri_tnsname="MASTER"
slave_tnsname="SLAVE"
slave_tnsname2="SLAVE2"

#################################################
standby = {
        'pri': {
            'iname' : 'orcl',
            'tnsname' : 'MASTER' },
        'slv': {
            'iname' : 'slave',
            'tnsname' : 'SLAVE' }
        }



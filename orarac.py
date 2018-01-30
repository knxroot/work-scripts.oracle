#!/usr/bin/env python

import os.path
import datetime

from fabric.api import *

import config as c
from common import *

class Oracc:

    def __init__(self,db_user,db_password,db_ip,sid):
        self.db_user = db_user
        self.db_password = db_password
        self.db_ip = db_ip
        self.sid = sid

    def _exec(self,sql):
        sqlplus(self.db_user,self.db_password,self.db_ip,self.sid,sql)
    
    def _querydual(self):
        sqlplus(self.db_user,self.db_password,self.db_ip,self.sid,"select * from dual;")



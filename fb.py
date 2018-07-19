#import os.path as path
#from os.path import *
#from config import *
from common import *

from fabric.api import *
from fabric.colors import green
from oracon import Orac
from orarac import Oracc

import config as c
import oraadmin as admin
import oradg as dg
import sqls as sqls


################################################################################
import fab_quanwei as quanwei
import fab_others as others
import fab_dev as dev
import fab_testdb as testdb

import fab_dataguard_161 as dg161
import fab_dataguard_163 as dg163


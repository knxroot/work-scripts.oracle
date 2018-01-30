#!/usr/bin/env python

from fabric.api import *
from config import *

def vrun(command):
    print '-------------------------------'
    print command
    if not dryrun:
        run(command)

def lrun(command):
    print '-------------------------------'
    print command
    if not dryrun:
        local(command)

def runsql(instance_name,sqlcommands):
    command = "env ORACLE_SID="+instance_name+" sqlplus / as sysdba <<-'EOI' \n" + sqlcommands +"\nEOI"
    vrun(command)

def sqlplus(user,password,ip,servicename,sqlcommands):
    asrole = ""
    if user == "sys":
        asrole = "as sysdba"
    
    command = "sqlplus64 "+user+"/"+password+"@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST="+ip+")(PORT=1521))(CONNECT_DATA=(SERVICE_NAME="+servicename+")))' "+asrole+" <<-'EOI' \n" + sqlcommands +"\nEOI"
    lrun(command)
    


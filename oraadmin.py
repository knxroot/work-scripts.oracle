#!/usr/bin/env python

import os.path
import datetime

from fabric.api import *

#from config import dryrun as dryrun
from config import *
from common import *

################################################################################

#nls_lang="AMERICAN_AMERICA.ZHS16GBK"
nls_lang="AMERICAN_AMERICA.UTF8"

def _tail_alert_log(oracle_base,instance_name):
    vrun("""sed -n '/ORA-/p' """+oracle_base+"""/diag/rdbms/"""+instance_name+"""/"""+instance_name+"""/trace/alert_"""+instance_name+""".log | tail""")

def _view_db(instance_name):
    #vrun("env | grep oracle")
    #vrun("locate '*.ora'")
    runsql(instance_name,"show parameter DB_NAME;")
    runsql(instance_name,"show parameter DB_UNIQUE_NAME;")
    runsql(instance_name,"show parameter DB_DOMAIN;")
    runsql(instance_name,"show parameter SERVICE_NAMES;")
    runsql(instance_name,"show parameter LOG_ARCHIVE_DEST_1;")
    runsql(instance_name,"ARCHIVE LOG LIST;")
    runsql(instance_name,"show parameter background_dump_dest;")

def _startup(instance):
    vrun("""lsnrctl start""")
    vrun("""env ORACLE_SID="""+instance+""" sqlplus / as sysdba <<-EOI
startup;
EOI""")

def _unlock_user(instance_name, user_name):
    runsql(instance_name,"ALTER USER "+user_name+" ACCOUNT UNLOCK;")

def _reset_user_password(instance_name, user_name, pass_word):
    runsql(instance_name,"alter user "+user_name+" identified by "+pass_word+";")

def _create_user(instance_name, user_name, pass_word):
    runsql(instance_name,"""CREATE USER """+user_name+""" IDENTIFIED BY """+pass_word+""";
grant create session to """+user_name+""";
ALTER USER """+user_name+""" QUOTA UNLIMITED ON USERS;""")

def _grant_dg_priviliges(instance_name, user_name):
    runsql(instance_name,"""GRANT EXECUTE ANY PROCEDURE TO """+user_name+""";""")

def _grant_mv_priviliges(instance_name, user_name):
    runsql(instance_name,"""GRANT CREATE MATERIALIZED VIEW TO """+user_name+""";
GRANT QUERY REWRITE TO """+user_name+""";
GRANT CREATE ANY TABLE TO """+user_name+""";
GRANT SELECT ANY TABLE TO """+user_name+""";
GRANT UNLIMITED TABLESPACE TO """+user_name+""";""")

def _grant_additional_priviliges(instance_name, user_name):
    runsql(instance_name,"""GRANT CREATE TRIGGER TO """+user_name+""";
GRANT CREATE SEQUENCE TO """+user_name+""";
GRANT CREATE PROCEDURE TO """+user_name+""";""")

################################################################################
def _clear_tables():
    pass 

def _enable_audit(instance_name):
    runsql(instance_name,"alter system set AUDIT_TRAIL=DB scope=spfile;")

def _enable_audit2(instance_name,user_name):
    runsql(instance_name,"alter system set AUDIT_TRAIL=DB scope=spfile;")
    runsql(instance_name,"audit all by "+user_name+";")

def _restart(instance_name):
    runsql(instance_name,"""SHUTDOWN IMMEDIATE;
STARTUP;""")

def _dropdb(instance_name,schema_name):
    runsql(instance_name,"DROP USER "+schema_name+" CASCADE;")

def _dropdb_forceful(instance_name,schema_name):
    runsql(instance_name,"""shutdown immediate;
startup restrict;
drop user """+schema_name+""" cascade;
shutdown immediate;
startup;""")


def _createdb(instance_name,schema_name,password):
    runsql(instance_name,"""CREATE USER """+schema_name+""" IDENTIFIED BY """+password+""";
GRANT CONNECT TO """+schema_name+""";
GRANT RESOURCE TO """+schema_name+""";""")

def _drop_tables(instance_name,schema_name):
    runsql(instance_name,"""BEGIN
    FOR table_ IN (SELECT * FROM dba_tables where owner like '"""+schema_name+"""') LOOP
        execute immediate 'drop table ' || table_.owner || '.' || table_.table_name;
    END LOOP;
END;""")

def _backup_to_localfile(db_password,schema_name,localfile):
    remotefile = _backup(db_password,schema_name)
    if dryrun:
        print "get("+remotefile+","+localfile+")"
    else:
        get(remotefile,localfile)

def _backup(db_password,schema_name):
    remotefile="~/backup_"+schema_name+"_"+now+".dmp"

    exp_command="env NLS_LANG="+nls_lang+" exp userid=system/"+db_password+" owner="+schema_name+"  ROWS=Y file="+remotefile
    vrun(exp_command)
    return remotefile

def _imp_with_localfile(db_password,from_schema,to_schema,localfile,withdata,onlydata):
    dmpfile_name = os.path.basename(localfile)
    remotefile="~/"+dmpfile_name
    if dryrun:
        print "put("+localfile+","+remotefile+")"
    else:
        print "put("+localfile+","+remotefile+")"
        put(localfile,remotefile)
    _imp_with_remotefile(db_password,from_schema,to_schema,remotefile,withdata,onlydata);


def _imp_with_remotefile(db_password,from_schema,to_schema,remotefile,withdata,onlydata):
    imp_command="env NLS_LANG="+nls_lang+" imp userid=\\'system/"+db_password+" as sysdba\\' fromuser="+from_schema+" touser="+to_schema+" IGNORE="+onlydata+" ROWS="+withdata+" file="+remotefile
    vrun(imp_command)

def _help():
    #print "dryrun:" + dryrun
    print "dryrun:%s" % dryrun
    pass


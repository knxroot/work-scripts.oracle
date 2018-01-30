#!/usr/bin/env python

def _table_count(schema):
    return """SELECT count(*) FROM DBA_OBJECTS WHERE owner ='"""+schema+"""' AND object_type = 'TABLE';"""

def _table_names(schema):
    return """SELECT object_name, object_type FROM DBA_OBJECTS WHERE owner ='"""+schema+"""' AND object_type = 'TABLE';"""

def _alter_conn_limits(processes):
    return """ALTER system SET processes="""+processes+""" scope=spfile;"""

def _view_parameter(name_pattern):
    return "SELECT name, value, isdefault FROM v$parameter where name like '%"+name_pattern+"%';"

def _view_conn_limits():
    return """SELECT * FROM v$resource_limit WHERE resource_name IN ('processes','sessions');"""

def _create_user(user_name, pass_word):
    return """CREATE USER """+user_name+""" IDENTIFIED BY """+pass_word+""";
grant create session to """+user_name+""";"""

def _grant_mv_priviliges(user_name):
    return """GRANT CREATE MATERIALIZED VIEW TO """+user_name+""";
GRANT QUERY REWRITE TO """+user_name+""";
GRANT CREATE ANY TABLE TO """+user_name+""";
GRANT SELECT ANY TABLE TO """+user_name+""";
GRANT UNLIMITED TABLESPACE TO """+user_name+""";"""

def _dropdb(schema_name):
    return "DROP USER "+schema_name+" CASCADE;"

def _dropdb_forceful(schema_name):
    return """shutdown immediate;
startup restrict;
drop user """+schema_name+"""cascade;
shutdown immediate;
startup;"""

def _createdb(schema_name,password):
    return """CREATE USER """+schema_name+""" IDENTIFIED BY """+password+""";
GRANT CONNECT TO """+schema_name+""";
GRANT RESOURCE TO """+schema_name+""";"""

def _drop_tables(schema_name):
    return """BEGIN
    FOR table_ IN (SELECT * FROM dba_tables where owner like '"""+schema_name+"""') LOOP
        execute immediate 'drop table ' || table_.owner || '.' || table_.table_name;
    END LOOP;
END;"""

def _drop_table(table_name):
    return """drop table """+table_name+""";"""

def _backup(db_password,schema_name,remotefile):
    return "exp userid=system/"+db_password+" owner="+schema_name+"  ROWS=Y file="+remotefile

def _imp_with_remotefile(db_password,from_schema,to_schema,remotefile,withdata,onlydata):
    return "imp userid=system/"+db_password+" fromuser="+from_schema+" touser="+to_schema+" IGNORE="+onlydata+" ROWS="+withdata+" file="+remotefile

def _create_table_ws_log():
    return """CREATE TABLE "T_DGAP_WS_LOG" (  
"ID" VARCHAR2(64 CHAR), 
"RESOURCE_DIR" VARCHAR2(64 CHAR), 
"WEB_SERVICE_ID" VARCHAR2(64 CHAR), 
"WEB_SERVICE_NAME" VARCHAR2(50 CHAR), 
"METHOD_NAME" VARCHAR2(50 CHAR), 
"CALLER_USER" VARCHAR2(64 CHAR), 
"ERROR_TYPE" VARCHAR2(10 CHAR), 
"ERROR_DESC" VARCHAR2(100 CHAR), 
"INVOKE_START_DATE" TIMESTAMP (6), 
"INVOKE_END_DATE" TIMESTAMP (6), 
"ERROR_DATE" TIMESTAMP (6), 
"CREATE_BY" VARCHAR2(64 CHAR), 
"CREATE_TIME" DATE DEFAULT SYSDATE, 
"UPDATE_BY" VARCHAR2(64 CHAR), 
"UPDATE_TIME" DATE DEFAULT SYSDATE, 
"DEL_FLAG" VARCHAR2(10 CHAR) DEFAULT 'N', 
"RESERVED_FIELD1" VARCHAR2(200 CHAR), 
"RESERVED_FIELD2" VARCHAR2(200 CHAR), 
"RESERVED_FIELD3" VARCHAR2(200 CHAR), 
"RESERVED_FIELD4" VARCHAR2(200 CHAR), 
"RESERVED_FIELD5" VARCHAR2(200 CHAR), 
"RESERVED_FIELD6" VARCHAR2(200 CHAR), 
"RESERVED_FIELD7" VARCHAR2(200 CHAR), 
"RESERVED_FIELD8" VARCHAR2(200 CHAR), 
"RESERVED_FIELD9" VARCHAR2(200 CHAR), 
"RESERVED_FIELD10" VARCHAR2(200 CHAR), 
"RESERVED_FIELD11" VARCHAR2(200 CHAR), 
"RESERVED_FIELD12" VARCHAR2(200 CHAR), 
"RESERVED_FIELD13" VARCHAR2(200 CHAR), 
"RESERVED_FIELD14" VARCHAR2(200 CHAR), 
"RESERVED_FIELD15" VARCHAR2(200 CHAR), 
"RESERVED_FIELD16" VARCHAR2(200 CHAR), 
"RESERVED_FIELD17" VARCHAR2(200 CHAR), 
"RESERVED_FIELD18" VARCHAR2(200 CHAR), 
"RESERVED_FIELD19" VARCHAR2(200 CHAR), 
"RESERVED_FIELD20" VARCHAR2(200 CHAR)
);"""


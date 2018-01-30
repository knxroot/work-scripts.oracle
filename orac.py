#!/usr/bin/env python
from fabric.api import *
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from tabulate import tabulate
import pandas

def run_query(db_user,db_password,ip,sid,sql):
    #conn_str='oracle+cx_oracle://gjzspt:12345678@192.168.21.249:1521/gjzs'
    conn_str='oracle+cx_oracle://'+db_user+':'+db_password+'@'+ip+':1521/'+sid
    if db_user == 'SYS' or db_user == 'sys' :
        conn_str += '?mode=2'
    #conn_str='oracle+cx_oracle://sys:oracle@10.0.52.1:1521/orcl?mode=2'
    engine = create_engine(conn_str, echo=False)
    conn = engine.connect()
    s=text(sql)
    r = conn.execute(s)
    rdata = r.fetchall()
    conn.close()
    print sql
    print '--------------------------------------------------------------------------------'
    print pandas.DataFrame(rdata,columns=r.keys())
    #print tabulate(r)

def run_statement(db_user,db_password,ip,sid,sql):
    conn_str='oracle+cx_oracle://'+db_user+':'+db_password+'@'+ip+':1521/'+sid
    if db_user == 'SYS' or db_user == 'sys' :
        conn_str += '?mode=2'
    #conn_str='oracle+cx_oracle://sys:oracle@10.0.52.1:1521/orcl?mode=2'
    engine = create_engine(conn_str, echo=False)
    conn = engine.connect()
    s=text(sql)
    print sql
    conn.execute(s)
    #print 'execute finished'
    conn.close()

def query(sql):
    conn_str='oracle+cx_oracle://gjzspt:12345678@192.168.21.249:1521/gjzs'
    engine = create_engine(conn_str, echo=False)
    conn = engine.connect()
    #s=text('select * from dual')
    s=text(sql)
    r = conn.execute(s).fetchall()
    conn.close()
    return r

def charset():
    #print query('select * from dual')
    r = query('select * from nls_database_parameters')
    #print tabulate(r)
    print pandas.DataFrame(r,columns=['NAME','VALUE'])
    #print tabulate(query('select * from t_dgap_resource'))

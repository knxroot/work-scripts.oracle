#!/usr/bin/env python
from fabric.api import *
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from tabulate import tabulate
import pandas

class Orac:

    def __init__(self,db_user,db_password,db_ip,sid,port=1521):
        self.db_user = db_user
        self.db_password = db_password
        self.db_ip = db_ip
        self.sid = sid
        self.port = port
        pandas.set_option('display.max_rows', 500)

    def run_query(self,sql):
        #conn_str='oracle+cx_oracle://gjzspt:12345678@192.168.21.249:1521/gjzs'
        conn_str='oracle+cx_oracle://'+self.db_user+':'+self.db_password+'@'+self.db_ip+':'+str(self.port)+'/'+self.sid
        if self.db_user == 'SYS' or self.db_user == 'sys' :
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
        result = pandas.DataFrame(rdata,columns=r.keys())
        print result
        return result

    def run_statement(self,sql):
        conn_str='oracle+cx_oracle://'+self.db_user+':'+self.db_password+'@'+self.db_ip+':'+str(self.port)+'/'+self.sid
        if self.db_user == 'SYS' or self.db_user == 'sys' :
            conn_str += '?mode=2'
        #conn_str='oracle+cx_oracle://sys:oracle@10.0.52.1:1521/orcl?mode=2'
        engine = create_engine(conn_str, echo=False)
        conn = engine.connect()
        s=text(sql)
        print sql
        conn.execute(s)
        #print 'execute finished'
        conn.close()

    def charset(self):
        run_query('select * from nls_database_parameters')

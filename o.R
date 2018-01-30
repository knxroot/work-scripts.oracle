#!/usr/bin/env Rscript

library(RJDBC)

drv<-JDBC("oracle.jdbc.driver.OracleDriver",classPath="/usr/lib/oracle/11.2/client64/lib/ojdbc6.jar")
sys161<-dbConnect(drv, "jdbc:oracle:thin:system/oracle@10.0.50.161:1521:orcl")
gjzspt249<-dbConnect(drv, "jdbc:oracle:thin:gjzspt/12345678@192.168.21.249:1521:gjzs")

fauditTrail<-function(con) {
	dbGetQuery(con,'select EXTENDED_TIMESTAMP,OS_USER,userhost,os_process,DB_USER,OBJECT_SCHEMA,OBJECT_NAME,RETURNCODE,STATEMENT_TYPE,SQL_TEXT,AUDIT_TYPE from DBA_COMMON_AUDIT_TRAIL order by EXTENDED_TIMESTAMP desc,LOGOFF_TIME desc')
}
fparameters<-function(con,pattern) {
	dbGetQuery(con,paste("SELECT name, value, isdefault FROM v$parameter where name like '%",pattern,"%'"))
}
#head(auditTrail)
fdgapTables<-function(con) {
	t <- dbGetTables(con)
	t_dgap <- t[grep('T_DGAP',t$TABLE_NAME),]
}

auditTrail161<-fauditTrail(sys161)
parameters161<-fparameters(sys161,"file")
dgapTables161<-fdgapTables(sys161)
#auditTrail249<-fauditTrail(sys249)

fcloseCon<-function() {
	dbDisconnect(sys161)
	dbDisconnect(gjzspt249)
	dbDisconnect(sys249)
}


#!/usr/bin/env Rscript

library(RJDBC)
drv =JDBC("oracle.jdbc.driver.OracleDriver",classPath="/usr/lib/oracle/11.2/client64/lib/ojdbc6.jar")
con =dbConnect(drv, "jdbc:oracle:thin:system/oracle@10.0.50.161:1521:orcl")
auditTrail =dbGetQuery(con,'select EXTENDED_TIMESTAMP,OS_USER,userhost,os_process,DB_USER,OBJECT_SCHEMA,OBJECT_NAME,RETURNCODE,STATEMENT_TYPE,SQL_TEXT,AUDIT_TYPE from DBA_COMMON_AUDIT_TRAIL order by EXTENDED_TIMESTAMP desc,LOGOFF_TIME desc')
head(auditTrail)
t <- dbGetTables(con)
t_dgap <- t[grep('T_DGAP',t$TABLE_NAME),]

#!/usr/bin/env Rscript

library(RJDBC)
library(compare)

drv<-JDBC("oracle.jdbc.driver.OracleDriver",classPath="/usr/lib/oracle/11.2/client64/lib/ojdbc6.jar")

gjzspt521<-dbConnect(drv, "jdbc:oracle:thin:gjzspt/12345678@10.0.52.1:1521:orcl")

t1<-dbGetTables(gjzspt521)
d1<-dbReadTable(gjzspt521,'SYS_USER')

x1<-dbGetQuery(gjzspt521,'select * from SYS_USER order by id')

fcloseCon<-function() {
	dbDisconnect(gjzspt521)
	dbDisconnect(gjzsptdemo521)
}


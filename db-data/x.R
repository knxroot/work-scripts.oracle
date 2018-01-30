#!/usr/bin/env Rscript

library(RJDBC)

drv<-JDBC("oracle.jdbc.driver.OracleDriver",classPath="/usr/lib/oracle/11.2/client64/lib/ojdbc6.jar")
gjzspt249<-dbConnect(drv, "jdbc:oracle:thin:gjzspt/12345678@192.168.21.249:1521:gjzs")

#head(auditTrail)
gjzsptTables<-function(con) {
	t <- dbGetTables(con)
	t_dgap <- t[grep('GJZSPT',t$TABLE_SCHEM),]
}

exportTableData<-function(con,tablename) {
	data <- dbReadTable(con,tablename)
	write.csv(data,paste(tablename,".csv",sep=""))
	data
}

exportGjzsptTables<-function(con) {
	tables <- gjzsptTables(con)
	tablenames <- tables$TABLE_NAME
	tablenames <- setdiff(tablenames,c("ACT_GE_BYTEARRAY"))
	for (tn in tablenames) {
		print(paste("table name:",tn))
		exportTableData(con, tn)
	}
}

gjzsptTables249<-gjzsptTables(gjzspt249)
wslog<-exportTableData(gjzspt249,"T_DGAP_WS_LOG")
#exportGjzsptTables(gjzspt249)

fcloseCon<-function() {
	dbDisconnect(gjzspt249)
}


#!/usr/bin/env Rscript

library(RJDBC)
drv =JDBC("oracle.jdbc.driver.OracleDriver",classPath="/usr/lib/oracle/11.2/client64/lib/ojdbc6.jar")
con =dbConnect(drv, "jdbc:oracle:thin:gjzspt/12345678@192.168.21.249:1521:gjzs")
ws_log =dbReadTable(con,'T_DGAP_WS_LOG')
t <- dbGetTables(con)
t_dgap <- t[grep('T_DGAP',t$TABLE_NAME),]

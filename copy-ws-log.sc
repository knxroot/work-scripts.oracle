 val ws_log=spark.read.format("jdbc").options(Map("url"->"jdbc:oracle:thin:@192.168.21.249:1521:gjzs","user"->"gjzspt","password"->"12345678","dbtable"->"t_dgap_ws_log","driver"->"oracle.jdbc.driver.OracleDriver")).load().cache()
 ws_log
 val prop = new java.util.Properties
 prop.setProperty("driver", "oracle.jdbc.driver.OracleDriver")
 prop.setProperty("user", "dgap_dw_empty")
 prop.setProperty("password","12345678")
 val url="jdbc:oracle:thin:@10.0.52.1:1521:orcl"
 val table="ws_log"
 ws_log.write.jdbc(url,table,prop)

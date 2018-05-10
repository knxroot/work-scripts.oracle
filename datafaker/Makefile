JDBC_USER:=gjzspt
JDBC_PASSWORD:=12345678
JDBC_URL=jdbc:oracle:thin:@192.168.21.249:1521:gjzs 

schema.xml:
	mvn -o com.maoren.plugin:ddlutils-maven-plugin:d2x -DjdbcDriver=oracle.jdbc.OracleDriver -DjdbcUser=$(JDBC_USER) -DjdbcPassword=$(JDBC_PASSWORD) -DjdbcUrl=$(JDBC_URL) -DschemaFile="$@"

#!/usr/bin/env ruby -w
=begin
  CREATE TABLE "GJZSPT"."T_DGAP_WS_ERROR_LOG" 
   (	"ID" VARCHAR2(64 BYTE), 
	"RESOURCE_DIRECTORY_ID" VARCHAR2(20 BYTE), 
	"WEB_SERVICE_ID" VARCHAR2(20 BYTE), 
	"WEB_SERVICE_NAME" VARCHAR2(50 BYTE), 
	"METHOD_NAME" VARCHAR2(50 BYTE), 
	"CALLER_USER" VARCHAR2(20 BYTE), 
	"ERROR_TYPE" VARCHAR2(10 BYTE), 
	"ERROR_DESC" VARCHAR2(100 BYTE), 
	"ERROR_DATE" DATE, 
	"CREATE_BY" VARCHAR2(64 BYTE), 
	"CREATE_TIME" DATE DEFAULT SYSDATE, 
	"UPDATE_BY" VARCHAR2(64 BYTE), 
	"UPDATE_TIME" DATE DEFAULT SYSDATE, 
	"DEL_FLAG" VARCHAR2(20 BYTE) DEFAULT 'N', 
	"RESERVED_FIELD1" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD2" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD3" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD4" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD5" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD6" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD7" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD8" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD9" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD10" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD11" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD12" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD13" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD14" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD15" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD16" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD17" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD18" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD19" VARCHAR2(200 BYTE), 
	"RESERVED_FIELD20" VARCHAR2(200 BYTE)
   ) SEGMENT CREATION DEFERRED 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  TABLESPACE "USERS" ;
=end
#"ID", "RESOURCE_DIRECTORY_ID", "WEB_SERVICE_ID", "WEB_SERVICE_NAME", "METHOD_NAME", "CALLER_USER", "ERROR_TYPE", "ERROR_DESC", "ERROR_DATE", "CREATE_BY", "CREATE_TIME", "UPDATE_BY", "UPDATE_TIME", "DEL_FLAG", "RESERVED_FIELD1", "RESERVED_FIELD2", "RESERVED_FIELD3", "RESERVED_FIELD4", "RESERVED_FIELD5", "RESERVED_FIELD6", "RESERVED_FIELD7", "RESERVED_FIELD8", "RESERVED_FIELD9", "RESERVED_FIELD10", "RESERVED_FIELD11", "RESERVED_FIELD12", "RESERVED_FIELD13", "RESERVED_FIELD14", "RESERVED_FIELD15", "RESERVED_FIELD16", "RESERVED_FIELD17", "RESERVED_FIELD18", "RESERVED_FIELD19", "RESERVED_FIELD20"

require 'securerandom'

for x in 1..100
	`echo "#{SecureRandom.hex},directoryId_#{SecureRandom.hex 1},serviceId_#,serviceName_#,methodName_#,callUser_#,et1,errorDescription_#," >>wel.csv`
end

#!/usr/bin/env ruby

class Ora

	def initialize(dry_run:true,ip:"192.168.21.249",sys_password:"12345678",instance_name:"gjzs")
		@dry_run=dry_run
		@ip=ip
		@sys_password=sys_password
		@instance_name=instance_name
	end

	def test_conn()
		run "sqlplus64 gjzspt/12345678@192.168.21.249/gjzs <<-EOI
		select * from dual;
		EOI"
	end

	def clear_data(username, password)
		run "sqlplus64 #{username}/#{password}@#{@ip}/#{@instance_name} <<-EOI
		truncate table T_DGAP_ALERT_CONFIG;
		truncate table T_DGAP_ALERT_LOG;
		truncate table T_DGAP_ALERT_RECEIPT;
		truncate table T_DGAP_ALERT_DATA_IMPORT_FIELD;
		truncate table T_DGAP_ALERT_DATA_IMPORT_TABLE;
		truncate table T_DGAP_RESOURCE;
		truncate table T_DGAP_RESOURCE_APPLICATION;
		truncate table T_DGAP_RESOURCE_DIRECTORY;
		truncate table T_DGAP_ROLE_RESOURCE;
		truncate table T_DGAP_TB_RESOURCE_CONFIG;
		truncate table T_DGAP_WS_DAILY_STAT;
		truncate table T_DGAP_WS_ERROR_LOG;
		truncate table T_DGAP_WS_LOG;
		EOI"
	end

	def create_schema(username, password)
		run "sqlplus64 sys/#{@sys_password}@#{@ip}/#{@instance_name} AS SYSDBA <<-EOI
		CREATE USER #{username} IDENTIFIED BY #{password};
		GRANT CONNECT TO #{username};
		GRANT RESOURCE TO #{username};
		EOI"
	end

	def drop_schema(username)
		run "sqlplus64 sys/#{@sys_password}@#{@ip}/#{@instance_name} AS SYSDBA <<-EOI
		DROP USER #{username};
		EOI"
	end

	def unlock_user(username)
		run "sqlplus64 sys/#{@sys_password}@#{@ip}/#{@instance_name} AS SYSDBA <<-EOI
		ALTER USER #{username} ACCOUNT UNLOCK;
		EOI"
	end

	def run(command)
		puts command
		if not @dry_run
			system command
		end
	end
end
#test_conn

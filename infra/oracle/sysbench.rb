#!/usr/bin/env ruby

class Sysbench

	def prepare
		run "sysbench --test=oltp --mysql-table-engine=innodb --mysql-host=#{@hosts} --mysql-port=#{@port} --mysql-db=test --oltp-table-size=#{@table_size} --mysql-user=root --mysql-password=mb123qwe prepare"
	end

	def run
		run "sysbench --num-threads=#{@threads} --test=oltp --mysql-table-engine=innodb --mysql-host=#{@hosts} --mysql-port=#{@port} --mysql-db=test --oltp-table-size=#{@table_size} --mysql-user=root --mysql-password=mb123qwe run"
	end

	def clean
		run "sysbench --num-threads=#{@threads} --test=oltp --mysql-table-engine=innodb --mysql-host=#{@hosts} --mysql-port=#{@port} --mysql-db=test --oltp-table-size=#{@table_size} --mysql-user=root --mysql-password=mb123qwe cleanup"
	end

	def initialize(threads, mode)
		@threads = threads
		@hosts = "192.168.21.243,192.168.21.246,192.168.21.247"
		@port = 3306
		@table_size = 500000
	end

	def run(command)
		puts command
		system command
	end

end

#/usr/bin/env ruby

class Db 
	def initialize(dry_run,withdata)
		@dry_run=dry_run
		@withdata=withdata
	end

	def exp(ip,username,password,db_password,schema,local_dir)
		#dmpfile_name=schema+`date +%F_%T`.strip+".dmp"
		if @withdata
			dataflag="wd"
			wr="Y"
		else
			dataflag="nd"
			wr="N"
		end
		dmpfile_name=schema+`date +%F`.strip+"_#{dataflag}.dmp"
		remotefile="/home/#{username}/#{dmpfile_name}"
		localfile=local_dir+"/"+dmpfile_name

		#exp userid=system/Oe123qwe### owner=gjzspt file=gjzspt.dmp
		exp_command="'exp userid=system/"+db_password+" owner=#{schema}  ROWS=#{wr} file=#{remotefile}"+"'"
		#exp_command="'which exp'"
		exp_command='"bash -ic '+exp_command+'"'

		run "sshpass -p #{password} ssh -t #{username}@#{ip} #{exp_command}"
		cp_command="scp #{username}@#{ip}:#{remotefile} #{localfile}"
		run "sshpass -p #{password} #{cp_command}"
	end

	def imp(ip,username,password,db_password,from_schema,to_schema,localfile)
		if @withdata
			wr="Y"
		else
			wr="N"
		end

		dmpfile_name=`basename #{localfile}`.strip
		remotefile="/home/#{username}/#{dmpfile_name}"
		cp_command="scp #{localfile} #{username}@#{ip}:#{remotefile}"
		run "sshpass -p #{password} #{cp_command}"

		imp_command="'imp userid=system/"+db_password+" fromuser=#{from_schema} touser=#{to_schema} ROWS=#{wr} file=#{remotefile}"+"'"
		#imp_command="'which imp'"
		imp_command='"bash -ic '+imp_command+'"'

		run "sshpass -p #{password} ssh -t #{username}@#{ip} #{imp_command}"
	end

	def run(command)
		puts command
		if not @dry_run
			system command
		end
	end
end

$dry_run=Db.new(true, false)
$run=Db.new(false, false)

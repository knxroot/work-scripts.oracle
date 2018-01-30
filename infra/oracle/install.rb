#!/usr/bin/env ruby

class Install
	def initialize(env)
		@inventory = env
	end

	def install
		cmd = %Q/ansible-playbook -i #{@inventory} -t install site.yaml/
		run cmd
	end

	def upload_files
		cmd = %Q/ansible-playbook -i #{@inventory} -t copy_files site.yaml/
		run cmd
	end

	def install_java8
		cmd = %Q/ansible-playbook -i #{@inventory} -t install_java8 site.yaml/
		run cmd
	end
	
	def install_oracle11g
		cmd = %Q/ansible-playbook -i #{@inventory} -t install_oracledb site.yaml/
		run cmd
	end

	def install_nexus
		cmd = %Q/ansible-playbook -i #{@inventory} -t install_nexus -l code site.yaml/
		run cmd
	end

	def install_nexus_service
		cmd = %Q/ansible-playbook -i #{@inventory} -t install_nexus_service -l code site.yaml/
		run cmd
	end

	def setup(limit)
		cmd = %Q/ansible-playbook -i #{@inventory} --tags="setup" -l #{limit} site.yaml/
		run cmd
	end

	def setup_user(limit)
		cmd = %Q/ansible-playbook -i #{@inventory} --tags="setup_user" -l #{limit} site.yaml/
		run cmd
	end

	def upload_files(limit)
		cmd = %Q/ansible-playbook -i #{@inventory} -t copy_files -l #{limit} site.yaml/
		run cmd
	end

	def install_oracle11g(limit)
		cmd = %Q/ansible-playbook -i #{@inventory} -t install_oracledb -l #{limit} site.yaml/
		run cmd
	end

	def post_install_oracle11g_service(limit)
		cmd = %Q/ansible-playbook -i #{@inventory} -t post_oracle_install_service -l #{limit} site.yaml/
		run cmd
	end

	def preview(tags,limit)
		cmd = %Q/ansible-playbook --list-hosts --list-tags --list-tasks -i #{@inventory} -l #{limit} site.yaml/
		run cmd
	end

	def syntax(limit)
		cmd = %Q/ansible-playbook --syntax-check -i #{@inventory} site.yaml/
		run cmd
	end

	def dryrun(tags,limit)
		cmd = %Q/ansible-playbook -C -i #{@inventory} -l #{limit} site.yaml/
		run cmd
	end

	def run(command)
		puts command
		system command
	end

	def test
		1.upto(5) do |i|
			puts "#{i}, Infinity, the star that would not die"
		end
	end

end

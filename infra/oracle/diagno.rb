#!/usr/bin/env ruby

class Diagno

	def setup
		run "ansible -i #{@inventory} all -m setup >setup.txt"
	end

	def ping
		run "ansible -i #{@inventory} all -m ping"
	end

	def check_inet
		run "ansible -i #{@inventory} all -m command -a 'ping -c 5 www.baidu.com'"
	end

	def check_hw
		run "ansible-playbook -i #{@inventory} -t diagnose site.yaml"
	end

	def t_check_hw
		run "ansible-playbook -i #{@inventory} -t diagnose site.yaml"
	end

	def initialize(env)
		@inventory = env
	end

	def run(command)
		puts command
		system command
	end

	def interactive
		print "inventory:"
		env=gets()
		puts "inventory:#{env}"
		setup(env)
	end
end

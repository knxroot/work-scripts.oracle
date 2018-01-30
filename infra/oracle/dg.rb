#!/usr/bin/env ruby

class Oradg


	def ansible
		run "ansible -i #{@inventory} all -m command -a 'ping -c 5 www.baidu.com'"
	end

	def playbook
		run "ansible-playbook -i #{@inventory} #{@playbook} -c local -vvv"
	end

	def initialize(env)
		@inventory = env
		@playbook = "oracle-dg.yml"
	end

	def run(command)
		puts command
		system command
	end
end

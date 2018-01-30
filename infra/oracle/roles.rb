#!/usr/bin/env ruby -w

class Roles
	def self.install
		puts """`ansible-galaxy install medzin.oracle-jdk -p ./roles; ansible-galaxy install abessifi.weblogic -p ./roles; ansible-galaxy install AerisCloud.zookeeper -p ./roles; ansible-galaxy install ellotheth.oracle -p ./roles;`"""
		puts """`ansible-galaxy install cchurch.memcached -p ./roles; ansible-galaxy install geerlingguy.nginx -p ./roles `"""
		puts """`ansible-galaxy install mchlumsky.sudoersd -p ./roles`"""
		puts """`ansible-galaxy install hullufred.nexus -p ./roles`"""
	end
end


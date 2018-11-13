SHELL:=/usr/bin/zsh

all:

sqlfiles:
	svn export https://192.168.21.251/svn/CodeRepository/GuoJiaZhuiSuPingTai/BusinessSystem/sofn-server/sofn-asms-service/src/main/resources/sql/asms-upgrade-2018-11-12.sql


.PHONY: all

SHELL:=/usr/bin/zsh
SQLFILES:=asms-upgrade.sql ales-upgrade.sql ads-upgrade.sql tts-upgrade.sql# dgap-upgrade.sql
OUTPUTSQL:=schema-update.sql
SVN_ROOT:=https://192.168.21.251/svn/CodeRepository/GuoJiaZhuiSuPingTai/BusinessSystem

all: $(SQLFILES) $(OUTPUTSQL)

init: 
	#jo -p local="$$(jo -p url="gjzspt_demo2/Oe123qwe###@10.0.52.1:1521/orcl")" dev="$$(jo -p url="gjzspt/12345678@192.168.21.249:1521/gjzs")" test="$$(jo url="gjzspt_demo2/Oe123qwe###@10.0.52.8:1521/orcl")" >db.json
	jj -p -i schema.json -o schema.json -v "2018-11-11" sync-date

db.json: rdp/ds-all.json
	cp $< $@

.ONESHELL:
%-upgrade.sql:
	typeset -A prjs=(ads sofn-ads-service asms sofn-asms-service ales sofn-ales-service tts sofn-tts-service-branch)
	prj=$${prjs[$*]}
	#print -l $$prj
	files=($$(comm -23 =(svn ls $(SVN_ROOT)/sofn-server/$$prj/src/main/resources/sql | sort) =(svn ls $(SVN_ROOT)/sofn-server/$$prj/src/main/resources/sql@{$$(command jq -r '.sqls.$*."last-fetch-date"' schema.json)} | sort)))
	rm -rf schema-updates/$*
	svn co --depth empty $(SVN_ROOT)/sofn-server/$$prj/src/main/resources/sql schema-updates/$*
	#eval svn update schema-updates/$*/{$${(j:,:)files}}
	svn update schema-updates/$*/$$files
	eval cat schema-updates/$*/*(.on) >$@
	print -n '\n' >>$@
	jj -p -i schema.json -o schema.json -v $(shell date +%F) sqls.$*.last-fetch-date

#schema-update.sql: bjdbclean/bj7/tts.sql bjdbclean/bj7/ads-upgrade-2018-11-12.sql bjdbclean/bj7/ales.sql bjdbclean/bj7/asms-upgrade-2018-11-12.sql
schema-update.sql: $(SQLFILES)
	cat $^ >$@
	dos2unix $@

updatedb-dev updatedb-local updatedb-test:

updatedb-%: db.json
	sqlplus64 "$$(command jq -r '.$*.yw.dsn' db.json)" <schema-update.sql | ts | tee -a updatedb.log
	jj -p -i schema.json -o schema.json -v $(shell date +%F) $*.last-sync-date

checkdb-all: checkdb-local checkdb-dev checkdb-test
	@echo checking

checkdb-%: db.json
	@echo checking $*
	$(call checkdb,.$*.yw.dsn)
	$(call checkdb,.$*.pre.dsn)
	$(call checkdb,.$*.dw.dsn)

clean:
	rm $(SQLFILES)
	rm -rf schema-updates
	rm db.json

#$(call checkdb,profile)
define checkdb
	print "**********"checking db "$$(command jq -r '$1' db.json)""**********"
	sqlplus64 "$$(command jq -r '$1' db.json)" <<<'select * from dual;'
endef

.PHONY: all clean init checkdb-all #checkdb-local checkdb-dev checkdb-test

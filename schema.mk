SHELL:=/usr/bin/zsh
SQLFILES:=asms-upgrade.sql ales-upgrade.sql ads-upgrade.sql tts-upgrade.sql# dgap-upgrade.sql
OUTPUTSQL:=schema-update.sql
#LIQUIBASE_DIFF_OUTPUT:=dev2test.xml test2dev.xml #bj2test.xml test2bj.xml
LIQUIBASE_DIFF_OUTPUT:=bj2test.xml test2bj.xml
SVN_ROOT:=https://192.168.21.251/svn/CodeRepository/GuoJiaZhuiSuPingTai/BusinessSystem

all: $(SQLFILES) $(OUTPUTSQL)

init: 
	jj -p -i schema.json -o schema.json -v "2018-11-01" to_sync_date

db.json: rdp/ds-all.json
	cp $< $@

.ONESHELL:
%-upgrade.sql:
	typeset -A prjs=(ads sofn-ads-service asms sofn-asms-service ales sofn-ales-service tts sofn-tts-service-branch)
	prj=$${prjs[$*]}
	files=($$(comm -23 =(svn ls $(SVN_ROOT)/sofn-server/$$prj/src/main/resources/sql | sort) =(svn ls $(SVN_ROOT)/sofn-server/$$prj/src/main/resources/sql@{$$(command jq -r '.to_sync_date' schema.json)} | sort)))
	rm -rf schema-updates/$*
	svn co --depth empty $(SVN_ROOT)/sofn-server/$$prj/src/main/resources/sql schema-updates/$*
	[[ -n $$files ]] && pushd schema-updates/$*; svn update $$files; popd
	[[ -n $$files ]] && for f in $$files; do print -n '\n' >>schema-updates/$*/$$f; done
	[[ -n $$files ]] && eval cat schema-updates/$*/*(.on) >$@
	print -n '\n' >>$@
	jj -p -i schema.json -o schema.json -v $(shell date +%F) sqls.$*.last-fetch-date

schema-update.sql: $(SQLFILES)
	cat $^ >$@
	dos2unix $@

updatedb-dev updatedb-local updatedb-test:

updatedb-%: db.json
	sqlplus64 -S "$$(command jq -r '.$*.yw.dsn' db.json)" <schema-update.sql | ts | tee -a updatedb.log
	jj -p -i schema.json -o schema.json -v $(shell date +%F) dbs.$*.last-sync-date

checkdb-all: checkdb-local checkdb-dev checkdb-test
	@echo checking

checkdb-%: db.json
	@echo checking $*
	$(call checkdb,.$*.yw.dsn)
	$(call checkdb,.$*.pre.dsn)
	$(call checkdb,.$*.dw.dsn)


db-diff: $(LIQUIBASE_DIFF_OUTPUT)

bj2test.xml:
	liquibase --changeLogFile=$@ --classpath="$$(mvn_artifact_classpath -g oracle.ojdbc -a ojdbc:6)" --driver=oracle.jdbc.driver.OracleDriver --url=jdbc:oracle:thin:@10.0.52.1:1521:orcl --username=gjzspt_demo2 --password='Oe123qwe###' diffChangeLog --referenceUrl=jdbc:oracle:thin:@10.0.52.8:1521/orcl --referenceUsername=gjzspt_demo2 --referencePassword="Oe123qwe###"

test2bj.xml:
	liquibase --changeLogFile=$@ --classpath="$$(mvn_artifact_classpath -g oracle.ojdbc -a ojdbc:6)" --driver=oracle.jdbc.driver.OracleDriver --url=jdbc:oracle:thin:@10.0.52.8:1521:orcl --username=gjzspt_demo2 --password='Oe123qwe###' diffChangeLog --referenceUrl=jdbc:oracle:thin:@10.0.52.1:1521/orcl --referenceUsername=gjzspt_demo2 --referencePassword="Oe123qwe###"

dev2test.xml:
	liquibase --changeLogFile=$@ --classpath="$$(mvn_artifact_classpath -g oracle.ojdbc -a ojdbc:6)" --driver=oracle.jdbc.driver.OracleDriver --url=jdbc:oracle:thin:@192.168.21.249:1521:gjzs --username=gjzspt --password='12345678' diffChangeLog --referenceUrl=jdbc:oracle:thin:@10.0.52.8:1521/orcl --referenceUsername=gjzspt_demo2 --referencePassword="Oe123qwe###"

test2dev.xml:
	liquibase --changeLogFile=$@ --classpath="$$(mvn_artifact_classpath -g oracle.ojdbc -a ojdbc:6)" --driver=oracle.jdbc.driver.OracleDriver --url=jdbc:oracle:thin:@10.0.52.8:1521:orcl --username=gjzspt_demo2 --password='Oe123qwe###' diffChangeLog --referenceUrl=jdbc:oracle:thin:@192.168.21.249:1521/gjzs --referenceUsername=gjzspt --referencePassword="12345678"

clean:
	rm $(SQLFILES)
	rm schema-update.sql
	rm -rf schema-updates

clean-diff:
	rm $(LIQUIBASE_DIFF_OUTPUT)

#$(call checkdb,profile)
define checkdb
	print "**********"checking db "$$(command jq -r '$1' db.json)""**********"
	sqlplus64 -S "$$(command jq -r '$1' db.json)" <<<'select * from dual;'
endef

.PHONY: all clean init checkdb-all #checkdb-local checkdb-dev checkdb-test

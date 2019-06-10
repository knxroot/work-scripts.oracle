SHELL:=/usr/bin/zsh
SQLFILES:=asms-upgrade.sql ales-upgrade.sql ads-upgrade.sql tts-upgrade.sql# dgap-upgrade.sql
OUTPUTSQL:=schema-update.sql
LIQUIBASE_DIFF_OUTPUT:=dev2test.xml test2dev.xml bj2test.xml test2bj.xml bjt2test.xml test2bjt.xml
DIFF_REPORT:=dev2test.txt test2dev.txt bj2test.txt test2bj.txt bjt2test.txt test2bjt.txt
#LIQUIBASE_DIFF_OUTPUT:=bj2test.xml test2bj.xml
SVN_ROOT:=https://192.168.21.251/svn/CodeRepository/GuoJiaZhuiSuPingTai/BusinessSystem

.PHONY: all
all: $(SQLFILES) $(OUTPUTSQL)

.PHONY: all
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


.PHONY: db-diff
db-diff: $(LIQUIBASE_DIFF_OUTPUT)

bj2test.xml:
	liquibase --changeLogFile=$@ --classpath="$$(mvn_artifact_classpath -g oracle.ojdbc -a ojdbc:6)" --driver=oracle.jdbc.driver.OracleDriver --url=jdbc:oracle:thin:@10.0.52.1:1521:orcl --username=gjzspt_demo2 --password='Oe123qwe###' diffChangeLog --referenceUrl=jdbc:oracle:thin:@10.0.52.7:1521/orcl --referenceUsername=gjzspt_demo2 --referencePassword="12345678"
	sed -i -re 's/version="1\.1"/version="1.0"/g' $@

test2bj.xml:
	liquibase --changeLogFile=$@ --classpath="$$(mvn_artifact_classpath -g oracle.ojdbc -a ojdbc:6)" --driver=oracle.jdbc.driver.OracleDriver --url=jdbc:oracle:thin:@10.0.52.7:1521:orcl --username=gjzspt_demo2 --password='12345678' diffChangeLog --referenceUrl=jdbc:oracle:thin:@10.0.52.1:1521/orcl --referenceUsername=gjzspt_demo2 --referencePassword="Oe123qwe###"
	sed -i -re 's/version="1\.1"/version="1.0"/g' $@

bjt2test.xml:
	liquibase --changeLogFile=$@ --classpath="$$(mvn_artifact_classpath -g oracle.ojdbc -a ojdbc:6)" --driver=oracle.jdbc.driver.OracleDriver --url=jdbc:oracle:thin:@10.0.52.1:1521:orcl --username=gjzspt_demo2_test --password='12345678' diffChangeLog --referenceUrl=jdbc:oracle:thin:@10.0.52.7:1521/orcl --referenceUsername=gjzspt_demo2 --referencePassword="12345678"
	sed -i -re 's/version="1\.1"/version="1.0"/g' $@

test2bjt.xml:
	liquibase --changeLogFile=$@ --classpath="$$(mvn_artifact_classpath -g oracle.ojdbc -a ojdbc:6)" --driver=oracle.jdbc.driver.OracleDriver --url=jdbc:oracle:thin:@10.0.52.7:1521:orcl --username=gjzspt_demo2 --password='12345678' diffChangeLog --referenceUrl=jdbc:oracle:thin:@10.0.52.1:1521/orcl --referenceUsername=gjzspt_demo2_test --referencePassword="12345678"
	sed -i -re 's/version="1\.1"/version="1.0"/g' $@

dev2test.xml:
	liquibase --changeLogFile=$@ --classpath="$$(mvn_artifact_classpath -g oracle.ojdbc -a ojdbc:6)" --driver=oracle.jdbc.driver.OracleDriver --url=jdbc:oracle:thin:@192.168.21.249:1521:gjzs --username=gjzspt --password='12345678' diffChangeLog --referenceUrl=jdbc:oracle:thin:@10.0.52.7:1521/orcl --referenceUsername=gjzspt_demo2 --referencePassword="12345678"
	sed -i -re 's/version="1\.1"/version="1.0"/g' $@

test2dev.xml:
	liquibase --changeLogFile=$@ --classpath="$$(mvn_artifact_classpath -g oracle.ojdbc -a ojdbc:6)" --driver=oracle.jdbc.driver.OracleDriver --url=jdbc:oracle:thin:@10.0.52.7:1521:orcl --username=gjzspt_demo2 --password='12345678' diffChangeLog --referenceUrl=jdbc:oracle:thin:@192.168.21.249:1521/gjzs --referenceUsername=gjzspt --referencePassword="12345678"
	sed -i -re 's/version="1\.1"/version="1.0"/g' $@

.PHONY: diff-report
diff-report: $(DIFF_REPORT)

%.txt: %.xml
	print '{{{create table' >>$@
	-xmlstarlet sel -t -m /_:databaseChangeLog/_:changeSet/_:createTable -v '@tableName' -n -m _:column -v '@name' -o ':' -v '@type' -n -b -n $< >>$@
	print '}}}' >>$@
	print '{{{drop table' >>$@
	-xmlstarlet sel -t -m /_:databaseChangeLog/_:changeSet/_:dropTable -v '@tableName' -n -n $< >>$@
	print '}}}' >>$@
	print '{{{add column' >>$@
	-xmlstarlet sel -t -m /_:databaseChangeLog/_:changeSet/_:addColumn -v '@tableName' -n -m _:column -v '@name' -o ':' -v '@type' -o ' ' -b -n -n $< >>$@
	print '}}}' >>$@
	print '{{{drop column' >>$@
	-xmlstarlet sel -t -m /_:databaseChangeLog/_:changeSet/_:dropColumn -v '@tableName' -o ' ' -v '@columnName' -n -n $< >>$@
	print '}}}' >>$@
	print '{{{add notnull constraint' >>$@
	-xmlstarlet sel -t -m /_:databaseChangeLog/_:changeSet/_:addNotNullConstraint -v '@tableName' -o ' ' -v '@columnName' -o ':' -v '@columnDataType' -n -n $< >>$@
	print '}}}' >>$@
	print '{{{drop notnull constraint' >>$@
	-xmlstarlet sel -t -m /_:databaseChangeLog/_:changeSet/_:dropNotNullConstraint -v '@tableName' -o ' ' -v '@columnName' -o ':' -v '@columnDataType' -n -n $< >>$@
	print '}}}' >>$@
	print '{{{modify datatype' >>$@
	-xmlstarlet sel -t -m /_:databaseChangeLog/_:changeSet/_:modifyDataType -v '@tableName' -o ' ' -v '@columnName' -o ' ' -v '@newDataType' -n -n $< >>$@
	print '}}}' >>$@

.PHONY: clean
clean:
	rm $(SQLFILES)
	rm schema-update.sql
	rm -rf schema-updates

.PHONY: clean-diff
clean-diff:
	-rm $(LIQUIBASE_DIFF_OUTPUT)

.PHONY: clean-report
clean-report: clean-diff
	-rm $(DIFF_REPORT)

#$(call checkdb,profile)
define checkdb
	print "**********"checking db "$$(command jq -r '$1' db.json)""**********"
	sqlplus64 -S "$$(command jq -r '$1' db.json)" <<<'select * from dual;'
endef

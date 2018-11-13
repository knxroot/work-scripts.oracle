SQLFILES:=asms.sql
OUTPUTSQL:=schema-update.sql
SVN_ROOT:=https://192.168.21.251/svn/CodeRepository/GuoJiaZhuiSuPingTai/BusinessSystem

all: $(SQLFILES) $(OUTPUTSQL)

init:
	jo -p local="$$(jo -p url="gjzspt_demo2/Oe123qwe###@10.0.52.1:1521/orcl")" dev="$$(jo -p url="gjzspt/12345678@192.168.21.249:1521/gjzs")" test="$$(jo url="gjzspt_demo2/Oe123qwe###@10.0.52.8:1521/orcl")" >db.json

asms.sql:
	svn cat $(SVN_ROOT)/sofn-server/sofn-asms-service/src/main/resources/sql/asms-upgrade-2018-11-12.sql >$@

dgap.sql:
	svn cat $(SVN_ROOT)/sofn-server/sofn-dgap-service/src/main/resources/sql/dgap-upgrade.sql >$@

schema-update.sql: bjdbclean/bj7/tts.sql bjdbclean/bj7/ads-upgrade-2018-11-12.sql bjdbclean/bj7/ales.sql bjdbclean/bj7/asms-upgrade-2018-11-12.sql
	#cat $(SQLFILES) >$@
	cat $^ >$@
	dos2unix $@

updatedb-dev updatedb-local updatedb-test:

updatedb-%:
	sqlplus64 "$$(command jq -r '.$*.url' db.json)" <schema-update.sql | ts | tee -a updatedb.log
	jj -p -i schema.json -o schema.json -v $(shell date +%FT%T) $*.last-sync-date

clean:
	rm $(SQLFILES)

.PHONY: all clean init
SHELL:=/usr/bin/zsh

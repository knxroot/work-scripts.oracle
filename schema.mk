SQLFILES:=asms.sql
OUTPUTSQL:=schema-update.sql

all: $(SQLFILES) $(OUTPUTSQL)

init:
	jo -p local= dev="$$(jo -p url="gjzspt/12345678@192.168.21.249:1521/gjzs")" test="$$(jo url="gjzspt_demo2/Oe123qwe###@10.0.52.8:1521/orcl")" >db.json

asms.sql:
	svn cat https://192.168.21.251/svn/CodeRepository/GuoJiaZhuiSuPingTai/BusinessSystem/sofn-server/sofn-asms-service/src/main/resources/sql/asms-upgrade-2018-11-12.sql >$@

dgap.sql:
	svn cat https://192.168.21.251/svn/CodeRepository/GuoJiaZhuiSuPingTai/BusinessSystem/sofn-server/sofn-dgap-service/src/main/resources/sql/dgap-upgrade.sql >$@

schema-update.sql: $(SQLFILES)
	cat $(SQLFILES) >$@

updatedb-%:
	sqlplus64 "$$(command jq -r '.$*.url' db.json)" <schema-update.sql

clean:
	rm $(SQLFILES)

sync:
	jj -p -i schema.json -o schema.json -v $(shell date +%FT%T) last-sync-date

.PHONY: all clean init
SHELL:=/usr/bin/zsh

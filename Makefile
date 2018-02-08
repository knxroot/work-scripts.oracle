.INTERMEDIATE: export.sql
.PHONY: import newdb kill-sessions

user_name:=gjzspt_bj_165
db_name:=GJZSPT_BJ_165

all: import

import: fixed.sql
	@echo importing
	echo "\nquit" >> $<
	NLS_LANG="SIMPLIFIED CHINESE_CHINA.UTF8" sqlplus64 "$(user_name)/12345678@10.0.52.1/orcl" @./$<

newdb:
	./create_schema.sh $(user_name)

kill-sessions:
	./query_session.sh $(db_name) | xargs -i ./kill_session.sh "'{}'"

fixed.sql: export.sql
	@echo fixing sql
	sed 's/"GJZSPT"\./"$(db_name)"./g' $< >$@
	sed 's/GJZSPT\./$(db_name)./g' $@ | sponge $@

export.sql:
	mkdir -p sqls; mv $@ sqls/backup_$(shell date +%F_%T).sql
	cp /home/helong/TencentFiles/2898132719/FileRecv/export.sql $@

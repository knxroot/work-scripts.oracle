.INTERMEDIATE: export.sql
.PHONY: import newdb kill-sessions

USER_NAME:=gjzspt_bj_165
DB_NAME:=GJZSPT_BJ_165

import: fixed.sql
	@echo importing
	echo "\nquit" >> $<
	NLS_LANG="SIMPLIFIED CHINESE_CHINA.UTF8" sqlplus64 "$(USER_NAME)/12345678@10.0.52.1/orcl" @./$<

newdb:
	./create_schema.sh $(USER_NAME)

kill-sessions:
	./query_session.sh $(DB_NAME) | xargs -i ./kill_session.sh "'{}'"

fixed.sql: export.sql
	@echo fixing sql
	sed 's/"GJZSPT"\./"$(DB_NAME)"./g' $< >$@
	sed 's/GJZSPT\./$(DB_NAME)./g' $@ | sponge $@

export.sql:
	-test -f $@ && { mkdir -p sqls; mv $@ sqls/backup_$(shell date +%F_%T).sql;}
	cp /home/helong/TencentFiles/2898132719/FileRecv/export.sql $@

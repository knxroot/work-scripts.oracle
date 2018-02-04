all: import

import: fix-sql
	@echo importing

fix-sql: export.sql
	@echo fixing sql
	sed -i.bak 's/"GJZSPT"\./"GJZSPT_DEMO2"./g' $<
	sed -i.bak 's/GJZSPT\./GJZSPT_DEMO2./g' $<

export.sql:
	mv /home/helong/TencentFiles/2898132719/FileRecv/export.sql $@

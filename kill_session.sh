db_name=${1:?"Please specify db_name"}

NLS_LANG="SIMPLIFIED CHINESE_CHINA.UTF8" sqlplus64 "sys/Oe123qwe###@10.0.52.1/orcl as sysdba" <<EOI
alter system kill session $db_name;
quit
EOI

db_name=${1:?Please specify db_name}

NLS_LANG="SIMPLIFIED CHINESE_CHINA.UTF8" sqlplus64 "sys/Oe123qwe###@10.0.52.1/orcl as sysdba" <<EOI
drop user $db_name cascade;
create user $db_name identified by 12345678;
grant connect to $db_name;
grant resource to $db_name;
grant create view to $db_name;
quit
EOI

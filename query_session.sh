user_name=${1:?You must specify db username}
NLS_LANG="SIMPLIFIED CHINESE_CHINA.UTF8" sqlplus64 "sys/Oe123qwe###@10.0.52.1/orcl as sysdba" <<EOI | egrep '[[:digit:]]+,[[:digit:]]+'
select sid || ',' || serial# from v\$session where USERNAME='$user_name';
quit
EOI

CREATE USER gjzspt IDENTIFIED BY 12345678;
GRANT CONNECT TO gjzspt;
GRANT RESOURCE TO gjzspt;

drop user gjzspt;

REVOKE RESOURCE FROM gjzspt;

CREATE ROLE dbop_user;
GRANT CONNECT TO dbop_user;
GRANT RESOURCE TO dbop_user;

CREATE USER dbops IDENTIFIED BY "1234qwer";
GRANT CONNECT TO dbops;
GRANT RESOURCE TO dbops;
GRANT DBA TO dbops;

DROP USER dbops;

ALTER USER gjzspt ACCOUNT UNLOCK

---
select * from user_sys_privs where username = 'gjzspt';

select * from all_sys_privs where username = 'gjzspt';

SELECT * FROM DBA_SYS_PRIVS WHERE GRANTEE='RESOURCE' OR GRANTEE='CONNECT' or grantee='gjzspt';

select * from dba_tab_privs WHERE grantee = 'gjzspt';
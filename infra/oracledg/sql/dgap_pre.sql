CREATE USER dgap_pre IDENTIFIED BY 12345678;
GRANT CONNECT TO dgap_pre;
GRANT RESOURCE TO dgap_pre;

DROP USER dgap_pre;

ALTER USER dgap_pre ACCOUNT UNLOCK

---
select * from xxxxx;
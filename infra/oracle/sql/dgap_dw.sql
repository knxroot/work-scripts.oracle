CREATE USER dgap_dw IDENTIFIED BY 12345678;;
GRANT CONNECT TO dgap_dw;
GRANT RESOURCE TO dgap_dw;

DROP USER dgap_dw;

ALTER USER dgap_dw ACCOUNT UNLOCK

---
select * from xxxxx;
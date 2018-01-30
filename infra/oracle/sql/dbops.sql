ALTER SESSION SET CURRENT_SCHEMA = gjzspt;

select 'drop table ' || table_name || ';' from user_tables where table_name like '%';

create table T_SUPERVISE_BASEINSPECTION 
(
   ID                   CHAR(32)             not null,
   ENTERPRISEID         CHAR(32),
   INSPECTION_RESULT    VARCHAR2(20),
   INSPECTION_VIEW      VARCHAR2(200),
   INSPECTION_IMAGES    VARCHAR2(2000),
   INSPECTION_TIME      DATE,
   INSPECTION_SUPERVISEID VARCHAR2(32),
   ENFORCELAWCHECK_STATE CHAR(2),
   INSPECTION_USERID    CHAR(32),
   constraint PK_T_SUPERVISE_BASEINSPECTION primary key (ID)
);

create table T_SUPERVISE_INSPECTIONTASK 
(
   ID                   CHAR(32)             not null,
   TASK_TYPE            VARCHAR2(100),
   TASK_YEAR            VARCHAR2(100),
   TASK_QUARTER         VARCHAR2(100),
   TASK_MONTH           VARCHAR2(100),
   INSPECTION_AREAID    VARCHAR2(100),
   INSPECTION_COUNT     NUMBER(10),
   TASK_RESULT               VARCHAR2(100),
   INSPECTION_REALCOUNT NUMBER(10),
   constraint PK_T_SUPERVISE_INSPECTIONTASK primary key (ID)
);

create table T_SUPERVISE_TASKUSER 
(
   TASK_ID              CHAR(32),
   USER_ID              CHAR(32)
);

create table T_SUBJECT_SUPERVISE 
(
   ID                   CHAR(32)             not null,
   NAME                 VARCHAR2(200)        not null,
   CODE                 VARCHAR2(50)         not null,
   SUPERVISE_LEVEL      VARCHAR2(20)         not null,
   AREAID               VARCHAR2(32)         not null,
   ADDRESS              VARCHAR2(200)        not null,
   LEADER               VARCHAR2(100)        not null,
   LEADERPHONE          VARCHAR2(20),
   CONTACT              VARCHAR2(100)        not null,
   CONTACTPHONE         VARCHAR2(20)         not null,
   CONTACTQQ            VARCHAR2(20),
   CONTACTMAIL          VARCHAR2(50),
   POSTCODE             CHAR(6),
   CREATETIME           DATE,
   REVOKETYPE           CHAR(2),
   constraint PK_T_SUBJECT_SUPERVISE primary key (ID)
);
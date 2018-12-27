---更新监管机构帐号［JG-410000-001］对应监管机构的行业［渔业］
UPDATE "ASMS_SUBJ_SUPERVISE"
SET "INDUSTRY_ID" = INDUSTRY_ID
|| ','
||
(SELECT id FROM sys_dict_data WHERE dict_name IN ('渔业')
),
"INDUSTRY_NAME" = INDUSTRY_NAME
|| ','
||
(SELECT dict_name FROM sys_dict_data WHERE dict_name IN ('渔业')
),
"INDUSTRY_VALUE" = INDUSTRY_VALUE
|| ','
||
(SELECT dict_value FROM sys_dict_data WHERE dict_name IN ('渔业')
)
WHERE "ID" =
(SELECT ss.id
FROM ASMS_SUBJ_SUPERVISE ss,
    SYS_ORGANIZATION o,
    SYS_USER u
WHERE ss.id           =o.org_id
AND u.ORGANIZATION_ID = o.id
AND u.account         ='JG-410000-001'
);
---增加监管机构帐号［JG-410000-001］的角色［监管机构管理员渔业角色］
INSERT INTO "SYS_USER_ROLE"
(
    "ID",
    "USER_ID",
    "ROLE_ID",
    "CREATE_BY",
    "CREATE_TIME",
    "UPDATE_BY",
    "UPDATE_TIME",
    "DEL_FLAG"
)
VALUES
(
    '74746752d4e499a6faa67b6188b1d3748b462ee4bb8a8dd62726dc3fbcfba631',
    (select id from sys_user where account='JG-410000-001'),
    (select id from sys_role where role_name = '监管机构管理员渔业角色'),
    NULL,
    sysdate,
    NULL,
    sysdate,
    'N'
);            
---更新监管机构帐号［JG-320000-002］对应监管机构的行业［畜牧业］
UPDATE "ASMS_SUBJ_SUPERVISE"
SET "INDUSTRY_ID" = INDUSTRY_ID
|| ','
||
(SELECT id FROM sys_dict_data WHERE dict_name IN ('畜牧业')
),
"INDUSTRY_NAME" = INDUSTRY_NAME
|| ','
||
(SELECT dict_name FROM sys_dict_data WHERE dict_name IN ('畜牧业')
),
"INDUSTRY_VALUE" = INDUSTRY_VALUE
|| ','
||
(SELECT dict_value FROM sys_dict_data WHERE dict_name IN ('畜牧业')
)
WHERE "ID" =
(SELECT ss.id
FROM ASMS_SUBJ_SUPERVISE ss,
    SYS_ORGANIZATION o,
    SYS_USER u
WHERE ss.id           =o.org_id
AND u.ORGANIZATION_ID = o.id
AND u.account         ='JG-320000-002'
);
---增加监管机构帐号［JG-320000-002］的角色［监管机构管理员畜牧业角色］
INSERT INTO "SYS_USER_ROLE"
(
    "ID",
    "USER_ID",
    "ROLE_ID",
    "CREATE_BY",
    "CREATE_TIME",
    "UPDATE_BY",
    "UPDATE_TIME",
    "DEL_FLAG"
)
VALUES
(
    '0ae1413e1d55a614325c9fc2adf1a12b86652f40716c37cccd32603f0e2a2a0f',
    (select id from sys_user where account='JG-320000-002'),
    (select id from sys_role where role_name = '监管机构管理员畜牧业角色'),
    NULL,
    sysdate,
    NULL,
    sysdate,
    'N'
);            
---更新监管机构帐号［JG-440100-007］对应监管机构的行业［渔业］
UPDATE "ASMS_SUBJ_SUPERVISE"
SET "INDUSTRY_ID" = INDUSTRY_ID
|| ','
||
(SELECT id FROM sys_dict_data WHERE dict_name IN ('渔业')
),
"INDUSTRY_NAME" = INDUSTRY_NAME
|| ','
||
(SELECT dict_name FROM sys_dict_data WHERE dict_name IN ('渔业')
),
"INDUSTRY_VALUE" = INDUSTRY_VALUE
|| ','
||
(SELECT dict_value FROM sys_dict_data WHERE dict_name IN ('渔业')
)
WHERE "ID" =
(SELECT ss.id
FROM ASMS_SUBJ_SUPERVISE ss,
    SYS_ORGANIZATION o,
    SYS_USER u
WHERE ss.id           =o.org_id
AND u.ORGANIZATION_ID = o.id
AND u.account         ='JG-440100-007'
);
---增加监管机构帐号［JG-440100-007］的角色［监管机构管理员渔业角色］
INSERT INTO "SYS_USER_ROLE"
(
    "ID",
    "USER_ID",
    "ROLE_ID",
    "CREATE_BY",
    "CREATE_TIME",
    "UPDATE_BY",
    "UPDATE_TIME",
    "DEL_FLAG"
)
VALUES
(
    '00a379c22b6529ed009c9ad2169d93638b462ee4bb8a8dd62726dc3fbcfba631',
    (select id from sys_user where account='JG-440100-007'),
    (select id from sys_role where role_name = '监管机构管理员渔业角色'),
    NULL,
    sysdate,
    NULL,
    sysdate,
    'N'
);            
---更新监管机构帐号［JG-440704-001］对应监管机构的行业［渔业］
UPDATE "ASMS_SUBJ_SUPERVISE"
SET "INDUSTRY_ID" = INDUSTRY_ID
|| ','
||
(SELECT id FROM sys_dict_data WHERE dict_name IN ('渔业')
),
"INDUSTRY_NAME" = INDUSTRY_NAME
|| ','
||
(SELECT dict_name FROM sys_dict_data WHERE dict_name IN ('渔业')
),
"INDUSTRY_VALUE" = INDUSTRY_VALUE
|| ','
||
(SELECT dict_value FROM sys_dict_data WHERE dict_name IN ('渔业')
)
WHERE "ID" =
(SELECT ss.id
FROM ASMS_SUBJ_SUPERVISE ss,
    SYS_ORGANIZATION o,
    SYS_USER u
WHERE ss.id           =o.org_id
AND u.ORGANIZATION_ID = o.id
AND u.account         ='JG-440704-001'
);
---增加监管机构帐号［JG-440704-001］的角色［监管机构管理员渔业角色］
INSERT INTO "SYS_USER_ROLE"
(
    "ID",
    "USER_ID",
    "ROLE_ID",
    "CREATE_BY",
    "CREATE_TIME",
    "UPDATE_BY",
    "UPDATE_TIME",
    "DEL_FLAG"
)
VALUES
(
    '60cd961f48f7863fec9d94b637c874a58b462ee4bb8a8dd62726dc3fbcfba631',
    (select id from sys_user where account='JG-440704-001'),
    (select id from sys_role where role_name = '监管机构管理员渔业角色'),
    NULL,
    sysdate,
    NULL,
    sysdate,
    'N'
);            
---更新监管机构帐号［JG-440783-001］对应监管机构的行业［渔业］
UPDATE "ASMS_SUBJ_SUPERVISE"
SET "INDUSTRY_ID" = INDUSTRY_ID
|| ','
||
(SELECT id FROM sys_dict_data WHERE dict_name IN ('渔业')
),
"INDUSTRY_NAME" = INDUSTRY_NAME
|| ','
||
(SELECT dict_name FROM sys_dict_data WHERE dict_name IN ('渔业')
),
"INDUSTRY_VALUE" = INDUSTRY_VALUE
|| ','
||
(SELECT dict_value FROM sys_dict_data WHERE dict_name IN ('渔业')
)
WHERE "ID" =
(SELECT ss.id
FROM ASMS_SUBJ_SUPERVISE ss,
    SYS_ORGANIZATION o,
    SYS_USER u
WHERE ss.id           =o.org_id
AND u.ORGANIZATION_ID = o.id
AND u.account         ='JG-440783-001'
);
---增加监管机构帐号［JG-440783-001］的角色［监管机构管理员渔业角色］
INSERT INTO "SYS_USER_ROLE"
(
    "ID",
    "USER_ID",
    "ROLE_ID",
    "CREATE_BY",
    "CREATE_TIME",
    "UPDATE_BY",
    "UPDATE_TIME",
    "DEL_FLAG"
)
VALUES
(
    '8d0f4e9c829ea0fe79a092af7d93de638b462ee4bb8a8dd62726dc3fbcfba631',
    (select id from sys_user where account='JG-440783-001'),
    (select id from sys_role where role_name = '监管机构管理员渔业角色'),
    NULL,
    sysdate,
    NULL,
    sysdate,
    'N'
);            
---更新监管机构帐号［JG-440785-002］对应监管机构的行业［渔业］
UPDATE "ASMS_SUBJ_SUPERVISE"
SET "INDUSTRY_ID" = INDUSTRY_ID
|| ','
||
(SELECT id FROM sys_dict_data WHERE dict_name IN ('渔业')
),
"INDUSTRY_NAME" = INDUSTRY_NAME
|| ','
||
(SELECT dict_name FROM sys_dict_data WHERE dict_name IN ('渔业')
),
"INDUSTRY_VALUE" = INDUSTRY_VALUE
|| ','
||
(SELECT dict_value FROM sys_dict_data WHERE dict_name IN ('渔业')
)
WHERE "ID" =
(SELECT ss.id
FROM ASMS_SUBJ_SUPERVISE ss,
    SYS_ORGANIZATION o,
    SYS_USER u
WHERE ss.id           =o.org_id
AND u.ORGANIZATION_ID = o.id
AND u.account         ='JG-440785-002'
);
---增加监管机构帐号［JG-440785-002］的角色［监管机构管理员渔业角色］
INSERT INTO "SYS_USER_ROLE"
(
    "ID",
    "USER_ID",
    "ROLE_ID",
    "CREATE_BY",
    "CREATE_TIME",
    "UPDATE_BY",
    "UPDATE_TIME",
    "DEL_FLAG"
)
VALUES
(
    '93c3a1b74f99d999e7162bdc918f35a58b462ee4bb8a8dd62726dc3fbcfba631',
    (select id from sys_user where account='JG-440785-002'),
    (select id from sys_role where role_name = '监管机构管理员渔业角色'),
    NULL,
    sysdate,
    NULL,
    sysdate,
    'N'
);            
---更新监管机构帐号［JG-441400-001］对应监管机构的行业［渔业］
UPDATE "ASMS_SUBJ_SUPERVISE"
SET "INDUSTRY_ID" = INDUSTRY_ID
|| ','
||
(SELECT id FROM sys_dict_data WHERE dict_name IN ('渔业')
),
"INDUSTRY_NAME" = INDUSTRY_NAME
|| ','
||
(SELECT dict_name FROM sys_dict_data WHERE dict_name IN ('渔业')
),
"INDUSTRY_VALUE" = INDUSTRY_VALUE
|| ','
||
(SELECT dict_value FROM sys_dict_data WHERE dict_name IN ('渔业')
)
WHERE "ID" =
(SELECT ss.id
FROM ASMS_SUBJ_SUPERVISE ss,
    SYS_ORGANIZATION o,
    SYS_USER u
WHERE ss.id           =o.org_id
AND u.ORGANIZATION_ID = o.id
AND u.account         ='JG-441400-001'
);
---增加监管机构帐号［JG-441400-001］的角色［监管机构管理员渔业角色］
INSERT INTO "SYS_USER_ROLE"
(
    "ID",
    "USER_ID",
    "ROLE_ID",
    "CREATE_BY",
    "CREATE_TIME",
    "UPDATE_BY",
    "UPDATE_TIME",
    "DEL_FLAG"
)
VALUES
(
    '92831f53e00929c8859654ab579097a88b462ee4bb8a8dd62726dc3fbcfba631',
    (select id from sys_user where account='JG-441400-001'),
    (select id from sys_role where role_name = '监管机构管理员渔业角色'),
    NULL,
    sysdate,
    NULL,
    sysdate,
    'N'
);            
---更新监管机构帐号［JG-440704-001］对应监管机构的行业［畜牧业］
UPDATE "ASMS_SUBJ_SUPERVISE"
SET "INDUSTRY_ID" = INDUSTRY_ID
|| ','
||
(SELECT id FROM sys_dict_data WHERE dict_name IN ('畜牧业')
),
"INDUSTRY_NAME" = INDUSTRY_NAME
|| ','
||
(SELECT dict_name FROM sys_dict_data WHERE dict_name IN ('畜牧业')
),
"INDUSTRY_VALUE" = INDUSTRY_VALUE
|| ','
||
(SELECT dict_value FROM sys_dict_data WHERE dict_name IN ('畜牧业')
)
WHERE "ID" =
(SELECT ss.id
FROM ASMS_SUBJ_SUPERVISE ss,
    SYS_ORGANIZATION o,
    SYS_USER u
WHERE ss.id           =o.org_id
AND u.ORGANIZATION_ID = o.id
AND u.account         ='JG-440704-001'
);
---增加监管机构帐号［JG-440704-001］的角色［监管机构管理员畜牧业角色］
INSERT INTO "SYS_USER_ROLE"
(
    "ID",
    "USER_ID",
    "ROLE_ID",
    "CREATE_BY",
    "CREATE_TIME",
    "UPDATE_BY",
    "UPDATE_TIME",
    "DEL_FLAG"
)
VALUES
(
    '60cd961f48f7863fec9d94b637c874a586652f40716c37cccd32603f0e2a2a0f',
    (select id from sys_user where account='JG-440704-001'),
    (select id from sys_role where role_name = '监管机构管理员畜牧业角色'),
    NULL,
    sysdate,
    NULL,
    sysdate,
    'N'
);            
---更新监管机构帐号［JG-440705-001］对应监管机构的行业［畜牧业］
UPDATE "ASMS_SUBJ_SUPERVISE"
SET "INDUSTRY_ID" = INDUSTRY_ID
|| ','
||
(SELECT id FROM sys_dict_data WHERE dict_name IN ('畜牧业')
),
"INDUSTRY_NAME" = INDUSTRY_NAME
|| ','
||
(SELECT dict_name FROM sys_dict_data WHERE dict_name IN ('畜牧业')
),
"INDUSTRY_VALUE" = INDUSTRY_VALUE
|| ','
||
(SELECT dict_value FROM sys_dict_data WHERE dict_name IN ('畜牧业')
)
WHERE "ID" =
(SELECT ss.id
FROM ASMS_SUBJ_SUPERVISE ss,
    SYS_ORGANIZATION o,
    SYS_USER u
WHERE ss.id           =o.org_id
AND u.ORGANIZATION_ID = o.id
AND u.account         ='JG-440705-001'
);
---增加监管机构帐号［JG-440705-001］的角色［监管机构管理员畜牧业角色］
INSERT INTO "SYS_USER_ROLE"
(
    "ID",
    "USER_ID",
    "ROLE_ID",
    "CREATE_BY",
    "CREATE_TIME",
    "UPDATE_BY",
    "UPDATE_TIME",
    "DEL_FLAG"
)
VALUES
(
    '601dc37a9f9e370890dd4a98e461bc2a86652f40716c37cccd32603f0e2a2a0f',
    (select id from sys_user where account='JG-440705-001'),
    (select id from sys_role where role_name = '监管机构管理员畜牧业角色'),
    NULL,
    sysdate,
    NULL,
    sysdate,
    'N'
);            
---更新监管机构帐号［JG-440781-001］对应监管机构的行业［畜牧业］
UPDATE "ASMS_SUBJ_SUPERVISE"
SET "INDUSTRY_ID" = INDUSTRY_ID
|| ','
||
(SELECT id FROM sys_dict_data WHERE dict_name IN ('畜牧业')
),
"INDUSTRY_NAME" = INDUSTRY_NAME
|| ','
||
(SELECT dict_name FROM sys_dict_data WHERE dict_name IN ('畜牧业')
),
"INDUSTRY_VALUE" = INDUSTRY_VALUE
|| ','
||
(SELECT dict_value FROM sys_dict_data WHERE dict_name IN ('畜牧业')
)
WHERE "ID" =
(SELECT ss.id
FROM ASMS_SUBJ_SUPERVISE ss,
    SYS_ORGANIZATION o,
    SYS_USER u
WHERE ss.id           =o.org_id
AND u.ORGANIZATION_ID = o.id
AND u.account         ='JG-440781-001'
);
---增加监管机构帐号［JG-440781-001］的角色［监管机构管理员畜牧业角色］
INSERT INTO "SYS_USER_ROLE"
(
    "ID",
    "USER_ID",
    "ROLE_ID",
    "CREATE_BY",
    "CREATE_TIME",
    "UPDATE_BY",
    "UPDATE_TIME",
    "DEL_FLAG"
)
VALUES
(
    'a2e0fcd233482635d067c0e8eac1076286652f40716c37cccd32603f0e2a2a0f',
    (select id from sys_user where account='JG-440781-001'),
    (select id from sys_role where role_name = '监管机构管理员畜牧业角色'),
    NULL,
    sysdate,
    NULL,
    sysdate,
    'N'
);            
---更新监管机构帐号［JG-440783-001］对应监管机构的行业［畜牧业］
UPDATE "ASMS_SUBJ_SUPERVISE"
SET "INDUSTRY_ID" = INDUSTRY_ID
|| ','
||
(SELECT id FROM sys_dict_data WHERE dict_name IN ('畜牧业')
),
"INDUSTRY_NAME" = INDUSTRY_NAME
|| ','
||
(SELECT dict_name FROM sys_dict_data WHERE dict_name IN ('畜牧业')
),
"INDUSTRY_VALUE" = INDUSTRY_VALUE
|| ','
||
(SELECT dict_value FROM sys_dict_data WHERE dict_name IN ('畜牧业')
)
WHERE "ID" =
(SELECT ss.id
FROM ASMS_SUBJ_SUPERVISE ss,
    SYS_ORGANIZATION o,
    SYS_USER u
WHERE ss.id           =o.org_id
AND u.ORGANIZATION_ID = o.id
AND u.account         ='JG-440783-001'
);
---增加监管机构帐号［JG-440783-001］的角色［监管机构管理员畜牧业角色］
INSERT INTO "SYS_USER_ROLE"
(
    "ID",
    "USER_ID",
    "ROLE_ID",
    "CREATE_BY",
    "CREATE_TIME",
    "UPDATE_BY",
    "UPDATE_TIME",
    "DEL_FLAG"
)
VALUES
(
    '8d0f4e9c829ea0fe79a092af7d93de6386652f40716c37cccd32603f0e2a2a0f',
    (select id from sys_user where account='JG-440783-001'),
    (select id from sys_role where role_name = '监管机构管理员畜牧业角色'),
    NULL,
    sysdate,
    NULL,
    sysdate,
    'N'
);            
---更新监管机构帐号［JG-440784-001］对应监管机构的行业［畜牧业］
UPDATE "ASMS_SUBJ_SUPERVISE"
SET "INDUSTRY_ID" = INDUSTRY_ID
|| ','
||
(SELECT id FROM sys_dict_data WHERE dict_name IN ('畜牧业')
),
"INDUSTRY_NAME" = INDUSTRY_NAME
|| ','
||
(SELECT dict_name FROM sys_dict_data WHERE dict_name IN ('畜牧业')
),
"INDUSTRY_VALUE" = INDUSTRY_VALUE
|| ','
||
(SELECT dict_value FROM sys_dict_data WHERE dict_name IN ('畜牧业')
)
WHERE "ID" =
(SELECT ss.id
FROM ASMS_SUBJ_SUPERVISE ss,
    SYS_ORGANIZATION o,
    SYS_USER u
WHERE ss.id           =o.org_id
AND u.ORGANIZATION_ID = o.id
AND u.account         ='JG-440784-001'
);
---增加监管机构帐号［JG-440784-001］的角色［监管机构管理员畜牧业角色］
INSERT INTO "SYS_USER_ROLE"
(
    "ID",
    "USER_ID",
    "ROLE_ID",
    "CREATE_BY",
    "CREATE_TIME",
    "UPDATE_BY",
    "UPDATE_TIME",
    "DEL_FLAG"
)
VALUES
(
    '015bf44b85beb7f7eda5fafc8615f63986652f40716c37cccd32603f0e2a2a0f',
    (select id from sys_user where account='JG-440784-001'),
    (select id from sys_role where role_name = '监管机构管理员畜牧业角色'),
    NULL,
    sysdate,
    NULL,
    sysdate,
    'N'
);            


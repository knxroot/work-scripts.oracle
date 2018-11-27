{
    clean_orphan_users(orgtypes):: {
        sql: |||
            UPDATE SYS_USER 
            SET DEL_FLAG = 'Y' 
            WHERE
                ID IN (
            SELECT
                SYS_USER.ID 
            FROM
                SYS_USER,
                SYS_ORGANIZATION
                LEFT JOIN ASMS_SUBJ_SUPERVISE ON ASMS_SUBJ_SUPERVISE.ID = SYS_ORGANIZATION.ORG_ID 
            WHERE
                ASMS_SUBJ_SUPERVISE.ID IS NULL 
                AND SYS_USER.ORGANIZATION_ID = SYS_ORGANIZATION.ID 
                AND SYS_ORGANIZATION.ORG_TYPE IN (%s)
                );
        ||| % ("'" + std.join("','",orgtypes) + "'")
    },

    clean_asms_dirty_account(sv_names):: {
        in_expr :: "'" + std.join("','",sv_names) + "'",
        sql: |||
            -- 系统用户角色对应关系表:
            DELETE
            FROM SYS_USER_ROLE
            WHERE ID IN
            (SELECT ID
            FROM SYS_USER_ROLE
            WHERE USER_ID IN
                (SELECT ID
                FROM SYS_USER
                WHERE ORGANIZATION_ID IN
                (SELECT ID
                FROM SYS_ORGANIZATION
                WHERE ORG_ID IN
                    (SELECT ID FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN (%(in_expr)s)
                    )
                )
                )
            );
            -- 系统用户表:
            DELETE
            FROM SYS_USER
            WHERE ID IN
            (SELECT ID
            FROM SYS_USER
            WHERE ORGANIZATION_ID IN
                (SELECT ID
                FROM SYS_ORGANIZATION
                WHERE ORG_ID IN
                (SELECT ID FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN (%(in_expr)s)
                )
                )
            );
            -- 系统组织机构与机构信息关系表:
            DELETE
            FROM SYS_ORGANIZATION
            WHERE ID IN
            (SELECT ID
            FROM SYS_ORGANIZATION
            WHERE ORG_ID IN
                (SELECT ID FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN (%(in_expr)s)
                )
            );
            -- 监管机构主体表:
            DELETE
            FROM ASMS_SUBJ_SUPERVISE
            WHERE ID IN
            (SELECT ID FROM ASMS_SUBJ_SUPERVISE S WHERE S.SV_NAME IN (%(in_expr)s)
            );
        ||| % self
    },
}

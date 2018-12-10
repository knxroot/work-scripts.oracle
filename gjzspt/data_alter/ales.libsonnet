{
    delete_all_data_by_userids(user_ids):: {
        in_expr :: "'" + std.join("','",user_ids) + "'",
        sql: |||
            --- 删除-现场巡查-脏数据
            DELETE FROM ALES_DAILY_ENFORCE_LAW WHERE CREATE_BY IN
            (
            SELECT
                P.CREATE_BY
            FROM
                ALES_DAILY_ENFORCE_LAW P
            LEFT JOIN SYS_USER H ON P.CREATE_BY = H.ID 
            LEFT JOIN SYS_ORGANIZATION T ON H .ORGANIZATION_ID = T.ID
            LEFT JOIN ASMS_SUBJ_ENFORCE_LAW M ON T.ORG_ID = M.ID
            WHERE	 H.ID in (%(in_expr)s));

            --- 删除-委托检测任务 - 脏数据
            DELETE FROM ALES_ENTRUST_DETECTION WHERE CREATE_BY IN
            (
            SELECT
                P.CREATE_BY
            FROM
                ALES_ENTRUST_DETECTION P
            LEFT JOIN SYS_USER H ON P.CREATE_BY = H.ID 
            LEFT JOIN SYS_ORGANIZATION T ON H .ORGANIZATION_ID = T.ID
            LEFT JOIN ASMS_SUBJ_ENFORCE_LAW M ON T.ORG_ID = M.ID
            WHERE H.ID in (%(in_expr)s));

            --- 删除-委托检测-检测对象表 -脏数据
            DELETE FROM ALES_ENTRUST_DETECTION WHERE CREATE_BY IN
            (
            SELECT
                P.CREATE_BY
            FROM
                ALES_TASK_SAMPLE P
            LEFT JOIN SYS_USER H ON P.CREATE_BY = H.ID 
            LEFT JOIN SYS_ORGANIZATION T ON H .ORGANIZATION_ID = T.ID
            LEFT JOIN ASMS_SUBJ_ENFORCE_LAW M ON T.ORG_ID = M.ID
            WHERE	 H.ID in (%(in_expr)s));

            --- 删除-委托检测任务-检测对象-抽样单-脏数据
            DELETE FROM ALES_TASK_SAMPLE WHERE CREATE_BY IN
            (
            SELECT
                P.CREATE_BY
            FROM
                ALES_TASK_SAMPLE P
            LEFT JOIN SYS_USER H ON P.CREATE_BY = H.ID 
            LEFT JOIN SYS_ORGANIZATION T ON H .ORGANIZATION_ID = T.ID
            LEFT JOIN ASMS_SUBJ_ENFORCE_LAW M ON T.ORG_ID = M.ID
            WHERE	 H.ID in (%(in_expr)s));

            --- 删除-行政处罚-脏数据
            DELETE FROM ALES_TASK_SAMPLE WHERE CREATE_BY IN
            (
            SELECT
                P.CREATE_BY
            FROM
                ALES_PRODUCE_ADMIN_PUNISH P
            LEFT JOIN SYS_USER H ON P.CREATE_BY = H.ID 
            LEFT JOIN SYS_ORGANIZATION T ON H .ORGANIZATION_ID = T.ID
            LEFT JOIN ASMS_SUBJ_ENFORCE_LAW M ON T.ORG_ID = M.ID
            WHERE	 H.ID in (%(in_expr)s));

            --删除系统用户表 数据
            DELETE
            FROM
                SYS_USER S
            WHERE
                S.ORGANIZATION_ID IN (
                    SELECT
                        ID
                    FROM
                        SYS_ORGANIZATION
                ) AND  S.ID in (%(in_expr)s);
        ||| % self
    },
}

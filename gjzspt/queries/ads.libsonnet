{
    query_user_by_accounts(accounts):: {
        in_expr :: "'" + std.join("','",accounts) + "'",
        sql: |||
            SELECT
                * 
            FROM
                ASMS_SUBJ_DETECTION t1
                LEFT JOIN SYS_ORGANIZATION t2 ON t1.id = t2.org_id
                LEFT JOIN sys_user t3 ON t2.id = t3.ORGANIZATION_id 
            WHERE
                t1.dt_name in (%(in_expr)s );
        ||| % self,
    },

    query_user_match_account(account):: {
        account:: account,
        sql: |||
            SELECT
                * 
            FROM
                ASMS_SUBJ_DETECTION t1
                LEFT JOIN SYS_ORGANIZATION t2 ON t1.id = t2.org_id
                LEFT JOIN sys_user t3 ON t2.id = t3.ORGANIZATION_id 
            WHERE
                t1.dt_name like '%(account)s' or t3.USER_NAME like '%(account)s' or t2.ORG_NAME like  '%(account)s';        
        ||| % self,
    }
}
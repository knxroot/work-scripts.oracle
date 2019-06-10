local func=import '../func.jsn';

{
    query_user_by_account(account_name):: |||
        select * from sys_user where account like '%s';
    ||| % account_name,

    query_user_roles(accounts):: |||
        SELECT u.account,
        r.ROLE_NAME
        FROM sys_user_role ur
        LEFT JOIN sys_user u
        ON ur.USER_ID = u.ID
        LEFT JOIN sys_role r
        ON ur.ROLE_ID    = r.ID
        WHERE u.account IN (%(accounts)s)
        ORDER BY u.account;
    ||| % { accounts: "'" + std.join("','",accounts) + "'" },

    query_user_info_by_accounts(account_names,sv_names):: |||
        SELECT u.account, asms.SV_NAME
        FROM 
            SYS_USER u 
            FULL OUTER JOIN SYS_ORGANIZATION o 
                ON u.ORGANIZATION_ID=o.ID
            FULL OUTER JOIN ASMS_SUBJ_SUPERVISE asms 
                ON o.ORG_ID=asms.ID 
        WHERE 
            asms.SV_NAME IN (%(sv_names)s)
            or u.account in (%(account_names)s);
    ||| % {account_names: func.in_expr(account_names), sv_names:func.in_expr(sv_names)},
}

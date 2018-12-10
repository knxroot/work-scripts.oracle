{
    delete_user_by_userids(user_ids):: {
        in_expr :: "'" + std.join("','",user_ids) + "'",
        sql: |||
            --　删除用户帐号
            DELETE
            FROM
                SYS_USER S
            WHERE
            S.ID in (%(in_expr)s);        
        ||| % self
    },
    delete_user_by_accounts(accounts):: {
        in_expr :: "'" + std.join("','",accounts) + "'",
        sql: |||
            --　删除用户帐号
            DELETE
            FROM
                SYS_USER S
            WHERE
            S.ACCOUNT in (%(in_expr)s);        
        ||| % self
    },
}

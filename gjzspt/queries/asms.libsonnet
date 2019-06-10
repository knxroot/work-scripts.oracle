{
    query_supervise(accounts):: |||
        //SELECT ss.*
        SELECT u.account, ss.INDUSTRY_ID, ss.INDUSTRY_NAME, ss.INDUSTRY_VALUE
        FROM ASMS_SUBJ_SUPERVISE ss,
        SYS_ORGANIZATION o,
        SYS_USER u
        WHERE ss.id           =o.org_id
        AND u.ORGANIZATION_ID = o.id
        AND u.account         in (%(accounts)s)
        ORDER BY u.account;
    ||| % { accounts: "'" + std.join("','",accounts) + "'"},

}

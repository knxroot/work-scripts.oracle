{
    query_supervise(account):: |||
        SELECT ss.*
        FROM ASMS_SUBJ_SUPERVISE ss,
        SYS_ORGANIZATION o,
        SYS_USER u
        WHERE ss.id           =o.org_id
        AND u.ORGANIZATION_ID = o.id
        AND u.account         ='%(account)s';
    ||| % { account: account},
    
}

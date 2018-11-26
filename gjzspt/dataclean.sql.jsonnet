local clean_orphan_users(orgtypes)={
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
};

{
    clean_asms_orphan_users: clean_orphan_users(['ASMS']),
    clean_ales_orphan_users: clean_orphan_users(['ALES']),
    clean_all_orphan_users: clean_orphan_users(['ASMS','ALES','ADS']),
}
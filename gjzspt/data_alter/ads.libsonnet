{
    update_by_name(old_name, new_name):: {
        old_name:: old_name,
        new_name:: new_name,
        sql: |||
            update ASMS_SUBJ_DETECTION set dt_name = '%(new_name)s' where dt_name = '%(old_name)s';
            update SYS_ORGANIZATION set ORG_NAME = '%(new_name)s' where ORG_NAME = '%(old_name)s';
            update SYS_USER set USER_NAME = '%(new_name)s_admin' where USER_NAME = '%(old_name)s';
        ||| % self,
    },
    
}

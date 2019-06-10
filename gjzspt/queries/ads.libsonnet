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
    },

    query_task_by_name(task_name):: {
        task_name:: task_name,
        sql: |||
            SELECT *
            FROM ADS_MONITOR_TASK
            WHERE task_name = '关于做好2019年农产品质量安全市级例行监测（风险监测）工作的通知';

            SELECT *
            FROM ADS_ORGAN_TASK ot,
            ADS_MONITOR_TASK mt
            WHERE ot.MONITOR_TASK_ID = mt.id
            AND mt.task_name         = '关于做好2019年农产品质量安全市级例行监测（风险监测）工作的通知';


            select *
            FROM ADS_ORGAN_TASK ot,
            ADS_RECIPE ar,
            ADS_MONITOR_TASK mt
            WHERE ar.ORGAN_TASK_ID = ot.id
            and ot.MONITOR_TASK_ID = mt.id
            AND mt.task_name         = '关于做好2019年农产品质量安全市级例行监测（风险监测）工作的通知';

            select *
            FROM ADS_FILE af,
            ADS_ORGAN_TASK ot,
            ADS_MONITOR_TASK mt
            WHERE af.ORGAN_TASK_ID = ot.id
            and af.MONITOR_TASK_ID = mt.id
            AND mt.task_name         = '关于做好2019年农产品质量安全市级例行监测（风险监测）工作的通知';
        ||| % self,
    },
}
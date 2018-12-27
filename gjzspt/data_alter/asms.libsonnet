{
    delete_by_area_prefix(area_prefix):: {
        sql: |||
            -- 临时主体
            DELETE
            FROM ASMS_SUBJ_ENT_TEMP S
            WHERE S.AREA_ID LIKE '%(area_prefix)s%%'
            -- 不良记录 在删除生产经营主体和临时主体前执行
            DELETE
            FROM ASMS_SUBJ_ENT_BADRECORD a
            WHERE a.ENTERPRISE_ID IN
            (SELECT ID
            FROM TTS_SCLTXXCJ_REGISTER_V2
            WHERE (AREA_ID LIKE '%(area_prefix)s%%')
            AND (ACCOUNT_RESOURCE !='SPYB'
            OR ACCOUNT_RESOURCE   IS NULL)
            AND APPROVE_STATUS    !=0
            UNION ALL
            SELECT S.ID
            FROM ASMS_SUBJ_ENT_TEMP S
            WHERE S.AREA_ID LIKE '%(area_prefix)s%%'
            );
            -- 删除常用意见
            DELETE
            FROM ASMS_COMMON_OPINION
            WHERE USER_ID IN
            (SELECT ID
            FROM SYS_USER
            WHERE ORGANIZATION_ID IN
                (SELECT ID
                FROM ASMS_SUBJ_SUPERVISE S
                WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
                AND SV_LEVEL > 0
                )
            );
            -- 考核任务
            DELETE
            FROM ASMS_INSPECTION_TASK TASK
            WHERE 1                 =1
            AND TASK.CREATE_ORG_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_SUPERVISE S
            WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
            AND SV_LEVEL > 0
            );
            -- 基地巡查与巡查人员关系表
            DELETE
            FROM ASMS_BASE_USER AU
            WHERE AU.BASE_INSPECTION_ID IN
            (SELECT B.ID
            FROM ASMS_BASE_INSPECTION B
            WHERE B.INSPECTION_SV_ID IN
                (SELECT ID
                FROM ASMS_SUBJ_SUPERVISE S
                WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
                AND SV_LEVEL > 0
                )
            );
            -- 基地巡查
            DELETE
            FROM ASMS_BASE_INSPECTION B
            WHERE B.INSPECTION_SV_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_SUPERVISE S
            WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
            AND SV_LEVEL > 0
            );
            -- 例行监测牵头单位关系表
            DELETE
            FROM ASMS_ROUTINE_LEAD_UNIT ARLU
            WHERE ARLU.ROUTINE_MONITOR_ID IN
            (SELECT ID
            FROM ASMS_ROUTINE_MONITOR M
            WHERE CREATE_ORG_ID IN
                (SELECT ID
                FROM ASMS_SUBJ_SUPERVISE S
                WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
                AND SV_LEVEL > 0
                )
            );
            -- 例行监测
            DELETE
            FROM ASMS_ROUTINE_MONITOR M
            WHERE CREATE_ORG_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_SUPERVISE S
            WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
            AND SV_LEVEL > 0
            );
            -- 专项监测牵头单位关系表
            DELETE
            FROM ASMS_SPECIAL_LEAD_UNIT ASLU
            WHERE ASLU.SPECIAL_MONITOR_ID IN
            (SELECT ID
            FROM ASMS_SPECIAL_MONITOR M
            WHERE CREATE_ORG_ID IN
                (SELECT ID
                FROM ASMS_SUBJ_SUPERVISE S
                WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
                AND SV_LEVEL > 0
                )
            );
            -- 专项监测
            DELETE
            FROM ASMS_SPECIAL_MONITOR M
            WHERE CREATE_ORG_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_SUPERVISE S
            WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
            AND SV_LEVEL > 0
            );
            -- 监督抽查检测标准关系表
            DELETE
            FROM ASMS_JC_STANDARD
            WHERE TASK_ID IN
            (SELECT ID
            FROM ASMS_CHECK_TASK M
            WHERE CREATE_ORG_ID IN
                (SELECT ID
                FROM ASMS_SUBJ_SUPERVISE S
                WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
                AND SV_LEVEL > 0
                )
            );
            -- 监督抽查判断标准关系表
            DELETE
            FROM ASMS_PD_STANDARD
            WHERE TASK_ID IN
            (SELECT ID
            FROM ASMS_CHECK_TASK M
            WHERE CREATE_ORG_ID IN
                (SELECT ID
                FROM ASMS_SUBJ_SUPERVISE S
                WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
                AND SV_LEVEL > 0
                )
            );
            -- 监督抽查受检单位关系表
            DELETE
            FROM ASMS_CHECK_TASK_ENTERPRISE
            WHERE CHECK_TASK_ID IN
            (SELECT ID
            FROM ASMS_CHECK_TASK M
            WHERE CREATE_ORG_ID IN
                (SELECT ID
                FROM ASMS_SUBJ_SUPERVISE S
                WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
                AND SV_LEVEL > 0
                )
            );
            -- 监督抽查受检项目关系表
            DELETE
            FROM ASMS_CHECK_OBJECT_CRITERION
            WHERE TASK_ID IN
            (SELECT ID
            FROM ASMS_CHECK_TASK M
            WHERE CREATE_ORG_ID IN
                (SELECT ID
                FROM ASMS_SUBJ_SUPERVISE S
                WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
                AND SV_LEVEL > 0
                )
            );
            -- 监督抽查
            DELETE
            FROM ASMS_CHECK_TASK M
            WHERE CREATE_ORG_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_SUPERVISE S
            WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
            AND SV_LEVEL > 0
            );
            -- 复检任务复检对象关联表
            DELETE
            FROM ASMS_RECHECK_OBJECT
            WHERE RECHECK_TASK_ID IN
            (SELECT ID
            FROM ASMS_RECHECK_TASK M
            WHERE CREATE_ORG_ID IN
                (SELECT ID
                FROM ASMS_SUBJ_SUPERVISE S
                WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
                AND SV_LEVEL > 0
                )
            );
            -- 复检任务
            DELETE
            FROM ASMS_RECHECK_TASK M
            WHERE CREATE_ORG_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_SUPERVISE S
            WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
            AND SV_LEVEL > 0
            );
            -- 应急任务与专家关系表
            DELETE
            FROM ASMS_EMERGENCY_EXPERT
            WHERE EMERGENCY_ID IN
            (SELECT ID
            FROM ASMS_EMERGENCY_TASK M
            WHERE CREATE_ORG_ID IN
                (SELECT ID
                FROM ASMS_SUBJ_SUPERVISE S
                WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
                AND SV_LEVEL > 0
                )
            );
            -- 应急任务
            DELETE
            FROM ASMS_EMERGENCY_TASK M
            WHERE CREATE_ORG_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_SUPERVISE S
            WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
            AND SV_LEVEL > 0
            );
            -- 监管机构变更记录表
            DELETE
            FROM ASMS_SUBJ_SV_CHANGE S
            WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%';
            -- 监管机构撤销记录表
            DELETE
            FROM ASMS_SUBJ_SV_REVOKE S
            WHERE S.SV_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_SUPERVISE S
            WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
            AND SV_LEVEL > 0
            );
            -- 监管机构注销记录表
            DELETE
            FROM ASMS_SUBJ_SV_CANCEL S
            WHERE S.SV_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_SUPERVISE S
            WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
            AND SV_LEVEL > 0
            );
            -- 执法机构变更记录表
            DELETE
            FROM ASMS_SUBJ_EL_CHANGE
            WHERE APPLY_EL_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_ENFORCE_LAW S
            WHERE S.EL_AREA_ID LIKE '%(area_prefix)s%%'
            AND EL_LEVEL > 0
            );
            -- 执法机构撤销记录表
            DELETE
            FROM ASMS_SUBJ_EL_REVOKE
            WHERE EL_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_ENFORCE_LAW S
            WHERE S.EL_AREA_ID LIKE '%(area_prefix)s%%'
            AND EL_LEVEL > 0
            );
            -- 执法机构注销记录表
            DELETE
            FROM ASMS_SUBJ_EL_CANCEL
            WHERE EL_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_ENFORCE_LAW S
            WHERE S.EL_AREA_ID LIKE '%(area_prefix)s%%'
            AND EL_LEVEL > 0
            );
            -- 检测机构变更记录表
            DELETE
            FROM ASMS_SUBJ_DT_CHANGE S
            WHERE S.DT_AREA_ID LIKE '%(area_prefix)s%%'
            AND DT_LEVEL > 0;
            -- 检测机构撤销记录表
            DELETE
            FROM ASMS_SUBJ_DT_REVOKE
            WHERE DT_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_DETECTION S
            WHERE S.DT_AREA_ID LIKE '%(area_prefix)s%%'
            AND DT_LEVEL > 0
            );
            -- 检测机构注销记录表
            DELETE
            FROM ASMS_SUBJ_DT_CANCEL
            WHERE DT_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_DETECTION S
            WHERE S.DT_AREA_ID LIKE '%(area_prefix)s%%'
            AND DT_LEVEL > 0
            );
            -- 系统用户角色对应关系表
            DELETE
            FROM SYS_USER_ROLE
            WHERE USER_ID IN
            (SELECT ID
            FROM SYS_USER
            WHERE ORGANIZATION_ID IN
                (SELECT ID
                FROM SYS_ORGANIZATION
                WHERE ORG_ID IN
                (SELECT ID
                FROM ASMS_SUBJ_SUPERVISE S
                WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
                AND SV_LEVEL > 0
                )
                )
            );
            -- 系统用户表
            DELETE
            FROM SYS_USER
            WHERE ORGANIZATION_ID IN
            (SELECT ID
            FROM SYS_ORGANIZATION
            WHERE ORG_ID IN
                (SELECT ID
                FROM ASMS_SUBJ_SUPERVISE S
                WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
                AND SV_LEVEL > 0
                )
            );
            -- 系统组织机构与机构信息关系表
            DELETE
            FROM SYS_ORGANIZATION
            WHERE ORG_ID IN
            (SELECT ID
            FROM ASMS_SUBJ_SUPERVISE S
            WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
            AND SV_LEVEL > 0
            );
            -- 监管机构主体表
            DELETE
            FROM ASMS_SUBJ_SUPERVISE S
            WHERE S.SV_AREA_ID LIKE '%(area_prefix)s%%'
            AND SV_LEVEL > 0;
        ||| % {area_prefix: area_prefix},
    },

    clean_all_data_by_svnames(sv_names)::{
        in_expr :: "'" + std.join("','",sv_names) + "'",
        sql: |||
            --删除常用意见:
            DELETE
            FROM ASMS_COMMON_OPINION
            WHERE id IN
            (SELECT id
            FROM ASMS_COMMON_OPINION
            WHERE USER_ID IN
                (SELECT ID
                FROM SYS_USER
                WHERE ORGANIZATION_ID IN
                (SELECT ID
                FROM SYS_ORGANIZATION
                WHERE ORG_ID IN
                    (SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE trim(s.SV_NAME) IN (%(in_expr)s)
                    )
                )
                )
            );
            --考核任务:
            DELETE
            FROM ASMS_INSPECTION_TASK T
            WHERE T.id IN
            (SELECT task.id
            FROM ASMS_INSPECTION_TASK task
            WHERE 1                 =1
            AND task.CREATE_ORG_ID IN
                (SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE trim(s.SV_NAME) IN (%(in_expr)s)
                )
            );
            --基地巡查与巡查人员关系表:
            DELETE
            FROM ASMS_BASE_USER ABU
            WHERE ABU.id IN
            (SELECT id
            FROM ASMS_BASE_USER AU
            WHERE AU.BASE_INSPECTION_ID IN
                (SELECT B.ID
                FROM ASMS_BASE_INSPECTION B
                WHERE B.INSPECTION_SV_NAME IN (%(in_expr)s)
                )
            );
            --基地巡查:
            DELETE
            FROM ASMS_BASE_INSPECTION ABI
            WHERE ABI.id IN
            (SELECT id
            FROM ASMS_BASE_INSPECTION B
            WHERE B.INSPECTION_SV_NAME IN (%(in_expr)s)
            );
            --例行监测牵头单位关系表:
            DELETE
            FROM ASMS_ROUTINE_LEAD_UNIT
            WHERE ID IN
            (SELECT id
            FROM ASMS_ROUTINE_LEAD_UNIT ARLU
            WHERE ARLU.ROUTINE_MONITOR_ID IN
                (SELECT id
                FROM ASMS_ROUTINE_MONITOR M
                WHERE CREATE_ORG_ID IN
                (SELECT id FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
                )
                )
            );
            --例行监测:
            DELETE
            FROM ASMS_ROUTINE_MONITOR
            WHERE id IN
            (SELECT id
            FROM ASMS_ROUTINE_MONITOR M
            WHERE CREATE_ORG_ID IN
                (SELECT id FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
                )
            );
            --专项监测牵头单位关系表:
            DELETE
            FROM ASMS_SPECIAL_LEAD_UNIT
            WHERE ID IN
            (SELECT id
            FROM ASMS_SPECIAL_LEAD_UNIT ASLU
            WHERE ASLU.SPECIAL_MONITOR_ID IN
                (SELECT id
                FROM ASMS_SPECIAL_MONITOR M
                WHERE CREATE_ORG_ID IN
                (SELECT id FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
                )
                )
            );
            --专项监测表:
            DELETE
            FROM ASMS_SPECIAL_MONITOR
            WHERE id IN
            (SELECT id
            FROM ASMS_SPECIAL_MONITOR M
            WHERE CREATE_ORG_ID IN
                (SELECT id FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
                )
            );
            --监督抽查检测标准关系表:
            DELETE
            FROM ASMS_JC_STANDARD
            WHERE id IN
            (SELECT id
            FROM ASMS_JC_STANDARD
            WHERE TASK_ID IN
                (SELECT ID
                FROM ASMS_CHECK_TASK M
                WHERE CREATE_ORG_ID IN
                ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
                )
                )
            );
            --监督抽查判断标准关系表:
            DELETE
            FROM ASMS_PD_STANDARD
            WHERE id IN
            (SELECT id
            FROM ASMS_PD_STANDARD
            WHERE TASK_ID IN
                (SELECT ID
                FROM ASMS_CHECK_TASK M
                WHERE CREATE_ORG_ID IN
                ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
                )
                )
            );
            --监督抽查受检单位关系表:
            DELETE
            FROM ASMS_CHECK_TASK_ENTERPRISE
            WHERE id IN
            (SELECT id
            FROM ASMS_CHECK_TASK_ENTERPRISE
            WHERE CHECK_TASK_ID IN
                (SELECT ID
                FROM ASMS_CHECK_TASK M
                WHERE CREATE_ORG_ID IN
                ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
                )
                )
            );
            --监督抽查受检项目关系表:
            DELETE
            FROM ASMS_CHECK_OBJECT_CRITERION
            WHERE id IN
            (SELECT id
            FROM ASMS_CHECK_OBJECT_CRITERION
            WHERE TASK_ID IN
                (SELECT id
                FROM ASMS_CHECK_TASK M
                WHERE CREATE_ORG_ID IN
                ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
                )
                )
            );
            --监督抽查:
            DELETE
            FROM ASMS_CHECK_TASK
            WHERE id IN
            (SELECT id
            FROM ASMS_CHECK_TASK M
            WHERE CREATE_ORG_ID IN
                ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
                )
            );
            --复检任务复检对象关联表:
            DELETE
            FROM ASMS_RECHECK_OBJECT
            WHERE id IN
            (SELECT id
            FROM ASMS_RECHECK_OBJECT
            WHERE RECHECK_TASK_ID IN
                (SELECT id
                FROM ASMS_RECHECK_TASK M
                WHERE CREATE_ORG_ID IN
                ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
                )
                )
            );
            --复检任务:
            DELETE
            FROM ASMS_RECHECK_TASK
            WHERE id IN
            (SELECT id
            FROM ASMS_RECHECK_TASK M
            WHERE CREATE_ORG_ID IN
                ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
                )
            );
            --应急任务与专家关系表:
            DELETE
            FROM ASMS_EMERGENCY_EXPERT
            WHERE id IN
            (SELECT id
            FROM ASMS_EMERGENCY_EXPERT
            WHERE EMERGENCY_ID IN
                (SELECT id
                FROM ASMS_EMERGENCY_TASK M
                WHERE CREATE_ORG_ID IN
                ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
                )
                )
            );
            --应急任务:
            DELETE
            FROM ASMS_EMERGENCY_TASK
            WHERE id IN
            (SELECT id
            FROM ASMS_EMERGENCY_TASK M
            WHERE CREATE_ORG_ID IN
                ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
                )
            );
            --监管机构变更记录表:
            DELETE
            FROM ASMS_SUBJ_SV_CANCEL
            WHERE sv_id IN
            (SELECT id FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN (%(in_expr)s)
            );
            --监管机构注销记录表:
            DELETE
            FROM ASMS_SUBJ_SV_CANCEL
            WHERE sv_id IN
            (SELECT id FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN (%(in_expr)s)
            );
            --监管机构撤销记录表:
            DELETE
            FROM ASMS_SUBJ_SV_REVOKE
            WHERE sv_id IN
            (SELECT id FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN (%(in_expr)s)
            );
            --执法机构变更记录表:
            DELETE
            FROM ASMS_SUBJ_EL_CHANGE
            WHERE id IN
            (SELECT id
            FROM ASMS_SUBJ_EL_CHANGE
            WHERE APPLY_EL_ID IN
                (SELECT ID FROM ASMS_SUBJ_ENFORCE_LAW s WHERE s.EL_NAME IN (%(in_expr)s)
                )
            );
            --执法机构注销记录表:
            DELETE
            FROM ASMS_SUBJ_EL_CANCEL
            WHERE id IN
            (SELECT id
            FROM ASMS_SUBJ_EL_CANCEL
            WHERE el_id IN
                (SELECT ID FROM ASMS_SUBJ_ENFORCE_LAW s WHERE s.EL_NAME IN (%(in_expr)s)
                )
            );
            --执法机构撤销记录表:
            DELETE
            FROM ASMS_SUBJ_EL_REVOKE
            WHERE id IN
            (SELECT id
            FROM ASMS_SUBJ_EL_REVOKE
            WHERE el_id IN
                (SELECT ID FROM ASMS_SUBJ_ENFORCE_LAW s WHERE s.EL_NAME IN (%(in_expr)s)
                )
            );
            --系统用户角色对应关系表:
            DELETE
            FROM SYS_USER_ROLE
            WHERE id IN
            (SELECT id
            FROM SYS_USER_ROLE
            WHERE USER_ID IN
                (SELECT id
                FROM SYS_USER
                WHERE ORGANIZATION_ID IN
                (SELECT id
                FROM SYS_ORGANIZATION
                WHERE ORG_ID IN
                    (SELECT id FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN (%(in_expr)s)
                    )
                )
                )
            );
            --系统用户表:
            DELETE
            FROM SYS_USER
            WHERE id IN
            (SELECT id
            FROM SYS_USER
            WHERE ORGANIZATION_ID IN
                (SELECT id
                FROM SYS_ORGANIZATION
                WHERE ORG_ID IN
                (SELECT id FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN (%(in_expr)s)
                )
                )
            );
            --系统组织机构与机构信息关系表:
            DELETE
            FROM SYS_ORGANIZATION
            WHERE id IN
            (SELECT id
            FROM SYS_ORGANIZATION
            WHERE ORG_ID IN
                (SELECT id FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN (%(in_expr)s)
                )
            );
            --监管机构主体表:
            DELETE
            FROM ASMS_SUBJ_SUPERVISE
            WHERE id IN
            (SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)
            );
          ||| % self,
    },

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

    clean_asms_sv_change(sv_names):: {
        in_expr :: "'" + std.join("','",sv_names) + "'",
        sql: |||
            -- 监管机构变更记录：
            DELETE  FROM ASMS_SUBJ_SV_CHANGE WHERE SV_NAME IN (%(in_expr)s);
        ||| % self,
    },

    add_role(account, role_name, industry_name):: {
        sql: |||
            ---更新监管机构帐号［%(account)s］对应监管机构的行业［%(industry_name)s］
            UPDATE "ASMS_SUBJ_SUPERVISE"
            SET "INDUSTRY_ID" = INDUSTRY_ID
            || ','
            ||
            (SELECT id FROM sys_dict_data WHERE dict_name IN ('%(industry_name)s')
            ),
            "INDUSTRY_NAME" = INDUSTRY_NAME
            || ','
            ||
            (SELECT dict_name FROM sys_dict_data WHERE dict_name IN ('%(industry_name)s')
            ),
            "INDUSTRY_VALUE" = INDUSTRY_VALUE
            || ','
            ||
            (SELECT dict_value FROM sys_dict_data WHERE dict_name IN ('%(industry_name)s')
            )
            WHERE "ID" =
            (SELECT ss.id
            FROM ASMS_SUBJ_SUPERVISE ss,
                SYS_ORGANIZATION o,
                SYS_USER u
            WHERE ss.id           =o.org_id
            AND u.ORGANIZATION_ID = o.id
            AND u.account         ='%(account)s'
            );
            ---增加监管机构帐号［%(account)s］的角色［%(role_name)s］
            INSERT INTO "SYS_USER_ROLE"
            (
                "ID",
                "USER_ID",
                "ROLE_ID",
                "CREATE_BY",
                "CREATE_TIME",
                "UPDATE_BY",
                "UPDATE_TIME",
                "DEL_FLAG"
            )
            VALUES
            (
                '%(id)s',
                (select id from sys_user where account='%(account)s'),
                (select id from sys_role where role_name = '%(role_name)s'),
                NULL,
                sysdate,
                NULL,
                sysdate,
                'N'
            );            
        ||| % {id: std.md5(account) + std.md5(role_name), 
        account: account, role_name: role_name, industry_name: industry_name },
    },    
}

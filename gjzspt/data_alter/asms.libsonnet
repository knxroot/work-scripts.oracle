{

    clean_all_data_by_account(sv_names)::{
        in_expr :: "'" + std.join("','",sv_names) + "'",
        sql: |||
            --删除常用意见:
            DELETE FROM ASMS_COMMON_OPINION WHERE id in (select id from ASMS_COMMON_OPINION where USER_ID in (SELECT ID FROM SYS_USER WHERE ORGANIZATION_ID IN (SELECT ID FROM SYS_ORGANIZATION WHERE ORG_ID IN (SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE trim(s.SV_NAME) IN (%(in_expr)s))))); 

            --考核任务:
            DELETE FROM ASMS_INSPECTION_TASK T WHERE T.id IN (SELECT task.id FROM ASMS_INSPECTION_TASK task WHERE 1=1 AND task.CREATE_ORG_ID in (SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE trim(s.SV_NAME) IN (%(in_expr)s)));

            --基地巡查与巡查人员关系表:
            DELETE FROM ASMS_BASE_USER ABU WHERE ABU.id in (SELECT id from ASMS_BASE_USER AU WHERE AU.BASE_INSPECTION_ID In (SELECT B.ID FROM ASMS_BASE_INSPECTION B WHERE B.INSPECTION_SV_NAME in (%(in_expr)s)));

            --基地巡查:
            DELETE FROM ASMS_BASE_INSPECTION ABI WHERE ABI.id In(SELECT id FROM ASMS_BASE_INSPECTION B WHERE B.INSPECTION_SV_NAME in (%(in_expr)s));

            --例行监测牵头单位关系表:
            DELETE FROM ASMS_ROUTINE_LEAD_UNIT WHERE ID in (SELECT id FROM ASMS_ROUTINE_LEAD_UNIT ARLU WHERE ARLU.ROUTINE_MONITOR_ID IN (SELECT id FROM ASMS_ROUTINE_MONITOR M WHERE CREATE_ORG_ID IN (SELECT id FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s))));

            --例行监测:
            delete from ASMS_ROUTINE_MONITOR where id in ( SELECT id FROM ASMS_ROUTINE_MONITOR M WHERE CREATE_ORG_ID IN (SELECT id FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)));

            --专项监测牵头单位关系表:
            DELETE FROM ASMS_SPECIAL_LEAD_UNIT WHERE ID in (SELECT id FROM ASMS_SPECIAL_LEAD_UNIT ASLU WHERE ASLU.SPECIAL_MONITOR_ID IN (SELECT id FROM ASMS_SPECIAL_MONITOR M WHERE CREATE_ORG_ID IN (SELECT id FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s))));

            --专项监测表:
            DELETE FROM ASMS_SPECIAL_MONITOR WHERE id in (SELECT id FROM ASMS_SPECIAL_MONITOR M WHERE CREATE_ORG_ID IN (SELECT id FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)));

            --监督抽查检测标准关系表:
            delete from ASMS_JC_STANDARD where id in (SELECT id FROM ASMS_JC_STANDARD WHERE TASK_ID in (SELECT ID FROM ASMS_CHECK_TASK M WHERE CREATE_ORG_ID IN ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s))));

            --监督抽查判断标准关系表:	
            delete from ASMS_PD_STANDARD where id in (SELECT id FROM ASMS_PD_STANDARD WHERE TASK_ID in (SELECT ID FROM ASMS_CHECK_TASK M WHERE CREATE_ORG_ID IN ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s))));

            --监督抽查受检单位关系表:
            delete from ASMS_CHECK_TASK_ENTERPRISE where id in ( SELECT id FROM ASMS_CHECK_TASK_ENTERPRISE WHERE CHECK_TASK_ID in (SELECT ID FROM ASMS_CHECK_TASK M WHERE CREATE_ORG_ID IN ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s))));

            --监督抽查受检项目关系表:
            delete from ASMS_CHECK_OBJECT_CRITERION where id in (SELECT id FROM ASMS_CHECK_OBJECT_CRITERION WHERE TASK_ID in (SELECT id FROM ASMS_CHECK_TASK M WHERE CREATE_ORG_ID IN ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s))));

            --监督抽查:
            delete from ASMS_CHECK_TASK where id in(SELECT id FROM ASMS_CHECK_TASK M WHERE CREATE_ORG_ID IN ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)));

            --复检任务复检对象关联表:
            delete from ASMS_RECHECK_OBJECT where id in (SELECT id FROM ASMS_RECHECK_OBJECT WHERE RECHECK_TASK_ID in (SELECT id FROM ASMS_RECHECK_TASK M WHERE CREATE_ORG_ID IN ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s))));

            --复检任务:
            delete from ASMS_RECHECK_TASK where id in(SELECT id FROM ASMS_RECHECK_TASK M WHERE CREATE_ORG_ID IN ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)));

            --应急任务与专家关系表:
            delete from ASMS_EMERGENCY_EXPERT where id in (SELECT id FROM ASMS_EMERGENCY_EXPERT WHERE EMERGENCY_ID in (SELECT id FROM ASMS_EMERGENCY_TASK M WHERE CREATE_ORG_ID IN ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s))));

            --应急任务:
            delete from ASMS_EMERGENCY_TASK where id in (SELECT id FROM ASMS_EMERGENCY_TASK M WHERE CREATE_ORG_ID IN ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s)));

            --监管机构变更记录表:
            delete from ASMS_SUBJ_SV_CANCEL where sv_id in (select id from ASMS_SUBJ_SUPERVISE where SV_NAME IN (%(in_expr)s));

            --监管机构注销记录表:	
            delete from ASMS_SUBJ_SV_CANCEL where sv_id in (select id from ASMS_SUBJ_SUPERVISE where SV_NAME IN (%(in_expr)s));

            --监管机构撤销记录表:
            delete from ASMS_SUBJ_SV_REVOKE where sv_id in (select id from ASMS_SUBJ_SUPERVISE where SV_NAME IN (%(in_expr)s));

            --执法机构变更记录表:
            delete from ASMS_SUBJ_EL_CHANGE where id in (select id from ASMS_SUBJ_EL_CHANGE WHERE APPLY_EL_ID IN (SELECT ID FROM ASMS_SUBJ_ENFORCE_LAW s WHERE s.EL_NAME IN (%(in_expr)s)));

            --执法机构注销记录表:
            delete from ASMS_SUBJ_EL_CANCEL where id in (select id from ASMS_SUBJ_EL_CANCEL WHERE el_id IN (SELECT ID FROM ASMS_SUBJ_ENFORCE_LAW s WHERE s.EL_NAME IN (%(in_expr)s)));
            
            --执法机构撤销记录表:
            delete from ASMS_SUBJ_EL_REVOKE where id in (select id from ASMS_SUBJ_EL_REVOKE WHERE el_id IN (SELECT ID FROM ASMS_SUBJ_ENFORCE_LAW s WHERE s.EL_NAME IN (%(in_expr)s)));
            
            --系统用户角色对应关系表:
            delete from SYS_USER_ROLE where id in (select id from SYS_USER_ROLE where USER_ID IN (select id from SYS_USER where ORGANIZATION_ID in (select id from SYS_ORGANIZATION where ORG_ID in (select id from ASMS_SUBJ_SUPERVISE where SV_NAME IN (%(in_expr)s)))));

            --系统用户表:
            delete from SYS_USER where id in (select id from SYS_USER where ORGANIZATION_ID in (select id from SYS_ORGANIZATION where ORG_ID in (select id from ASMS_SUBJ_SUPERVISE where SV_NAME IN (%(in_expr)s))));

            --系统组织机构与机构信息关系表:
            delete from SYS_ORGANIZATION where id in (select id from SYS_ORGANIZATION where ORG_ID in (select id from ASMS_SUBJ_SUPERVISE where SV_NAME IN (%(in_expr)s)));

            --监管机构主体表:
            delete from ASMS_SUBJ_SUPERVISE where id in (SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN (%(in_expr)s));
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
    }
}

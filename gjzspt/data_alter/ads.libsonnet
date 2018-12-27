{
    delete_by_area_prefix(area_prefix):: {
        sql: |||
            --检测系统 根据任务名称来删除相关数据
            --检测系统 附件
            DELETE
            FROM
                (
                    SELECT
                        A .*
                    FROM
                        ADS_FILE A
                    INNER JOIN ADS_MONITOR_TASK b ON A .MONITOR_TASK_ID = b. ID
                    WHERE
                        b.ORGAN_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_SUBJ_DETECTION
                            WHERE
                                DT_LEVEL > 0
                                AND DT_AREA_ID LIKE '%(area_prefix)s%%'
                                AND DT_TYPE = '检测机构'
                        )
                );

            --检测系统 检测项
            DELETE
            FROM
                (
                    SELECT
                        A .*
                    FROM
                        ADS_CHECK_INFO A
                    INNER JOIN ADS_ORGAN_TASK b ON A .ORGAN_TASK_ID = b. ID
                    INNER JOIN ADS_MONITOR_TASK c ON c. ID = b.monitor_task_id
                    WHERE
                        c.ORGAN_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_SUBJ_DETECTION
                            WHERE
                                DT_LEVEL > 0
                                AND DT_AREA_ID LIKE '%(area_prefix)s%%'
                                AND DT_TYPE = '检测机构'
                        )
                );

            --检测系统 抽样单
            DELETE
            FROM
                (
                    SELECT
                        A .*
                    FROM
                        ADS_MONITOR_SAMPLE A
                    INNER JOIN ADS_ORGAN_TASK b ON A .ORGAN_TASK_ID = b. ID
                    INNER JOIN ADS_MONITOR_TASK c ON c. ID = b.monitor_task_id
                    WHERE
                        c.ORGAN_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_SUBJ_DETECTION
                            WHERE
                                DT_LEVEL > 0
                                AND DT_AREA_ID LIKE '%(area_prefix)s%%'
                                AND DT_TYPE = '检测机构'
                        )
                );

            -- 检测系统 承担单位
            DELETE
            FROM
                (
                    SELECT
                        b.*
                    FROM
                        ADS_MONITOR_TASK A
                    INNER JOIN ADS_ORGAN_TASK b ON A . ID = b.monitor_task_id
                    WHERE
                        A .ORGAN_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_SUBJ_DETECTION
                            WHERE
                                DT_LEVEL > 0
                                AND DT_AREA_ID LIKE '%(area_prefix)s%%'
                                AND DT_TYPE = '检测机构'
                        )
                );

            --检测系统 牵头单位
            DELETE
            FROM
                (
                    SELECT
                        *
                    FROM
                        ADS_MONITOR_TASK
                    WHERE
                        ORGAN_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_SUBJ_DETECTION
                            WHERE
                                DT_LEVEL > 0
                                AND DT_AREA_ID LIKE '%(area_prefix)s%%'
                                AND DT_TYPE = '检测机构'
                        )
                );

            -- 清除检测对象包表(ADS_CHECK_OBJECT_PACKAGE)
            DELETE
            FROM
                (
                    SELECT
                        *
                    FROM
                        ADS_CHECK_OBJECT_PACKAGE T
                    WHERE
                        T .organ_id IN (
                            SELECT
                                T .org_id
                            FROM
                                SYS_ORGANIZATION T
                            WHERE
                                T .org_name IN (
                                    SELECT
                                        DT_NAME
                                    FROM
                                        ASMS_SUBJ_DETECTION
                                    WHERE
                                        DT_LEVEL > 0
                                        AND DT_AREA_ID LIKE '%(area_prefix)s%%'
                                        AND DT_TYPE = '检测机构'
                                )
                        )
                );

            -- 检测项表(ADS_CHECK_PACKAGE)
            DELETE
            FROM
                (
                    SELECT
                        *
                    FROM
                        ADS_CHECK_PACKAGE T
                    WHERE
                        T .organ_id IN (
                            SELECT
                                T .org_id
                            FROM
                                SYS_ORGANIZATION T
                            WHERE
                                T .org_name IN (
                                    SELECT
                                        DT_NAME
                                    FROM
                                        ASMS_SUBJ_DETECTION
                                    WHERE
                                        DT_LEVEL > 0
                                        AND DT_AREA_ID LIKE '%(area_prefix)s%%'
                                        AND DT_TYPE = '检测机构'
                                )
                        )
                );

            -- 模型配置表(ADS_MONITOR_MODEL)
            DELETE
            FROM
                (
                    SELECT
                        *
                    FROM
                        ADS_MONITOR_MODEL T
                    WHERE
                        T .organ_id IN (
                            SELECT
                                ID
                            FROM
                                ASMS_SUBJ_DETECTION
                            WHERE
                                DT_LEVEL > 0
                                AND DT_AREA_ID LIKE '%(area_prefix)s%%'
                                AND DT_TYPE = '检测机构'
                        )
                );


            --清除检测机构用户
            DELETE
            FROM
                (
                    SELECT
                        A .*
                    FROM
                        SYS_USER A
                    INNER JOIN SYS_ORGANIZATION b ON A .ORGANIZATION_ID = b. ID
                    WHERE
                        b.ORG_TYPE = 'ADS'
                    AND ORG_NAME IN (
                        SELECT
                            DT_NAME
                        FROM
                            ASMS_SUBJ_DETECTION
                        WHERE
                            DT_LEVEL > 0
                            AND DT_AREA_ID LIKE '%(area_prefix)s%%'
                            AND DT_TYPE = '检测机构'
                    )
                );


            --清除检测机构
            DELETE
            FROM
                (
                    SELECT
                        *
                    FROM
                        SYS_ORGANIZATION
                    WHERE
                        ORG_TYPE = 'ADS'
                    AND ORG_NAME IN (
                        SELECT
                            DT_NAME
                        FROM
                            ASMS_SUBJ_DETECTION
                        WHERE
                            DT_LEVEL > 0
                            AND DT_AREA_ID LIKE '%(area_prefix)s%%'
                            AND DT_TYPE = '检测机构'
                    )
                );

            DELETE
            FROM
                (
                    SELECT
                        *
                
                        FROM
                            ASMS_SUBJ_DETECTION
                        WHERE
                            DT_LEVEL > 0
                            AND DT_AREA_ID LIKE '%(area_prefix)s%%'
                            AND DT_TYPE = '检测机构'
                );
        ||| % {area_prefix: area_prefix},
    },

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

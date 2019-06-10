local func = import '../func.jsn';

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
    ||| % { area_prefix: area_prefix },
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

  delete_dummy_org(org_name):: {
    sql: |||
      DELETE FROM ASMS_SUBJ_DETECTION WHERE DT_NAME = '%(org_name)s';
      DELETE FROM SYS_ORGANIZATION WHERE SYS_ORGANIZATION.ORG_NAME = '%(org_name)s';
    ||| % { org_name: org_name },
  },

  delete_task_by_name(task_name):: {
    sql: |||
      delete from ADS_MONITOR_TASK
      WHERE task_name = '%(task_name)s';
    ||| % { task_name: task_name },
  },

  delete_all_by_names(names):: |||
    --检测系统 根据检测机构名称来删除相关数据
    --检测系统 附件
    DELETE
    FROM
        (
            SELECT
                *
            FROM
                ADS_FILE
            WHERE
                MONITOR_TASK_ID IN (
                        SELECT
                        id
                    FROM
                        ADS_MONITOR_TASK
                    WHERE
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_ROUTINE_MONITOR
                            WHERE
                                RM_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_SPECIAL_MONITOR
                            WHERE
                                SM_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_CHECK_TASK
                            WHERE
                                TASK_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_RECHECK_TASK
                            WHERE
                                RECHECK_UNIT_NAME IN (
                                %(names)s
                            )
                        )
                        or
                        ID IN (
                            SELECT
                                ID
                            FROM
                                ALES_ENTRUST_DETECTION
                            WHERE
                                TASK_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                    
                )
        );

    --检测系统 检测项
    DELETE
    FROM
        (
            SELECT
                e.*
            FROM
                ads_monitor_task a,
            ads_organ_task b,
            ads_check_info c,
            ads_monitor_sample d,
            ads_info_project e
            where a.id = b.monitor_task_id
            and b.id = c.organ_task_id
            and c.monitor_sample_id=d.id
            and c.id=e.check_info_id
            and
                b.MONITOR_TASK_ID IN (
                        SELECT
                        id
                    FROM
                        ADS_MONITOR_TASK
                    WHERE
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_ROUTINE_MONITOR
                            WHERE
                                RM_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_SPECIAL_MONITOR
                            WHERE
                                SM_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_CHECK_TASK
                            WHERE
                                TASK_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_RECHECK_TASK
                            WHERE
                                RECHECK_UNIT_NAME IN (
                                %(names)s
                            )
                        )
                        or
                        ID IN (
                            SELECT
                                ID
                            FROM
                                ALES_ENTRUST_DETECTION
                            WHERE
                                TASK_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                    
                )
        );

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
                c.ID IN (
                        SELECT
                        id
                    FROM
                        ADS_MONITOR_TASK
                    WHERE
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_ROUTINE_MONITOR
                            WHERE
                                RM_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_SPECIAL_MONITOR
                            WHERE
                                SM_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_CHECK_TASK
                            WHERE
                                TASK_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_RECHECK_TASK
                            WHERE
                                RECHECK_UNIT_NAME IN (
                                %(names)s
                            )
                        )
                        or
                        ID IN (
                            SELECT
                                ID
                            FROM
                                ALES_ENTRUST_DETECTION
                            WHERE
                                TASK_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                    
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
                c.ID IN (
                        SELECT
                        id
                    FROM
                        ADS_MONITOR_TASK
                    WHERE
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_ROUTINE_MONITOR
                            WHERE
                                RM_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_SPECIAL_MONITOR
                            WHERE
                                SM_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_CHECK_TASK
                            WHERE
                                TASK_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_RECHECK_TASK
                            WHERE
                                RECHECK_UNIT_NAME IN (
                                %(names)s
                            )
                        )
                        or
                        ID IN (
                            SELECT
                                ID
                            FROM
                                ALES_ENTRUST_DETECTION
                            WHERE
                                TASK_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                    
                )
        );

    -- 检测系统 承担单位
    DELETE
    FROM
        (
            SELECT
                b .*
            FROM
                ADS_MONITOR_TASK A
            INNER JOIN ADS_ORGAN_TASK b ON A . ID = b.monitor_task_id
            WHERE
                A.ID IN (
                        SELECT
                        id
                    FROM
                        ADS_MONITOR_TASK
                    WHERE
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_ROUTINE_MONITOR
                            WHERE
                                RM_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_SPECIAL_MONITOR
                            WHERE
                                SM_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        SUP_ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_CHECK_TASK
                            WHERE
                                TASK_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                        or
                        ID IN (
                            SELECT
                                ID
                            FROM
                                ASMS_RECHECK_TASK
                            WHERE
                                RECHECK_UNIT_NAME IN (
                                %(names)s
                            )
                        )
                        or
                        ID IN (
                            SELECT
                                ID
                            FROM
                                ALES_ENTRUST_DETECTION
                            WHERE
                                TASK_RELEASE_UNIT IN (
                                %(names)s
                            )
                        )
                    
                )
        );

    --检测系统 牵头单位 
    --例行
    DELETE
    FROM
        (
            SELECT
                *
            FROM
                ADS_MONITOR_TASK
            WHERE
                SUP_ID IN (
                    SELECT
                        ID
                    FROM
                        ASMS_ROUTINE_MONITOR
                    WHERE
                        RM_RELEASE_UNIT IN (
                        %(names)s
                    )
                )
                or
                SUP_ID IN (
                    SELECT
                        ID
                    FROM
                        ASMS_SPECIAL_MONITOR
                    WHERE
                        SM_RELEASE_UNIT IN (
                        %(names)s
                    )
                )
                or
                SUP_ID IN (
                    SELECT
                        ID
                    FROM
                        ASMS_CHECK_TASK
                    WHERE
                        TASK_RELEASE_UNIT IN (
                        %(names)s
                    )
                )
                or
                ID IN (
                    SELECT
                        ID
                    FROM
                        ASMS_RECHECK_TASK
                    WHERE
                        RECHECK_UNIT_NAME IN (
                        %(names)s
                    )
                )
                or
                        ID IN (
                            SELECT
                                ID
                            FROM
                                ALES_ENTRUST_DETECTION
                            WHERE
                                TASK_RELEASE_UNIT IN (
                                %(names)s
                            )
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
                %(names)s
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
                %(names)s
            )
        );

    --清除检测机构
    DELETE
    FROM
        (
            SELECT
                *
        
                FROM
                    ASMS_SUBJ_DETECTION
                WHERE
                    DT_NAME IN (
                %(names)s
            )
        );
  ||| % { names: func.in_expr(names) },
}

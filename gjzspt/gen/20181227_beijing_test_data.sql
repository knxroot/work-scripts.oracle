SET AUTOCOMMIT OFF;

BEGIN
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
        (SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE trim(s.SV_NAME) IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    (SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE trim(s.SV_NAME) IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    WHERE B.INSPECTION_SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
    )
);
--基地巡查:
DELETE
FROM ASMS_BASE_INSPECTION ABI
WHERE ABI.id IN
(SELECT id
FROM ASMS_BASE_INSPECTION B
WHERE B.INSPECTION_SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    (SELECT id FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    (SELECT id FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    (SELECT id FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    (SELECT id FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    ( SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
    )
);
--监管机构变更记录表:
DELETE
FROM ASMS_SUBJ_SV_CANCEL
WHERE sv_id IN
(SELECT id FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
);
--监管机构注销记录表:
DELETE
FROM ASMS_SUBJ_SV_CANCEL
WHERE sv_id IN
(SELECT id FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
);
--监管机构撤销记录表:
DELETE
FROM ASMS_SUBJ_SV_REVOKE
WHERE sv_id IN
(SELECT id FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
);
--执法机构变更记录表:
DELETE
FROM ASMS_SUBJ_EL_CHANGE
WHERE id IN
(SELECT id
FROM ASMS_SUBJ_EL_CHANGE
WHERE APPLY_EL_ID IN
    (SELECT ID FROM ASMS_SUBJ_ENFORCE_LAW s WHERE s.EL_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
    )
);
--执法机构注销记录表:
DELETE
FROM ASMS_SUBJ_EL_CANCEL
WHERE id IN
(SELECT id
FROM ASMS_SUBJ_EL_CANCEL
WHERE el_id IN
    (SELECT ID FROM ASMS_SUBJ_ENFORCE_LAW s WHERE s.EL_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
    )
);
--执法机构撤销记录表:
DELETE
FROM ASMS_SUBJ_EL_REVOKE
WHERE id IN
(SELECT id
FROM ASMS_SUBJ_EL_REVOKE
WHERE el_id IN
    (SELECT ID FROM ASMS_SUBJ_ENFORCE_LAW s WHERE s.EL_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
        (SELECT id FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    (SELECT id FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
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
    (SELECT id FROM ASMS_SUBJ_SUPERVISE WHERE SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
    )
);
--监管机构主体表:
DELETE
FROM ASMS_SUBJ_SUPERVISE
WHERE id IN
(SELECT ID FROM ASMS_SUBJ_SUPERVISE s WHERE s.SV_NAME IN ('海淀区监管','北京县级监管机构一测试','北京市级监管机构一测试','北京省级监管机构一测试')
);
--- 删除-现场巡查-脏数据
DELETE FROM ALES_DAILY_ENFORCE_LAW WHERE CREATE_BY IN
(
SELECT
    P.CREATE_BY
FROM
    ALES_DAILY_ENFORCE_LAW P
LEFT JOIN SYS_USER H ON P.CREATE_BY = H.ID 
LEFT JOIN SYS_ORGANIZATION T ON H .ORGANIZATION_ID = T.ID
LEFT JOIN ASMS_SUBJ_ENFORCE_LAW M ON T.ORG_ID = M.ID
WHERE	 H.ACCOUNT in ('ZF-110100-003','ZF-110101-003','ZF-110000-010','test|_sjzf2','test_sjzf','test_xjzf') );

--- 删除-委托检测任务 - 脏数据
DELETE FROM ALES_ENTRUST_DETECTION WHERE CREATE_BY IN
(
SELECT
    P.CREATE_BY
FROM
    ALES_ENTRUST_DETECTION P
LEFT JOIN SYS_USER H ON P.CREATE_BY = H.ID 
LEFT JOIN SYS_ORGANIZATION T ON H .ORGANIZATION_ID = T.ID
LEFT JOIN ASMS_SUBJ_ENFORCE_LAW M ON T.ORG_ID = M.ID
WHERE H.ACCOUNT in ('ZF-110100-003','ZF-110101-003','ZF-110000-010','test|_sjzf2','test_sjzf','test_xjzf') );

--- 删除-委托检测-检测对象表 -脏数据
DELETE FROM ALES_ENTRUST_DETECTION WHERE CREATE_BY IN
(
SELECT
    P.CREATE_BY
FROM
    ALES_TASK_SAMPLE P
LEFT JOIN SYS_USER H ON P.CREATE_BY = H.ID 
LEFT JOIN SYS_ORGANIZATION T ON H .ORGANIZATION_ID = T.ID
LEFT JOIN ASMS_SUBJ_ENFORCE_LAW M ON T.ORG_ID = M.ID
WHERE	 H.ACCOUNT in ('ZF-110100-003','ZF-110101-003','ZF-110000-010','test|_sjzf2','test_sjzf','test_xjzf') );

--- 删除-委托检测任务-检测对象-抽样单-脏数据
DELETE FROM ALES_TASK_SAMPLE WHERE CREATE_BY IN
(
SELECT
    P.CREATE_BY
FROM
    ALES_TASK_SAMPLE P
LEFT JOIN SYS_USER H ON P.CREATE_BY = H.ID 
LEFT JOIN SYS_ORGANIZATION T ON H .ORGANIZATION_ID = T.ID
LEFT JOIN ASMS_SUBJ_ENFORCE_LAW M ON T.ORG_ID = M.ID
WHERE	 H.ACCOUNT in ('ZF-110100-003','ZF-110101-003','ZF-110000-010','test|_sjzf2','test_sjzf','test_xjzf') );

--- 删除-行政处罚-脏数据
DELETE FROM ALES_TASK_SAMPLE WHERE CREATE_BY IN
(
SELECT
    P.CREATE_BY
FROM
    ALES_PRODUCE_ADMIN_PUNISH P
LEFT JOIN SYS_USER H ON P.CREATE_BY = H.ID 
LEFT JOIN SYS_ORGANIZATION T ON H .ORGANIZATION_ID = T.ID
LEFT JOIN ASMS_SUBJ_ENFORCE_LAW M ON T.ORG_ID = M.ID
WHERE	 H.ACCOUNT in ('ZF-110100-003','ZF-110101-003','ZF-110000-010','test|_sjzf2','test_sjzf','test_xjzf') );

--删除系统用户表 数据
DELETE
FROM
    SYS_USER S
WHERE
    S.ORGANIZATION_ID IN (
        SELECT
            ID
        FROM
            SYS_ORGANIZATION
    ) AND  S.ACCOUNT in ('ZF-110100-003','ZF-110101-003','ZF-110000-010','test|_sjzf2','test_sjzf','test_xjzf') ;

-- 删除系统组织机构与机构信息关系表数据
DELETE
FROM
    SYS_ORGANIZATION
WHERE
    ID IN (
        SELECT
            S.ORGANIZATION_ID
        FROM
            SYS_USER S
        WHERE
S.ACCOUNT in ('ZF-110100-003','ZF-110101-003','ZF-110000-010','test|_sjzf2','test_sjzf','test_xjzf') 
    );

--- 删除机构表数据
DELETE
FROM
    ASMS_SUBJ_ENFORCE_LAW
WHERE
    ID IN (
        SELECT
            S.ORGANIZATION_ID
        FROM
            SYS_USER S
        WHERE
        S.ACCOUNT in ('ZF-110100-003','ZF-110101-003','ZF-110000-010','test|_sjzf2','test_sjzf','test_xjzf') 
    );
--产品表
DELETE 
FROM
    TTS_SCLTXXCJ_PRODUCT_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) );
    
--基地表
DELETE 
FROM
    T_SCLTXXCJ_BASE_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) );
    
--客户表
DELETE 
FROM
    TTS_SCLTXXCJ_CUSTOMER_V2 T1 
WHERE
    T1.ENTITY_ID_CODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) );
    
-- 投诉举报
DELETE 
FROM
    TTS_SCLTXXCJ_COMPLAINT_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) );
    
--优化建议
DELETE 
FROM
    TTS_SCLTXXCJ_PROPOSAL_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) );
    
--通知消息
DELETE 
FROM
    TTS_SCLTXXCJ_NOTIFICATION_V2 T1 
WHERE
    T1.FROM_ID IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) );
    
DELETE 
FROM
    TTS_SCLTXXCJ_CGGL_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) );
    
DELETE 
FROM
    TTS_SCLTXXCJ_CPPCHC_V2 T1 
WHERE
    T1.PRODUCT_PC IN (
SELECT
    T2.PRODUCT_PC 
FROM
    TTS_SCLTXXCJ_SCGL_V2 T2 LEFT JOIN TTS_SCLTXXCJ_REGISTER_V2 T3 ON T2.ENTITY_IDCODE = T3.ENTITY_IDCODE 
WHERE
    T3.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) 
    );
    
    
DELETE 
FROM
    TTS_SCLTXXCJ_LOSSRECORD_V2 T1 
WHERE
    T1.PRODUCTPC IN (
SELECT
    T2.PRODUCT_PC 
FROM
    TTS_SCLTXXCJ_SCGL_V2 T2 LEFT JOIN TTS_SCLTXXCJ_REGISTER_V2 T3 ON T2.ENTITY_IDCODE = T3.ENTITY_IDCODE 
WHERE
    T3.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) 
    );
    
    
DELETE 
FROM
    TTS_SCLTXXCJ_SLA_RECORD_V2 T1 
WHERE
    T1.PRODUCT_PC IN (
SELECT
    T2.PRODUCT_PC 
FROM
    TTS_SCLTXXCJ_SCGL_V2 T2 LEFT JOIN TTS_SCLTXXCJ_REGISTER_V2 T3 ON T2.ENTITY_IDCODE = T3.ENTITY_IDCODE 
WHERE
    T3.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) 
    );
    
    
DELETE 
FROM
    TTS_SCLTXXCJ_XSDJ_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) );
    
DELETE 
FROM
    TTS_SCLTXXCJ_XSDJJL_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) );
    
DELETE 
FROM
    TTS_SCLTXXCJ_XSTH_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) );
    
DELETE 
FROM
    TTS_SCLTXXCJ_SCGL_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) );
    
--用户变更记录
DELETE 
FROM
    TTS_SCLTXXCJ_CHANGERECORD_V2 
WHERE
    ACCOUNT IN ( SELECT ACCOUNT FROM TTS_SCLTXXCJ_REGISTER_V2 WHERE ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) );
    
--账户和子账户
DELETE 
FROM
    TTS_SCLTXXCJ_USER_V2 
WHERE
    ACCOUNT IN ( SELECT ACCOUNT FROM TTS_SCLTXXCJ_REGISTER_V2 WHERE ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' ) );
    
--主体
DELETE 
FROM
    TTS_SCLTXXCJ_REGISTER_V2 
WHERE
    ACCOUNT IN ( 'sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td' );	
--　删除用户帐号
DELETE
FROM
    SYS_USER S
WHERE
S.ACCOUNT in ('sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td');        
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
                    AND DT_AREA_ID LIKE '11%'
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
                    AND DT_AREA_ID LIKE '11%'
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
                    AND DT_AREA_ID LIKE '11%'
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
                    AND DT_AREA_ID LIKE '11%'
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
                    AND DT_AREA_ID LIKE '11%'
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
                            AND DT_AREA_ID LIKE '11%'
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
                            AND DT_AREA_ID LIKE '11%'
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
                    AND DT_AREA_ID LIKE '11%'
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
                AND DT_AREA_ID LIKE '11%'
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
                AND DT_AREA_ID LIKE '11%'
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
                AND DT_AREA_ID LIKE '11%'
                AND DT_TYPE = '检测机构'
    );

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
END;


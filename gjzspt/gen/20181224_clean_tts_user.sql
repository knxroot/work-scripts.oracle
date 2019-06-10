--产品表
DELETE 
FROM
    TTS_SCLTXXCJ_PRODUCT_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) );
    
--基地表
DELETE 
FROM
    T_SCLTXXCJ_BASE_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) );
    
--客户表
DELETE 
FROM
    TTS_SCLTXXCJ_CUSTOMER_V2 T1 
WHERE
    T1.ENTITY_ID_CODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) );
    
-- 投诉举报
DELETE 
FROM
    TTS_SCLTXXCJ_COMPLAINT_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) );
    
--优化建议
DELETE 
FROM
    TTS_SCLTXXCJ_PROPOSAL_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) );
    
--通知消息
DELETE 
FROM
    TTS_SCLTXXCJ_NOTIFICATION_V2 T1 
WHERE
    T1.FROM_ID IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) );
    
DELETE 
FROM
    TTS_SCLTXXCJ_CGGL_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) );
    
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
    T3.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) 
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
    T3.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) 
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
    T3.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) 
    );
    
    
DELETE 
FROM
    TTS_SCLTXXCJ_XSDJ_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) );
    
DELETE 
FROM
    TTS_SCLTXXCJ_XSDJJL_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) );
    
DELETE 
FROM
    TTS_SCLTXXCJ_XSTH_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) );
    
DELETE 
FROM
    TTS_SCLTXXCJ_SCGL_V2 T1 
WHERE
    T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) );
    
--用户变更记录
DELETE 
FROM
    TTS_SCLTXXCJ_CHANGERECORD_V2 
WHERE
    ACCOUNT IN ( SELECT ACCOUNT FROM TTS_SCLTXXCJ_REGISTER_V2 WHERE ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) );
    
--账户和子账户
DELETE 
FROM
    TTS_SCLTXXCJ_USER_V2 
WHERE
    ACCOUNT IN ( SELECT ACCOUNT FROM TTS_SCLTXXCJ_REGISTER_V2 WHERE ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' ) );
    
--主体
DELETE 
FROM
    TTS_SCLTXXCJ_REGISTER_V2 
WHERE
    ACCOUNT IN ( 'zxcv','fuyunping123','yipinrs2013' );	
--　删除用户帐号
DELETE
FROM
    SYS_USER S
WHERE
S.ACCOUNT in ('zxcv','fuyunping123','yipinrs2013');        

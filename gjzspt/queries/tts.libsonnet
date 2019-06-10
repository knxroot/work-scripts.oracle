{
    query_user_by_account(account_name):: |||
        SELECT * 
        FROM
            TTS_SCLTXXCJ_USER_V2 
        WHERE
            ACCOUNT IN ( SELECT ACCOUNT FROM TTS_SCLTXXCJ_REGISTER_V2 WHERE ACCOUNT = '%s' );
    ||| % account_name,

    query_by_enterprise_name(enterprise_name):: |||
        select * from tts_scltxxcj_register_v2 where enterprise_name = '%(ename)s';
    ||| % { ename: enterprise_name },

    query_data_by_accounts(accounts):: |||
        --产品表
        SELECT * 
        FROM
            TTS_SCLTXXCJ_PRODUCT_V2 T1 
        WHERE
            T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
            
        --基地表
        SELECT * 
        FROM
            T_SCLTXXCJ_BASE_V2 T1 
        WHERE
            T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
            
        --客户表
        SELECT * 
        FROM
            TTS_SCLTXXCJ_CUSTOMER_V2 T1 
        WHERE
            T1.ENTITY_ID_CODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
            
        -- 投诉举报
        SELECT * 
        FROM
            TTS_SCLTXXCJ_COMPLAINT_V2 T1 
        WHERE
            T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
            
        --优化建议
        SELECT * 
        FROM
            TTS_SCLTXXCJ_PROPOSAL_V2 T1 
        WHERE
            T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
            
        --通知消息
        SELECT * 
        FROM
            TTS_SCLTXXCJ_NOTIFICATION_V2 T1 
        WHERE
            T1.FROM_ID IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
            
        SELECT * 
        FROM
            TTS_SCLTXXCJ_CGGL_V2 T1 
        WHERE
            T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
            
        SELECT * 
        FROM
            TTS_SCLTXXCJ_CPPCHC_V2 T1 
        WHERE
            T1.PRODUCT_PC IN (
        SELECT
            T2.PRODUCT_PC 
        FROM
            TTS_SCLTXXCJ_SCGL_V2 T2 LEFT JOIN TTS_SCLTXXCJ_REGISTER_V2 T3 ON T2.ENTITY_IDCODE = T3.ENTITY_IDCODE 
        WHERE
            T3.ACCOUNT IN ( %(in_expr)s ) 
            );
            
            
        SELECT * 
        FROM
            TTS_SCLTXXCJ_LOSSRECORD_V2 T1 
        WHERE
            T1.PRODUCTPC IN (
        SELECT
            T2.PRODUCT_PC 
        FROM
            TTS_SCLTXXCJ_SCGL_V2 T2 LEFT JOIN TTS_SCLTXXCJ_REGISTER_V2 T3 ON T2.ENTITY_IDCODE = T3.ENTITY_IDCODE 
        WHERE
            T3.ACCOUNT IN ( %(in_expr)s ) 
            );
            
            
        SELECT * 
        FROM
            TTS_SCLTXXCJ_SLA_RECORD_V2 T1 
        WHERE
            T1.PRODUCT_PC IN (
        SELECT
            T2.PRODUCT_PC 
        FROM
            TTS_SCLTXXCJ_SCGL_V2 T2 LEFT JOIN TTS_SCLTXXCJ_REGISTER_V2 T3 ON T2.ENTITY_IDCODE = T3.ENTITY_IDCODE 
        WHERE
            T3.ACCOUNT IN ( %(in_expr)s ) 
            );
            
            
        SELECT * 
        FROM
            TTS_SCLTXXCJ_XSDJ_V2 T1 
        WHERE
            T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
            
        SELECT * 
        FROM
            TTS_SCLTXXCJ_XSDJJL_V2 T1 
        WHERE
            T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
            
        SELECT * 
        FROM
            TTS_SCLTXXCJ_XSTH_V2 T1 
        WHERE
            T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
            
        SELECT * 
        FROM
            TTS_SCLTXXCJ_SCGL_V2 T1 
        WHERE
            T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
            
        --用户变更记录
        SELECT * 
        FROM
            TTS_SCLTXXCJ_CHANGERECORD_V2 
        WHERE
            ACCOUNT IN ( SELECT ACCOUNT FROM TTS_SCLTXXCJ_REGISTER_V2 WHERE ACCOUNT IN ( %(in_expr)s ) );
            
        --账户和子账户
        SELECT * 
        FROM
            TTS_SCLTXXCJ_USER_V2 
        WHERE
            ACCOUNT IN ( SELECT ACCOUNT FROM TTS_SCLTXXCJ_REGISTER_V2 WHERE ACCOUNT IN ( %(in_expr)s ) );
            
        --主体
        SELECT * 
        FROM
            TTS_SCLTXXCJ_REGISTER_V2 
        WHERE
            ACCOUNT IN ( %(in_expr)s );	    
    ||| % {in_expr :: "'" + std.join("','",accounts) + "'"},

    query_spyb_info():: |||
        SELECT ENTITY_IDCODE, ENTERPRISE_NAME, /* ENTITY_TYPE_NAME, ENTITY_PROPERTY, ENTITY_INDUSTRY_NAME, BUSINESS_LICENCEIMG,*/
        AREA, ADDRESS,
        CONTACT_NAME, CONTACT_EMAIL, CONTACT_PHONE, FAX_NUMBER,
        LEGAL_NAME, LEGAL_IDNUMBER, LEGAL_PHONE
        FROM TTS_SCLTXXCJ_REGISTER_V2;
    |||,

    query_complaints(complaint_title, complaint_cop_name, account_name):: |||
        SELECT *
        FROM TTS_SCLTXXCJ_COMPLAINT_V2
        WHERE COMPLAINT_TITLE='%(complaint_title)s'
        AND COMPLAINT_COP_NAME='%(complaint_cop_name)s'
        AND ENTITY_IDCODE=(
            SELECT ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 where account='%(account_name)s');
    ||| % {complaint_title: complaint_title, complaint_cop_name: complaint_cop_name, account_name: account_name},
}

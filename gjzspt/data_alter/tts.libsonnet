{
    delete_by_area_prefix(area_prefix):: {
        sql: |||
            --产品表           
            DELETE FROM TTS_SCLTXXCJ_PRODUCT_V2 T1 WHERE T1.ENTITY_IDCODE IN (
                SELECT T2.ENTITY_IDCODE
            FROM
                TTS_SCLTXXCJ_REGISTER_V2 T2
            WHERE T2.AREA LIKE '%(area_prefix)s%%'
            );
            
            --基地表 
            DELETE FROM T_SCLTXXCJ_BASE_V2 T1 WHERE T1.ENTITY_IDCODE IN (
                SELECT T2.ENTITY_IDCODE
            FROM
                TTS_SCLTXXCJ_REGISTER_V2 T2
            WHERE T2.AREA LIKE '%(area_prefix)s%%'
            );
            
            
            --客户表
            DELETE FROM TTS_SCLTXXCJ_CUSTOMER_V2 T1 WHERE T1.ENTITY_ID_CODE IN (
                SELECT T2.ENTITY_IDCODE
            FROM
                TTS_SCLTXXCJ_REGISTER_V2 T2
            WHERE T2.AREA LIKE '%(area_prefix)s%%'
            );
            
            -- 投诉举报
            DELETE FROM TTS_SCLTXXCJ_COMPLAINT_V2 T1 WHERE T1.ENTITY_IDCODE IN (
                SELECT T2.ENTITY_IDCODE
            FROM
                TTS_SCLTXXCJ_REGISTER_V2 T2
            WHERE T2.AREA LIKE '%(area_prefix)s%%'
            ); 
            
            --优化建议
            DELETE FROM TTS_SCLTXXCJ_PROPOSAL_V2 T1 WHERE T1.ENTITY_IDCODE IN (
                SELECT T2.ENTITY_IDCODE
            FROM
                TTS_SCLTXXCJ_REGISTER_V2 T2
            WHERE T2.AREA LIKE '%(area_prefix)s%%'
            );
            
            
            --通知消息
            DELETE FROM TTS_SCLTXXCJ_NOTIFICATION_V2 T1 WHERE T1.FROM_ID IN (
                SELECT T2.ENTITY_IDCODE
            FROM
                TTS_SCLTXXCJ_REGISTER_V2 T2
            WHERE T2.AREA LIKE '%(area_prefix)s%%'
            );

            ---------------------------------------------------------------

            --删除TTS_SCLTXXCJ_CGGL_V2
            DELETE FROM TTS_SCLTXXCJ_CGGL_V2 T1 WHERE T1.ENTITY_IDCODE IN (
                SELECT T2.ENTITY_IDCODE
            FROM
                TTS_SCLTXXCJ_REGISTER_V2 T2
            WHERE T2.AREA LIKE '%(area_prefix)s%%'
            );

            --删除TTS_SCLTXXCJ_CPPCHC_V2
            DELETE FROM TTS_SCLTXXCJ_CPPCHC_V2 T1 
            WHERE T1.PRODUCT_PC IN (
                SELECT T2.PRODUCT_PC
            FROM
                TTS_SCLTXXCJ_SCGL_V2 T2 LEFT JOIN TTS_SCLTXXCJ_REGISTER_V2 T3 ON T2.ENTITY_IDCODE = T3.ENTITY_IDCODE
            WHERE T3.AREA LIKE '%(area_prefix)s%%'
            );

            --删除 TTS_SCLTXXCJ_LOSSRECORD_V2
            DELETE FROM TTS_SCLTXXCJ_LOSSRECORD_V2 T1 
            WHERE T1.PRODUCTPC IN (
                SELECT T2.PRODUCT_PC
            FROM
                TTS_SCLTXXCJ_SCGL_V2 T2 LEFT JOIN TTS_SCLTXXCJ_REGISTER_V2 T3 ON T2.ENTITY_IDCODE = T3.ENTITY_IDCODE
            WHERE T3.AREA LIKE '%(area_prefix)s%%'
            );

            --删除 TTS_SCLTXXCJ_SLA_RECORD_V2
            DELETE FROM TTS_SCLTXXCJ_SLA_RECORD_V2 T1 
            WHERE T1.PRODUCT_PC IN (
                SELECT T2.PRODUCT_PC
            FROM
                TTS_SCLTXXCJ_SCGL_V2 T2 LEFT JOIN TTS_SCLTXXCJ_REGISTER_V2 T3 ON T2.ENTITY_IDCODE = T3.ENTITY_IDCODE
            WHERE T3.AREA LIKE '%(area_prefix)s%%'
            );

            --删除 TTS_SCLTXXCJ_XSDJ_V2
            DELETE FROM TTS_SCLTXXCJ_XSDJ_V2 T1 WHERE T1.ENTITY_IDCODE IN (
                SELECT T2.ENTITY_IDCODE
            FROM
                TTS_SCLTXXCJ_REGISTER_V2 T2
            WHERE T2.AREA LIKE '%(area_prefix)s%%'
            );

            --删除 TTS_SCLTXXCJ_XSDJJL_V2
            DELETE FROM TTS_SCLTXXCJ_XSDJJL_V2 T1 WHERE T1.ENTITY_IDCODE IN (
                SELECT T2.ENTITY_IDCODE
            FROM
                TTS_SCLTXXCJ_REGISTER_V2 T2
            WHERE T2.AREA LIKE '%(area_prefix)s%%'
            );

            --删除 TTS_SCLTXXCJ_XSTH_V2
            DELETE FROM TTS_SCLTXXCJ_XSTH_V2 T1 WHERE T1.ENTITY_IDCODE IN (
                SELECT T2.ENTITY_IDCODE
            FROM
                TTS_SCLTXXCJ_REGISTER_V2 T2
            WHERE T2.AREA LIKE '%(area_prefix)s%%'
            );

            --删除 TTS_SCLTXXCJ_SCGL_V2
            DELETE FROM TTS_SCLTXXCJ_SCGL_V2 T1 WHERE T1.ENTITY_IDCODE IN (
                SELECT T2.ENTITY_IDCODE
            FROM
                TTS_SCLTXXCJ_REGISTER_V2 T2
            WHERE T2.AREA LIKE '%(area_prefix)s%%'
            );

            ------------------------------------------

            --用户变更记录
            DELETE FROM TTS_SCLTXXCJ_CHANGERECORD_V2
            WHERE ACCOUNT IN(
            SELECT ACCOUNT FROM TTS_SCLTXXCJ_REGISTER_V2
            WHERE 
            (AREA LIKE '%(area_prefix)s%%')
            AND (ACCOUNT_RESOURCE !='SPYB' OR ACCOUNT_RESOURCE IS NULL)
            AND APPROVE_STATUS !=0
            );

            --账户和子账户
            DELETE FROM TTS_SCLTXXCJ_USER_V2
            WHERE ACCOUNT IN(
            SELECT ACCOUNT FROM TTS_SCLTXXCJ_REGISTER_V2
            WHERE 
            (AREA LIKE '%(area_prefix)s%%')
            AND (ACCOUNT_RESOURCE !='SPYB' OR ACCOUNT_RESOURCE IS NULL)
            AND APPROVE_STATUS !=0
            );

            --主体

            DELETE FROM TTS_SCLTXXCJ_REGISTER_V2
            WHERE 
            (AREA LIKE '%(area_prefix)s%%')
            AND (ACCOUNT_RESOURCE !='SPYB' OR ACCOUNT_RESOURCE IS NULL)
            AND APPROVE_STATUS !=0
            ;
        ||| % {area_prefix: area_prefix},
    },

    delete_all_data_by_accounts(accounts):: {
        in_expr :: "'" + std.join("','",accounts) + "'",
        sql: |||
            --产品表
            DELETE 
            FROM
                TTS_SCLTXXCJ_PRODUCT_V2 T1 
            WHERE
                T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
                
            --基地表
            DELETE 
            FROM
                T_SCLTXXCJ_BASE_V2 T1 
            WHERE
                T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
                
            --客户表
            DELETE 
            FROM
                TTS_SCLTXXCJ_CUSTOMER_V2 T1 
            WHERE
                T1.ENTITY_ID_CODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
                
            -- 投诉举报
            DELETE 
            FROM
                TTS_SCLTXXCJ_COMPLAINT_V2 T1 
            WHERE
                T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
                
            --优化建议
            DELETE 
            FROM
                TTS_SCLTXXCJ_PROPOSAL_V2 T1 
            WHERE
                T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
                
            --通知消息
            DELETE 
            FROM
                TTS_SCLTXXCJ_NOTIFICATION_V2 T1 
            WHERE
                T1.FROM_ID IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
                
            DELETE 
            FROM
                TTS_SCLTXXCJ_CGGL_V2 T1 
            WHERE
                T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
                
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
                T3.ACCOUNT IN ( %(in_expr)s ) 
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
                T3.ACCOUNT IN ( %(in_expr)s ) 
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
                T3.ACCOUNT IN ( %(in_expr)s ) 
                );
                
                
            DELETE 
            FROM
                TTS_SCLTXXCJ_XSDJ_V2 T1 
            WHERE
                T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
                
            DELETE 
            FROM
                TTS_SCLTXXCJ_XSDJJL_V2 T1 
            WHERE
                T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
                
            DELETE 
            FROM
                TTS_SCLTXXCJ_XSTH_V2 T1 
            WHERE
                T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
                
            DELETE 
            FROM
                TTS_SCLTXXCJ_SCGL_V2 T1 
            WHERE
                T1.ENTITY_IDCODE IN ( SELECT T2.ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 T2 WHERE T2.ACCOUNT IN ( %(in_expr)s ) );
                
            --用户变更记录
            DELETE 
            FROM
                TTS_SCLTXXCJ_CHANGERECORD_V2 
            WHERE
                ACCOUNT IN ( SELECT ACCOUNT FROM TTS_SCLTXXCJ_REGISTER_V2 WHERE ACCOUNT IN ( %(in_expr)s ) );
                
            --账户和子账户
            DELETE 
            FROM
                TTS_SCLTXXCJ_USER_V2 
            WHERE
                ACCOUNT IN ( SELECT ACCOUNT FROM TTS_SCLTXXCJ_REGISTER_V2 WHERE ACCOUNT IN ( %(in_expr)s ) );
                
            --主体
            DELETE 
            FROM
                TTS_SCLTXXCJ_REGISTER_V2 
            WHERE
                ACCOUNT IN ( %(in_expr)s );	
        ||| % self
    },

    update_by_account(account,scale_name):: {
        sql: |||
            UPDATE TTS_SCLTXXCJ_REGISTER_V2
            SET ENTITY_SCALE_NAME = '%(scale_name)s'
            WHERE
                ACCOUNT = '%(account)s'        
        ||| % { account: account, scale_name: scale_name }
    },

    delete_complaints(complaint_title, complaint_cop_name, account_name):: |||
        DELETE FROM (
            SELECT *
            FROM TTS_SCLTXXCJ_COMPLAINT_V2
            WHERE COMPLAINT_TITLE='%(complaint_title)s'
            AND COMPLAINT_COP_NAME='%(complaint_cop_name)s'
            AND ENTITY_IDCODE=(
                SELECT ENTITY_IDCODE FROM TTS_SCLTXXCJ_REGISTER_V2 where account='%(account_name)s')
         );
    ||| % {complaint_title: complaint_title, complaint_cop_name: complaint_cop_name, account_name: account_name},
}

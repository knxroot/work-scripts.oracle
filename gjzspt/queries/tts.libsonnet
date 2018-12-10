{
    query_user_by_account(account_name):: |||
        SELECT * 
        FROM
            TTS_SCLTXXCJ_USER_V2 
        WHERE
            ACCOUNT IN ( SELECT ACCOUNT FROM TTS_SCLTXXCJ_REGISTER_V2 WHERE ACCOUNT = '%s' );
    ||| % account_name,
}

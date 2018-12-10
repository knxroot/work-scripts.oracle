{
    query_user_by_account(account_name):: |||
        select * from sys_user where account like '%s';
    ||| % account_name,
}

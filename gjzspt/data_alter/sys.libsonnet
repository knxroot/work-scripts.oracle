{
    delete_user_by_userids(user_ids):: {
        in_expr :: "'" + std.join("','",user_ids) + "'",
        sql: |||
            --　删除用户帐号
            DELETE
            FROM
                SYS_USER S
            WHERE
            S.ID in (%(in_expr)s);        
        ||| % self
    },
    delete_user_by_accounts(accounts):: {
        in_expr :: "'" + std.join("','",accounts) + "'",
        sql: |||
            --　删除用户帐号
            DELETE
            FROM
                SYS_USER S
            WHERE
            S.ACCOUNT in (%(in_expr)s);        
        ||| % self
    },
    update_region_code(region_code, new_region_code):: {
        sql: |||
            update sys_region set region_code='%(new_region_code)s' where region_code = '%(region_code)s';
        ||| % {region_code: region_code, new_region_code: new_region_code},
    },
    update_county_to_region(county_name, region_name,new_region_code, parentid):: {
        sql: |||
            update sys_region set region_name='%(region_name)s',region_code='%(new_region_code)s',parent_id='%(parentid)s' where region_name = '%(county_name)s';
        ||| % {county_name: county_name, region_name: region_name, new_region_code: new_region_code, parentid: parentid},
    },
}

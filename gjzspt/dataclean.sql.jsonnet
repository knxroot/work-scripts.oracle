local asms=import 'data_alter/asms.libsonnet';
local ales=import 'data_alter/ales.libsonnet';
local tts=import 'data_alter/tts.libsonnet';
local sys=import 'data_alter/sys.libsonnet';
local ads=import 'data_alter/ads.libsonnet';
local input=import 'input.jsonnet';

local alesq=import 'queries/ales.libsonnet';

local trans_wrap(sqls)=|||
        SET AUTOCOMMIT OFF;

        BEGIN
            %s
            COMMIT;
        EXCEPTION
            WHEN OTHERS THEN
                ROLLBACK;
        END;
    ||| % sqls;
{
    /*
    clean_asms_orphan_users:: asms.clean_orphan_users(['ASMS']),
    clean_asms_dirty_account:: asms.clean_asms_dirty_account(['陕西省级监管机构','陕西市级监管机构','河南省导入测试监管机构']),
    */

    /*
    "20181130_clean_ales_data_by_userid.sql": ales.delete_all_data_by_userids(['bbfbdb9b7f41428086c3183df2f4991e6876c060fb644457928b51190f70e810','728d3327bb7649d2aeaefa615a1b6b8b3776db36d6bd4f0d8162b81d6eca0cd7',
    '9a69edf7356e4eeab33e67b6d991cd81b085536f791f4515bb4487645f92cacb']).sql,

    "20181130_clean_user.sql": sys.delete_user_by_userids(['bbfbdb9b7f41428086c3183df2f4991e6876c060fb644457928b51190f70e810']).sql,

    "20181130_account_with_duplicate_users.sql": qsys.query_user_by_account("ZF-110000-010"),
    */

    /*
    "20181203_clean_user.sql": asms.clean_asms_dirty_account(['广西壮族自治区农业厅','广西壮族自治区农业厅畜牧']).sql+ asms.clean_asms_sv_change(['广西壮族自治区农业厅','广西壮族自治区农业厅畜牧']).sql,
    */

    /*
    "20181206_clean_tts_user.sql" : tts.delete_all_data_by_accounts(['taishanshihaoyexiehui']).sql,
    */

    /*
    "20181210_clean_tts_user.sql" : tts.delete_all_data_by_accounts(['yunhongjituan']).sql
                                        + sys.delete_user_by_accounts(['yunhongjituan']).sql, 
    "20181210_ads_org_rename.sql" : ads.update_by_name('普洱市农业环境保护监测站','new_name').sql,
    */

    /*
    "20181217_clean_xinjiang_account.sql": asms.clean_all_data_by_svnames(['新疆兵团农业局']).sql,
    "20181217_clean_chongqing_account.sql": asms.clean_all_data_by_svnames(['潼南区农业委员会']).sql,
    */

    /*
    "20181220_chongqing_sys_region.sql": std.join('',
        [
         sys.update_region_code(region_code,std.strReplace(region_code,"5002","5001")).sql
         for region_code in std.setDiff(
             std.set([std.toString(x) for x in std.range(500228,500243)]),
             std.set(["500239"])
             )   
         ]+
        [sys.update_county_to_region("梁平县","梁平区","500155","500100").sql] +
        [sys.update_county_to_region("武隆县","武隆区","500156","500100").sql] 
    ),

    "20181224_clean_tts_user.sql" : 
        tts.delete_all_data_by_accounts(['zxcv','fuyunping123','yipinrs2013']).sql +
        sys.delete_user_by_accounts(['zxcv','fuyunping123','yipinrs2013']).sql,
        // +
        // asms.clean_all_data_by_svnames(['普洱三国庄园茶业有限责任公司','江城中澳农科科技发展有限公司','大道无为']).sql, 

    "20181225_jingshanshi_sys_region.sql": 
        sys.update_county_to_region("京山县","京山市","420882",null).sql,

    "20181227_shengji_asms_add_roles.sql":
        asms.add_role('JG-410000-001','监管机构管理员渔业角色','渔业').sql +
        asms.add_role('JG-320000-002','监管机构管理员畜牧业角色','畜牧业').sql,
    
    "20181227_guangdong_shixian_asms_add_roles.sql":
        asms.add_role('JG-440100-007','监管机构管理员渔业角色','渔业').sql+
        asms.add_role('JG-440704-001','监管机构管理员渔业角色','渔业').sql+
        asms.add_role('JG-440783-001','监管机构管理员渔业角色','渔业').sql+
        asms.add_role('JG-440785-002','监管机构管理员渔业角色','渔业').sql+
        asms.add_role('JG-441400-001','监管机构管理员渔业角色','渔业').sql+

        asms.add_role('JG-440704-001','监管机构管理员畜牧业角色','畜牧业').sql+
        asms.add_role('JG-440705-001','监管机构管理员畜牧业角色','畜牧业').sql+
        asms.add_role('JG-440781-001','监管机构管理员畜牧业角色','畜牧业').sql+
        asms.add_role('JG-440783-001','监管机构管理员畜牧业角色','畜牧业').sql+
        asms.add_role('JG-440784-001','监管机构管理员畜牧业角色','畜牧业').sql,

    "20181227_xinjiang_bingtuanzongbu_data.sql":
        trans_wrap(
            sys.add_region('兵团总部','新疆生产建设兵团','661500').sql+
            sys.add_region('兵团总部','兵团总部','661501').sql
        ),          
    */

    local beijing_test_data = {
        sv_names: ["海淀区监管","北京县级监管机构一测试","北京市级监管机构一测试","北京省级监管机构一测试"],
        ales_user_accounts: ['ZF-110100-003','ZF-110101-003','ZF-110000-010','test|_sjzf2','test_sjzf','test_xjzf'],
        tts_user_accounts: ['sqwertyuiop','user','test_bjqy3','haixinhuaxia2008','cc_123','bjtest_12','test_bjhzs','test_bjqy','aaaa','liangqiujidan','wangtshg','bjcy','zywy','45252419531015431X','rc_td',],
        bj_area_prefix: '11',
    },

    "20181227_beijing_test_data.sql":
        trans_wrap(
            asms.clean_all_data_by_svnames(beijing_test_data.sv_names).sql+
            ales.delete_all_data_by_accounts(beijing_test_data.ales_user_accounts).sql+
            //tts
            tts.delete_all_data_by_accounts(beijing_test_data.tts_user_accounts).sql+
            sys.delete_user_by_accounts(beijing_test_data.tts_user_accounts).sql+
            //ads
            ads.delete_by_area_prefix(beijing_test_data.bj_area_prefix).sql
        ),
      
    // "query_20181227_beijing_test_data.sql":
    //     alesq.query_data_by_accounts(input.beijing_test_data.ales_user_accounts).sql,
}
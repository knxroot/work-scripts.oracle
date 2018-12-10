local asms=import 'data_alter/asms.libsonnet';
local ales=import 'data_alter/ales.libsonnet';
local tts=import 'data_alter/tts.libsonnet';
local sys=import 'data_alter/sys.libsonnet';
local qsys=import 'queries/sys.libsonnet';
local qtts=import 'queries/tts.libsonnet';

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

    "20181210_clean_tts_user.sql" : tts.delete_all_data_by_accounts(['yunhongjituan']).sql+ sys.delete_user_by_accounts(['yunhongjituan']).sql, 
}

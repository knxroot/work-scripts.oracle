local qsys=import 'queries/sys.libsonnet';
local qtts=import 'queries/tts.libsonnet';
local qads=import 'queries/ads.libsonnet';
local qasms=import 'queries/asms.libsonnet';

{
    /* */
    "sys":: qsys.query_user_by_account(['taishanshihaoyexiehui']),
    "tts":: qsys.query_user_by_account(['taishanshihaoyexiehui'])+qtts.query_user_by_account('taishanshihaoyexiehui'),

    "ads":: qads.query_user_by_accounts(['云南省普洱市检测机构','普洱市农业环境保护监测站']).sql+
           qads.query_user_match_account('普洱').sql,
    
    "asms":: qasms.query_supervise(['lvguangping']),

    "tts0530.sql":: qtts.query_data_by_accounts(["JCXXCGSZYHZS1"]),
    "20190531": qsys.query_user_info_by_accounts(["JG-64120000-006"],[]),
}

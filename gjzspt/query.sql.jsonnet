local qsys=import 'queries/sys.libsonnet';
local qtts=import 'queries/tts.libsonnet';
local qads=import 'queries/ads.libsonnet';

{
    /* */
    "sys": qsys.query_user_by_account(['taishanshihaoyexiehui']),
    "tts": qsys.query_user_by_account(['taishanshihaoyexiehui'])+qtts.query_user_by_account('taishanshihaoyexiehui'),

    "ads": qads.query_user_by_accounts(['云南省普洱市检测机构','普洱市农业环境保护监测站']).sql+
           qads.query_user_match_account('普洱').sql,
}

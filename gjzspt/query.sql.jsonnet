local qsys=import 'queries/sys.libsonnet';
local qtts=import 'queries/tts.libsonnet';

{
    /* */
    "sys": qsys.query_user_by_account(['taishanshihaoyexiehui']),
    "tts": qsys.query_user_by_account(['taishanshihaoyexiehui'])+qtts.query_user_by_account('taishanshihaoyexiehui'),

}

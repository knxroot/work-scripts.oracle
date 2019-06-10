local ads = import 'data_alter/ads.libsonnet';
local ales = import 'data_alter/ales.libsonnet';
local asms = import 'data_alter/asms.libsonnet';
local sys = import 'data_alter/sys.libsonnet';
local tts = import 'data_alter/tts.libsonnet';
local input = import 'input.jsonnet';

local alesq = import 'queries/ales.libsonnet';
local asmsq = import 'queries/asms.libsonnet';
local sysq = import 'queries/sys.libsonnet';

local trans_wrap(sqls) = |||
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

  local shengji=[
      {
          account: 'JG-410000-001',
          role_name: '监管机构管理员渔业角色',
          industry_name: '渔业',
      },
      {
          account: 'JG-320000-002',
          role_name: '监管机构管理员畜牧业角色',
          industry_name: '畜牧业',
      },
  ],

  // local guangdong_shengshi={
  //     '监管机构管理员渔业角色': {
  //         accounts:[
  //         'JG-440100-007',
  //         'JG-440704-001',
  //         'JG-440783-001',
  //         'JG-440785-002',
  //         'JG-441400-001',
  //         ],
  //         industry: "渔业",
  //     },
  //     '监管机构管理员畜牧业角色': {
  //         accounts: [
  //         'JG-440704-001',
  //         'JG-440705-001',
  //         'JG-440781-001',
  //         'JG-440783-001',
  //         'JG-440784-001',
  //         ],
  //         industry: "畜牧业",
  //     },
  // },

  // "20181227_shengji_asms_add_roles.sql":
  //     asms.add_role('JG-410000-001','监管机构管理员渔业角色','渔业').sql +
  //     asms.add_role('JG-320000-002','监管机构管理员畜牧业角色','畜牧业').sql,
  "20181227_shengji_asms_add_roles.sql":
      std.join('',
          [
              asms.add_role(d.account,d.role_name,d.industry_name).sql
              for d in shengji
          ]
      )

  local guangdong_shengshi={
      local yuye_accounts=[
          'JG-440100-007',
          'JG-440704-001',
          'JG-440783-001',
          'JG-440785-002',
          'JG-441400-001',
          ],
      local xumu_accounts=[
          'JG-440704-001',
          'JG-440705-001',
          'JG-440781-001',
          'JG-440783-001',
          'JG-440784-001',
      ],
      data:[
          {
              account: acc,
              role_name: if std.setMember(acc,yuye_accounts) then '监管机构管理员渔业角色' else if std.setMember(acc,xumu_accounts) then '监管机构管理员畜牧业角色',
              industry_name: if std.setMember(acc,yuye_accounts) then '渔业' else if std.setMember(acc,xumu_accounts) then '畜牧业',
          } for acc in yuye_accounts + xumu_accounts
      ],
  },
  "20181227_guangdong_shixian_asms_add_roles.sql":
      std.join('',
          [
              asms.add_role(d.account,d.role_name,d.industry_name).sql
              for d in guangdong_shengshi.data
          ]
      ),

  "20181227_xinjiang_bingtuanzongbu_data.sql":
      trans_wrap(
          sys.add_region('兵团总部','新疆生产建设兵团','661500').sql+
          sys.add_region('兵团总部','兵团总部','661501').sql
      ),

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
  */

  /*
  local shanghai_beijing_sys_region={
      accounts: {
      "上海市农业委员会": "JG-310000-001",
      "上海市农产品质量安全中心": "JG-310100-001",
      "上海": "JG-110000-001",
      "上海市农": "JG-110100-001",
      },
  },
  "20181228_shanghai_beijing_sys_region.sql": std.join('',
      [sys.update_county_to_region("崇明县","崇明区","310151","310100").sql] +
      [sys.update_county_to_region("密云县","密云区","110118","110100").sql] +
      [sys.update_county_to_region("延庆县","延庆区","110119","110100").sql],
  ),
  */

  /*
  "20190110_delete_tts_data.sql":
      trans_wrap(
          tts.delete_all_data_by_accounts(["zhaoyang8888"]).sql
      ),

  local neimeng_xinganmeng_qixian={
      local yuye_accounts=[
          'JG-152201-001',
          'JG-152202-001',
          'JG-152221-001',
          'JG-152222-001',
          'JG-152223-001',
          'JG-152224-001',
          ],
      local xumu_accounts=[
      ],
      data:[
          {
              account: acc,
              role_name: if std.setMember(acc,yuye_accounts) then '监管机构管理员渔业角色' else if std.setMember(acc,xumu_accounts) then '监管机构管理员畜牧业角色',
              industry_name: if std.setMember(acc,yuye_accounts) then '渔业' else if std.setMember(acc,xumu_accounts) then '畜牧业',
          } for acc in yuye_accounts + xumu_accounts
      ],
  },
  "20190110_neimeng_xinganmeng_qixian_asms_add_roles.sql":
      trans_wrap(
          std.join('',
              [
                  asms.add_role(d.account,d.role_name,d.industry_name).sql
                  for d in neimeng_xinganmeng_qixian.data
              ]
          )
      ),
  */

  /*
  "20190111_yunnan_changningxian_delete_account.sql" :
      trans_wrap(
          asms.clean_all_data_by_svnames(["昌宁县农业局"]).sql
      ),

  local guangdong_jieyang_accounts={
      local zhongzhi_accounts=std.set([
          'JG-445202-001',
          ]),
      local yuye_accounts=std.set([
          ]),
      local xumu_accounts=std.set([
          'JG-445200-001',
          'JG-445224-001',
          'JG-445222-001',
          'JG-445281-001',
          'JG-445203-001',
      ]),
      data:[
          {
              account: acc,
              role_name: if std.setMember(acc,yuye_accounts) then '监管机构管理员渔业角色' else if std.setMember(acc,xumu_accounts) then '监管机构管理员畜牧业角色' else if
              std.setMember(acc,zhongzhi_accounts) then '监管机构管理员种植业角色',

              industry_name: if std.setMember(acc,yuye_accounts) then '渔业' else if std.setMember(acc,xumu_accounts) then '畜牧业' else if
              std.setMember(acc,zhongzhi_accounts) then '种植业',
          } for acc in zhongzhi_accounts + xumu_accounts + yuye_accounts
      ],
      accounts: zhongzhi_accounts + xumu_accounts + yuye_accounts,
  },

  "20190111_guangdong_jieyang_asms_add_roles.sql":
      trans_wrap(
          std.join('',
              [
                  asm.add_role(d.account,d.role_name,d.industry_name).sql
                  for d in guangdong_jieyang_accounts.data
              ]
          )
      ),

  "query":
      std.join("",[
          asmsq.query_supervise(guangdong_jieyang_accounts.accounts),
          sysq.query_user_roles(guangdong_jieyang_accounts.accounts),
      ]),
  */

  /*
  //福建三明市的账号增加渔业行业权限
  local fujian_sanming_accounts={
      local zhongzhi_accounts=std.set([
          ]),
      local yuye_accounts=std.set([
          'JG-350400-001',
          'JG-350402-001',
          'JG-350403-001',
          'JG-350481-001',
          'JG-350421-001',
          'JG-350423-001',
          'JG-350424-001',
          'JG-350425-001',
          'JG-350426-001',
          'JG-350427-001',
          'JG-350428-001',
          'JG-350429-001',
          'JG-350430-001',
          ]),
      local xumu_accounts=std.set([
      ]),
      data:[
          {
              account: acc,
              role_name: if std.setMember(acc,yuye_accounts) then '监管机构管理员渔业角色' else if std.setMember(acc,xumu_accounts) then '监管机构管理员畜牧业角色' else if
              std.setMember(acc,zhongzhi_accounts) then '监管机构管理员种植业角色',

              industry_name: if std.setMember(acc,yuye_accounts) then '渔业' else if std.setMember(acc,xumu_accounts) then '畜牧业' else if
              std.setMember(acc,zhongzhi_accounts) then '种植业',
          } for acc in zhongzhi_accounts + xumu_accounts + yuye_accounts
      ],
      accounts: zhongzhi_accounts + xumu_accounts + yuye_accounts,
  },

  "20190111_fujian_sanming_asms_add_roles.sql":
      trans_wrap(
          std.join('',
              [
                  asms.add_role(d.account,d.role_name,d.industry_name).sql
                  for d in fujian_sanming_accounts.data
              ]
          )
      ),

  //福建
  local fujian_accounts={
      local zhongzhi_accounts=std.set([
          ]),
      local yuye_accounts=std.set([
          'JG-350305-001',
          ]),
      local xumu_accounts=std.set([
          'JG-350000-002'
      ]),
      data:[
          {
              account: acc,
              role_name: if std.setMember(acc,yuye_accounts) then '监管机构管理员渔业角色' else if std.setMember(acc,xumu_accounts) then '监管机构管理员畜牧业角色' else if
              std.setMember(acc,zhongzhi_accounts) then '监管机构管理员种植业角色',

              industry_name: if std.setMember(acc,yuye_accounts) then '渔业' else if std.setMember(acc,xumu_accounts) then '畜牧业' else if
              std.setMember(acc,zhongzhi_accounts) then '种植业',
          } for acc in zhongzhi_accounts + xumu_accounts + yuye_accounts
      ],
      accounts: zhongzhi_accounts + xumu_accounts + yuye_accounts,
  },

  "20190114_fujian_asms_add_roles.sql":
      trans_wrap(
          std.join('',
              [
                  asms.add_role(d.account,d.role_name,d.industry_name).sql
                  for d in fujian_accounts.data
              ]
          )
      ),

  "20190122_delete_asms_account.sql":
      trans_wrap(
          asms.clean_all_data_by_svnames(["说实话"]).sql
      ),
  */

  /*
  "20190306_clean_tts_user.sql" : tts.delete_all_data_by_accounts(['yayuan123456','hbl198008']).sql,

  "20190320_tts_modify_user.sql": trans_wrap(
      tts.update_by_account('ZEH68167','合作社').sql
  ),

  "20190320_clean_ales_ads_user.sql": trans_wrap(
      ales.delete_dummy_org('云南省执法机构').sql  +  ads.delete_dummy_org('云南省检测机构').sql
  ),kjjj

  "20190401_clean_tts_and_asms_user.sql" : trans_wrap(tts.delete_all_data_by_accounts(['fusiontest']).sql + asms.clean_all_data_by_svnames(['荔波县农村工作局']).sql),

  "20190408_clean_asms_user.sql" : trans_wrap(asms.clean_all_data_by_svnames(['宁波市海曙区农业农村局']).sql),

  "20190415_delete_ads_task.sql" : trans_wrap(ads.delete_task_by_name('关于做好2019年农产品质量安全市级例行监测（风险监测）工作的通知').sql),
  */

  /*
  "20190417_fix_ads_task.sql" : |||
      INSERT
      INTO ADS_MONITOR_TASK
      (
          ID,
          TASK_NAME,
          MONITOR_CLASS,
          RELEASE_UNIT,
          CHECK_MODEL,
          YEAR,
          BATCH,
          SEPARATION,
          START_TIME,
          END_TIME,
          DEADLINE,
          ATTACHMENT,
          ATTACHMENTCODE,
          "COMMENT",
          PUBLISH_STATUS,
          INDUSTRY,
          JUDGE_STANDARD,
          SAMPLE_LINK,
          CREATE_BY,
          CREATE_TIME,
          UPDATE_BY,
          UPDATE_TIME,
          DEL_FLAG,
          RESERVED_FIELD1,
          RESERVED_FIELD2,
          TASK_SOURCE,
          NUMBERS,
          LEVE,
          ATTACHMENT_ADDRESS,
          ABOLISH,
          ORGAN_ID,
          SUP_ID,
          INDUSTRY_ID,
          CREATE_ORG_REGION_ID,
          LEVEL_ENUM
      )
      VALUES
      (
          '03df5ab32561489e98074be36889a12d',
          '关于做好2019年农产品质量安全市级例行监测（风险监测）工作的通知',
          '例行监测',
          '黄山市农业农村局',
          NULL,
          '2019',
          '1',
          0,
          to_timestamp('2019-04-04 00:00:00','YYYY-MM-DD HH24:MI:SS'),
          to_timestamp('2019-06-20 00:00:00','YYYY-MM-DD HH24:MI:SS'),
          NULL,
          '黄山市农业农村局关于做好2019年农产品质量安全市级例行监测（风险监测）工作的通知.pdf',
          '黄农函〔2019〕72号',
          NULL,
          0,
          NULL,
          NULL,
          NULL,
          '7f2eb9f4cb3142d289221cd90d962481d6e2f6ec4e294e07819cc9071a38c888',
          to_timestamp('2019-04-10 07:54:43','YYYY-MM-DD HH24:MI:SS'),
          NULL,
          NULL,
          'N',
          NULL,
          NULL,
          'SDPTASK',
          NULL,
          NULL,
          '//10.2.12.217/dfs/group3/M00/00/64/CgIMvlysPz2AaqouAAU5xEaOcDw01..pdf',
          NULL,
          '9f654cf7598644e9adce11eceb2fbd95eb654a0c3b6849c088471661894345b7',
          '7c0a963372724459ad065e62f364376b39c92b3d109848e8afff0050f577f523',
          NULL,
          '341002',
          '2 '
      );
      DELETE
      FROM ASMS_ROUTINE_MONITOR
      WHERE RM_NAME = '关于做好2019年农产品质量安全市级例行监测（风险监测）工作的通知'
      AND RM_STATE  = '0';
  |||,

  "20190422_tts_delete_account.sql": trans_wrap(tts.delete_all_data_by_accounts(['xiaoming']).sql),

  "20190424_sys_fix_agri_product.sql": |||
      DELETE FROM "SYS_ARGI_PRODUCT" WHERE PRODUCT_CODE = '—';
  |||,
  */

  '20190426_tts_data_fix.sql': |||
    UPDATE TTS_SCLTXXCJ_REGISTER_V2
    SET INFO_UNIQUE = '93310116361670517F',
    CREDIT_CODE = '93310116361670517F',
    USER_IDCODE = '2.93310116361670517F.00001',
    ENTITY_IDCODE = '2.93310116361670517F.00000'
    WHERE
        ACCOUNT = 'yhh_13127752098';

    --修改完主体等级表之后,相关条件需要进行改变
    UPDATE TTS_SCLTXXCJ_USER_V2
    SET USER_IDCODE = '2.93310116361670517F.00001',
    ENTITY_IDCODE = '2.93310116361670517F.00000'
    WHERE
        ACCOUNT = 'yhh_13127752098';

    --修改完主体等级表之后,相关条件需要进行改变
    UPDATE TTS_SCLTXXCJ_CHANGERECORD_V2
    SET INFO_UNIQUE = '93310116361670517F',
    USER_IDCODE = '2.93310116361670517F.00001',
    ENTITY_IDCODE = '2.93310116361670517F.00000'
    WHERE
        ACCOUNT = 'yhh_13127752098';
  |||,

  '20190523_sys_delete_duplicated_accounts.sql': sys.delete_accounts_with_same_loginname(),
  '20190528_tts_delete_account_by_shenfenzheng': |||
    delete FROM TTS_SCLTXXCJ_CHANGERECORD_V2 WHERE LEGAL_IDNUMBER='511126197704092612';
    DELETE FROM TTS_SCLTXXCJ_REGISTER_V2 WHERE LEGAL_IDNUMBER='511126197704092612';
  |||,

  '20190528_tts_delete_account_by_account.sql': trans_wrap(tts.delete_all_data_by_accounts(['PZWH123456']).sql),

  /*
  "20190529_reset_account_initial_password.sql": sys.reset_user_initial_password('yangguang','12345678'),
  update sys_user set del_flag='N' where account='yangguang';
  */

  "20190530_tts_delete_account.sql": trans_wrap(
      tts.delete_all_data_by_accounts(["JCXXCGSZYHZS1"]).sql
   ),

  "20190531_delete_related_account.sql": trans_wrap(
      asms.clean_asms_dirty_account(["波密县农业农村局"]).sql+
      ales.delete_all_data_by_accounts(["ZF-654200-001"],).sql+
      tts.delete_all_data_by_accounts(["chenshiwu28"],).sql+
      ads.delete_all_by_names(["塔城市农产品质量安全检验检测中心"])
  ),

  "20190603_delete_tts_complaints.sql": tts.delete_complaints("北京","四川省文君茶叶有限公司","wjc"),

  "20190603_delete_ales_org_by_sv_name.sql": trans_wrap(
      ales.delete_dummy_org("塔城市农业行政执法大队").sql),

    //赤水市元厚龙眼农民专业合作社	  gylc520381	qwertyuiop123
    //企业名称：金沙县四季新农业专业合作社，账号：yuan18786492172
  "20190604_delete_tts_account.sql": trans_wrap(
      tts.delete_all_data_by_accounts(["yuan18786492172"]).sql+
      tts.delete_all_data_by_accounts(["gylc520381"]).sql),

  "20190605_delete_tts_account.sql": trans_wrap(
      tts.delete_all_data_by_accounts(["ynqjmlhs"]).sql),
}

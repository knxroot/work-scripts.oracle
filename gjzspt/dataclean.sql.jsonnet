local sqls=import 'dataclean_templates_sql.libsonnet';

{
    clean_asms_orphan_users: sqls.clean_orphan_users(['ASMS']),
    clean_asms_dirty_account: sqls.clean_asms_dirty_account(['陕西省级监管机构','陕西市级监管机构','河南省导入测试监管机构']),
}
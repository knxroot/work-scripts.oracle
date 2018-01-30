truncate table t_dgap_alert_log;
truncate table t_dgap_alert_receipt;
-- truncate table t_dgap_alert_config;
SELECT * FROM USER_CONSTRAINTS WHERE TABLE_NAME = 't_dgap_alert_config';

truncate table t_dgap_ws_log;
truncate table t_dgap_ws_daily_stat;
truncate table t_dgap_ws_error_log;

truncate table t_dgap_role_resource;
truncate table t_dgap_resource_application;
--truncate table t_dgap_resource;
--truncate table t_dgap_resource_directory;

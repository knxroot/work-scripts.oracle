--更改文件名长度
ALTER TABLE "TTS_SCLTXXCJ_REGISTER_MEDIA_V2"
MODIFY ( "RESOURCE_NAME" VARCHAR2(512 CHAR) ) ;
--检测系统 修改上传附件名称长度为1000
alter table ads_file modify (FILE_NAME varchar2(1000 char));

alter table ADS_MONITOR_SAMPLE modify (FILE_NAME varchar2(1000 char));
alter table ALES_DAILY_ENFORCE_LAW modify (SCENE_PICTURE_NAMES varchar2(512 char));

alter table ALES_TASK_SAMPLE modify (ATTACHMENT_NAMES varchar2(512 char));

alter table ALES_PRODUCE_ADMIN_PUNISH modify (PUNISH_FILES_NAME varchar2(512 char));
-- 更改附件名称字段长度
ALTER TABLE ASMS_ROUTINE_MONITOR MODIFY (RM_FILE_NAME VARCHAR2(512 char));
ALTER TABLE ASMS_SPECIAL_MONITOR MODIFY (SM_FILE_NAME VARCHAR2(512 char));
ALTER TABLE ASMS_CHECK_TASK MODIFY (ATTACHMENT_NAME VARCHAR2(512 char));
ALTER TABLE ASMS_EMERGENCY_TASK MODIFY (FILES_NAME VARCHAR2(512 char));
ALTER TABLE ASMS_INSPECTION_TASK MODIFY (ATTACHMENT_NAME VARCHAR2(512 char));
ALTER TABLE ASMS_BASE_INSPECTION MODIFY (VIDEO_NAME VARCHAR2(512 char));
ALTER TABLE ASMS_BASE_INSPECTION MODIFY (HEAD_SIGN_FILE_NAME VARCHAR2(512 char));
ALTER TABLE ASMS_BASE_INSPECTION MODIFY (INSPECTION_IMAGES_NAME VARCHAR2(2048 char));
ALTER TABLE ASMS_SUBJ_ENT_TEMP MODIFY (ATTACHMENT_NAME VARCHAR2(512 char));
m4_changequote(`[',`]')
m4_define([clean_orphan_user],[UPDATE SYS_USER 
SET DEL_FLAG = 'Y' 
WHERE
	ID IN (
SELECT
	SYS_USER.ID 
FROM
	SYS_USER,
	SYS_ORGANIZATION
	LEFT JOIN ASMS_SUBJ_SUPERVISE ON ASMS_SUBJ_SUPERVISE.ID = SYS_ORGANIZATION.ORG_ID 
WHERE
	ASMS_SUBJ_SUPERVISE.ID IS NULL 
	AND SYS_USER.ORGANIZATION_ID = SYS_ORGANIZATION.ID 
	AND SYS_ORGANIZATION.ORG_TYPE IN ($1)
	);])
dnl start to call macros
clean_orphan_user([asms])
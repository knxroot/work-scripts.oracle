SET AUTOCOMMIT OFF;

BEGIN
    insert into sys_region(id,parent_id,region_name,region_code,del_flag)
values('661500',(select id from sys_region where region_name = '新疆生产建设兵团'),'兵团总部','661500','N');
insert into sys_region(id,parent_id,region_name,region_code,del_flag)
values('661501',(select id from sys_region where region_name = '兵团总部'),'兵团总部','661501','N');

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
END;


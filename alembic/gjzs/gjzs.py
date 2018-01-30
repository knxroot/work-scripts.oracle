# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Index, LargeBinary, Numeric, String, Table, Text, Unicode, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class ActGeBytearray(Base):
    __tablename__ = 'act_ge_bytearray'

    id_ = Column(String(64), primary_key=True)
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    name_ = Column(String(255))
    deployment_id_ = Column(ForeignKey(u'act_re_deployment.id_'), index=True)
    bytes_ = Column(LargeBinary)
    generated_ = Column(Numeric(1, 0, asdecimal=False))

    act_re_deployment = relationship(u'ActReDeployment')


class ActGeProperty(Base):
    __tablename__ = 'act_ge_property'

    name_ = Column(String(64), primary_key=True)
    value_ = Column(String(300))
    rev_ = Column(Numeric(scale=0, asdecimal=False))


class ActHiActinst(Base):
    __tablename__ = 'act_hi_actinst'
    __table_args__ = (
        Index('act_idx_hi_act_inst_procinst', 'proc_inst_id_', 'act_id_'),
        Index('act_idx_hi_act_inst_exec', 'execution_id_', 'act_id_')
    )

    id_ = Column(String(64), primary_key=True)
    proc_def_id_ = Column(String(64), nullable=False)
    proc_inst_id_ = Column(String(64), nullable=False)
    execution_id_ = Column(String(64), nullable=False)
    act_id_ = Column(String(255), nullable=False)
    task_id_ = Column(String(64))
    call_proc_inst_id_ = Column(String(64))
    act_name_ = Column(String(255))
    act_type_ = Column(String(255), nullable=False)
    assignee_ = Column(String(64))
    start_time_ = Column(DateTime, nullable=False, index=True)
    end_time_ = Column(DateTime, index=True)
    duration_ = Column(Numeric(19, 0, asdecimal=False))


class ActHiAttachment(Base):
    __tablename__ = 'act_hi_attachment'

    id_ = Column(String(64), primary_key=True)
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    user_id_ = Column(String(255))
    name_ = Column(String(255))
    description_ = Column(String(2000))
    type_ = Column(String(255))
    task_id_ = Column(String(64))
    proc_inst_id_ = Column(String(64))
    url_ = Column(String(2000))
    content_id_ = Column(String(64))


class ActHiComment(Base):
    __tablename__ = 'act_hi_comment'

    id_ = Column(String(64), primary_key=True)
    type_ = Column(String(255))
    time_ = Column(DateTime, nullable=False)
    user_id_ = Column(String(255))
    task_id_ = Column(String(64))
    proc_inst_id_ = Column(String(64))
    action_ = Column(String(255))
    message_ = Column(String(2000))
    full_msg_ = Column(LargeBinary)


class ActHiDetail(Base):
    __tablename__ = 'act_hi_detail'

    id_ = Column(String(64), primary_key=True)
    type_ = Column(String(255), nullable=False)
    proc_inst_id_ = Column(String(64), index=True)
    execution_id_ = Column(String(64))
    task_id_ = Column(String(64), index=True)
    act_inst_id_ = Column(String(64), index=True)
    name_ = Column(String(255), nullable=False, index=True)
    var_type_ = Column(String(64))
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    time_ = Column(DateTime, nullable=False, index=True)
    bytearray_id_ = Column(String(64))
    double_ = Column(Numeric(scale=10))
    long_ = Column(Numeric(19, 0, asdecimal=False))
    text_ = Column(String(2000))
    text2_ = Column(String(2000))


class ActHiIdentitylink(Base):
    __tablename__ = 'act_hi_identitylink'

    id_ = Column(Unicode(64), primary_key=True)
    group_id_ = Column(Unicode(255))
    type_ = Column(Unicode(255))
    user_id_ = Column(Unicode(255), index=True)
    task_id_ = Column(Unicode(64), index=True)
    proc_inst_id_ = Column(Unicode(64), index=True)


class ActHiProcinst(Base):
    __tablename__ = 'act_hi_procinst'

    id_ = Column(String(64), primary_key=True)
    proc_inst_id_ = Column(String(64), nullable=False, unique=True)
    business_key_ = Column(String(255), index=True)
    proc_def_id_ = Column(String(64), nullable=False)
    start_time_ = Column(DateTime, nullable=False)
    end_time_ = Column(DateTime, index=True)
    duration_ = Column(Numeric(19, 0, asdecimal=False))
    start_user_id_ = Column(String(255))
    start_act_id_ = Column(String(255))
    end_act_id_ = Column(String(255))
    super_process_instance_id_ = Column(String(64))
    delete_reason_ = Column(String(2000))


class ActHiTaskinst(Base):
    __tablename__ = 'act_hi_taskinst'

    id_ = Column(String(64), primary_key=True)
    proc_def_id_ = Column(String(64))
    task_def_key_ = Column(String(255))
    proc_inst_id_ = Column(String(64))
    execution_id_ = Column(String(64))
    parent_task_id_ = Column(String(64))
    name_ = Column(String(255))
    description_ = Column(String(2000))
    owner_ = Column(String(255))
    assignee_ = Column(String(255))
    start_time_ = Column(DateTime, nullable=False)
    claim_time_ = Column(DateTime)
    end_time_ = Column(DateTime)
    duration_ = Column(Numeric(19, 0, asdecimal=False))
    delete_reason_ = Column(String(2000))
    priority_ = Column(Numeric(scale=0, asdecimal=False))
    due_date_ = Column(DateTime)
    form_key_ = Column(String(255))


class ActHiVarinst(Base):
    __tablename__ = 'act_hi_varinst'
    __table_args__ = (
        Index('act_idx_hi_procvar_name_type', 'name_', 'var_type_'),
    )

    id_ = Column(String(64), primary_key=True)
    proc_inst_id_ = Column(String(64), index=True)
    execution_id_ = Column(String(64))
    task_id_ = Column(String(64))
    name_ = Column(String(255), nullable=False)
    var_type_ = Column(String(100))
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    bytearray_id_ = Column(String(64))
    double_ = Column(Numeric(scale=10))
    long_ = Column(Numeric(19, 0, asdecimal=False))
    text_ = Column(String(2000))
    text2_ = Column(String(2000))


class ActIdGroup(Base):
    __tablename__ = 'act_id_group'

    id_ = Column(String(64), primary_key=True)
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    name_ = Column(String(255))
    type_ = Column(String(255))

    act_id_user = relationship(u'ActIdUser', secondary='act_id_membership')


class ActIdInfo(Base):
    __tablename__ = 'act_id_info'

    id_ = Column(String(64), primary_key=True)
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    user_id_ = Column(String(64))
    type_ = Column(String(64))
    key_ = Column(String(255))
    value_ = Column(String(255))
    password_ = Column(LargeBinary)
    parent_id_ = Column(String(255))


t_act_id_membership = Table(
    'act_id_membership', metadata,
    Column('user_id_', ForeignKey(u'act_id_user.id_'), primary_key=True, nullable=False, index=True),
    Column('group_id_', ForeignKey(u'act_id_group.id_'), primary_key=True, nullable=False, index=True)
)


class ActIdUser(Base):
    __tablename__ = 'act_id_user'

    id_ = Column(String(64), primary_key=True)
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    first_ = Column(String(255))
    last_ = Column(String(255))
    email_ = Column(String(255))
    pwd_ = Column(String(255))
    picture_id_ = Column(String(64))


class ActReDeployment(Base):
    __tablename__ = 'act_re_deployment'

    id_ = Column(String(64), primary_key=True)
    name_ = Column(String(255))
    category_ = Column(String(255))
    deploy_time_ = Column(DateTime)


class ActReModel(Base):
    __tablename__ = 'act_re_model'

    id_ = Column(String(64), primary_key=True)
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    name_ = Column(String(255))
    key_ = Column(String(255))
    category_ = Column(String(255))
    create_time_ = Column(DateTime)
    last_update_time_ = Column(DateTime)
    version_ = Column(Numeric(scale=0, asdecimal=False))
    meta_info_ = Column(String(2000))
    deployment_id_ = Column(ForeignKey(u'act_re_deployment.id_'), index=True)
    editor_source_value_id_ = Column(ForeignKey(u'act_ge_bytearray.id_'), index=True)
    editor_source_extra_value_id_ = Column(ForeignKey(u'act_ge_bytearray.id_'), index=True)

    act_re_deployment = relationship(u'ActReDeployment')
    act_ge_bytearray = relationship(u'ActGeBytearray', primaryjoin='ActReModel.editor_source_extra_value_id_ == ActGeBytearray.id_')
    act_ge_bytearray1 = relationship(u'ActGeBytearray', primaryjoin='ActReModel.editor_source_value_id_ == ActGeBytearray.id_')


class ActReProcdef(Base):
    __tablename__ = 'act_re_procdef'
    __table_args__ = (
        Index('act_uniq_procdef', 'key_', 'version_', unique=True),
    )

    id_ = Column(String(64), primary_key=True)
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    category_ = Column(String(255))
    name_ = Column(String(255))
    key_ = Column(String(255), nullable=False)
    version_ = Column(Numeric(scale=0, asdecimal=False), nullable=False)
    deployment_id_ = Column(String(64))
    resource_name_ = Column(String(2000))
    dgrm_resource_name_ = Column(String(4000))
    description_ = Column(String(2000))
    has_start_form_key_ = Column(Numeric(1, 0, asdecimal=False))
    suspension_state_ = Column(Numeric(scale=0, asdecimal=False))


class ActRuEventSubscr(Base):
    __tablename__ = 'act_ru_event_subscr'

    id_ = Column(String(64), primary_key=True)
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    event_type_ = Column(String(255), nullable=False)
    event_name_ = Column(String(255))
    execution_id_ = Column(ForeignKey(u'act_ru_execution.id_'), index=True)
    proc_inst_id_ = Column(String(64))
    activity_id_ = Column(String(64))
    configuration_ = Column(String(255), index=True)
    created_ = Column(DateTime, nullable=False)

    act_ru_execution = relationship(u'ActRuExecution')


class ActRuExecution(Base):
    __tablename__ = 'act_ru_execution'

    id_ = Column(String(64), primary_key=True)
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    proc_inst_id_ = Column(ForeignKey(u'act_ru_execution.id_'), index=True)
    business_key_ = Column(String(255), index=True)
    parent_id_ = Column(ForeignKey(u'act_ru_execution.id_'), index=True)
    proc_def_id_ = Column(ForeignKey(u'act_re_procdef.id_'), index=True)
    super_exec_ = Column(ForeignKey(u'act_ru_execution.id_'), index=True)
    act_id_ = Column(String(255))
    is_active_ = Column(Numeric(1, 0, asdecimal=False))
    is_concurrent_ = Column(Numeric(1, 0, asdecimal=False))
    is_scope_ = Column(Numeric(1, 0, asdecimal=False))
    is_event_scope_ = Column(Numeric(1, 0, asdecimal=False))
    suspension_state_ = Column(Numeric(scale=0, asdecimal=False))
    cached_ent_state_ = Column(Numeric(scale=0, asdecimal=False))

    parent = relationship(u'ActRuExecution', remote_side=[id_], primaryjoin='ActRuExecution.parent_id_ == ActRuExecution.id_')
    act_re_procdef = relationship(u'ActReProcdef')
    parent1 = relationship(u'ActRuExecution', remote_side=[id_], primaryjoin='ActRuExecution.proc_inst_id_ == ActRuExecution.id_')
    parent2 = relationship(u'ActRuExecution', remote_side=[id_], primaryjoin='ActRuExecution.super_exec_ == ActRuExecution.id_')


class ActRuIdentitylink(Base):
    __tablename__ = 'act_ru_identitylink'

    id_ = Column(String(64), primary_key=True)
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    group_id_ = Column(String(255), index=True)
    type_ = Column(String(255))
    user_id_ = Column(String(255), index=True)
    task_id_ = Column(ForeignKey(u'act_ru_task.id_'), index=True)
    proc_inst_id_ = Column(ForeignKey(u'act_ru_execution.id_'), index=True)
    proc_def_id_ = Column(ForeignKey(u'act_re_procdef.id_'), index=True)

    act_re_procdef = relationship(u'ActReProcdef')
    act_ru_execution = relationship(u'ActRuExecution')
    act_ru_task = relationship(u'ActRuTask')


class ActRuJob(Base):
    __tablename__ = 'act_ru_job'

    id_ = Column(String(64), primary_key=True)
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    type_ = Column(String(255), nullable=False)
    lock_exp_time_ = Column(DateTime)
    lock_owner_ = Column(String(255))
    exclusive_ = Column(Numeric(1, 0, asdecimal=False))
    execution_id_ = Column(String(64))
    process_instance_id_ = Column(String(64))
    proc_def_id_ = Column(String(64))
    retries_ = Column(Numeric(scale=0, asdecimal=False))
    exception_stack_id_ = Column(ForeignKey(u'act_ge_bytearray.id_'), index=True)
    exception_msg_ = Column(String(2000))
    duedate_ = Column(DateTime)
    repeat_ = Column(String(255))
    handler_type_ = Column(String(255))
    handler_cfg_ = Column(String(2000))

    act_ge_bytearray = relationship(u'ActGeBytearray')


class ActRuTask(Base):
    __tablename__ = 'act_ru_task'

    id_ = Column(String(64), primary_key=True)
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    execution_id_ = Column(ForeignKey(u'act_ru_execution.id_'), index=True)
    proc_inst_id_ = Column(ForeignKey(u'act_ru_execution.id_'), index=True)
    proc_def_id_ = Column(ForeignKey(u'act_re_procdef.id_'), index=True)
    name_ = Column(String(255))
    parent_task_id_ = Column(String(64))
    description_ = Column(String(2000))
    task_def_key_ = Column(String(255))
    owner_ = Column(String(255))
    assignee_ = Column(String(255))
    delegation_ = Column(String(64))
    priority_ = Column(Numeric(scale=0, asdecimal=False))
    create_time_ = Column(DateTime, index=True)
    due_date_ = Column(DateTime)
    suspension_state_ = Column(Numeric(scale=0, asdecimal=False))

    act_ru_execution = relationship(u'ActRuExecution', primaryjoin='ActRuTask.execution_id_ == ActRuExecution.id_')
    act_re_procdef = relationship(u'ActReProcdef')
    act_ru_execution1 = relationship(u'ActRuExecution', primaryjoin='ActRuTask.proc_inst_id_ == ActRuExecution.id_')


class ActRuVariable(Base):
    __tablename__ = 'act_ru_variable'

    id_ = Column(String(64), primary_key=True)
    rev_ = Column(Numeric(scale=0, asdecimal=False))
    type_ = Column(String(255), nullable=False)
    name_ = Column(String(255), nullable=False)
    execution_id_ = Column(ForeignKey(u'act_ru_execution.id_'), index=True)
    proc_inst_id_ = Column(ForeignKey(u'act_ru_execution.id_'), index=True)
    task_id_ = Column(String(64), index=True)
    bytearray_id_ = Column(ForeignKey(u'act_ge_bytearray.id_'), index=True)
    double_ = Column(Numeric(scale=10))
    long_ = Column(Numeric(19, 0, asdecimal=False))
    text_ = Column(String(2000))
    text2_ = Column(String(2000))

    act_ge_bytearray = relationship(u'ActGeBytearray')
    act_ru_execution = relationship(u'ActRuExecution', primaryjoin='ActRuVariable.execution_id_ == ActRuExecution.id_')
    act_ru_execution1 = relationship(u'ActRuExecution', primaryjoin='ActRuVariable.proc_inst_id_ == ActRuExecution.id_')


class AdsCheckInfo(Base):
    __tablename__ = 'ads_check_info'

    id = Column(String(64), primary_key=True)
    sample_bar_code = Column(String(64), nullable=False, index=True)
    sample_code = Column(String(32), nullable=False)
    sample_name = Column(String(32), nullable=False)
    check_link = Column(String(32), nullable=False)
    result = Column(String(2), nullable=False)
    check_organ_id = Column(String(64), nullable=False)
    check_report = Column(String(2), nullable=False)
    check_time = Column(DateTime, nullable=False)
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    organ_task_id = Column(String(64), nullable=False)
    product_traceability_code = Column(String(200), nullable=False)
    tested_deparment = Column(String(64))
    sample_deparment = Column(String(64))
    monitor_sample_id = Column(String(64), nullable=False)
    check_organ = Column(String(256))


class AdsCheckModel(Base):
    __tablename__ = 'ads_check_model'

    id = Column(String(64), primary_key=True)
    model_name = Column(String(32), nullable=False, unique=True)
    monitor_type = Column(String(32))
    industry = Column(String(64))
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    industry_id = Column(String(64))
    is_enable = Column(String(1), server_default=text("""\
'0'
"""))


class AdsCheckProject(Base):
    __tablename__ = 'ads_check_project'

    id = Column(String(64), primary_key=True)
    check_project = Column(String(32), nullable=False)
    check_num = Column(String(32), nullable=False)
    judge_num = Column(String(32), nullable=False)
    result = Column(String(32), nullable=False)
    check_info_id = Column(ForeignKey(u'ads_check_info.id'), nullable=False)
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))

    check_info = relationship(u'AdsCheckInfo')


class AdsFile(Base):
    __tablename__ = 'ads_file'

    id = Column(String(64), primary_key=True)
    file_address = Column(String(1024), nullable=False)
    monitor_task_id = Column(String(64), nullable=False)
    monitor_task = Column(String(64), nullable=False)
    upload_department = Column(String(64), nullable=False)
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    file_name = Column(String(128), nullable=False)
    monitor_type = Column(String(16), nullable=False)
    years = Column(String(8))
    source = Column(String(32))
    folder = Column(String(64))
    field = Column(String(64))
    organ_task_id = Column(String(64))
    field_id = Column(String(64))


class AdsInfoProject(Base):
    __tablename__ = 'ads_info_project'

    id = Column(String(64), primary_key=True)
    check_project = Column(String(32), nullable=False)
    check_num = Column(String(32), nullable=False)
    judge_num = Column(String(32), nullable=False)
    result = Column(String(2), nullable=False)
    check_info_id = Column(String(64), nullable=False)
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    required = Column(String(32), server_default=text("""\
'1'
"""))


class AdsModelAttributeMapping(Base):
    __tablename__ = 'ads_model_attribute_mapping'

    id = Column(String(64), primary_key=True)
    model_id = Column(String(64), nullable=False)
    object_id = Column(String(64), nullable=False)
    type = Column(String(32))
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))


class AdsModelCheckItem(Base):
    __tablename__ = 'ads_model_check_item'

    id = Column(String(64), primary_key=True)
    standard_id = Column(String(64), nullable=False)
    name = Column(String(200), nullable=False)
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))


class AdsModelCheckObject(Base):
    __tablename__ = 'ads_model_check_object'

    id = Column(String(64), primary_key=True)
    name = Column(String(200), nullable=False, unique=True)
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    numbers = Column(Numeric(asdecimal=False), server_default=text("""\
0
"""))
    gb_code = Column(String(64))
    product_code = Column(String(64))
    product_name = Column(String(64))
    industry = Column(String(64))


class AdsModelCheckStandard(Base):
    __tablename__ = 'ads_model_check_standard'

    id = Column(String(64), primary_key=True)
    name = Column(String(200), nullable=False)
    value = Column(Numeric(asdecimal=False), nullable=False)
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))


class AdsModelJudgeStandard(Base):
    __tablename__ = 'ads_model_judge_standard'

    id = Column(String(64), primary_key=True)
    name = Column(String(200), nullable=False)
    file_path = Column(String(200))
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))


class AdsModelObjectItemMapping(Base):
    __tablename__ = 'ads_model_object_item_mapping'

    id = Column(String(64), primary_key=True)
    object_id = Column(String(64), nullable=False)
    item_id = Column(String(64), nullable=False)
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))


class AdsModelSampleLink(Base):
    __tablename__ = 'ads_model_sample_link'

    id = Column(String(64), primary_key=True)
    name = Column(String(200), nullable=False)
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))


class AdsModelType(Base):
    __tablename__ = 'ads_model_type'

    id = Column(String(64), primary_key=True)
    name = Column(String(64), nullable=False)
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))


class AdsMonitorSample(Base):
    __tablename__ = 'ads_monitor_sample'

    id = Column(String(64), primary_key=True)
    organ_task_id = Column(String(64), nullable=False)
    sample_bar_code = Column(String(32), nullable=False)
    sample_name = Column(String(32), nullable=False)
    sample_code = Column(String(32), nullable=False)
    trade_mark = Column(String(32))
    packing = Column(String(32))
    grade = Column(String(32))
    identify = Column(String(32))
    specification = Column(String(32))
    standard = Column(String(32))
    produce_date = Column(DateTime, nullable=False)
    produce_certificate = Column(String(1024))
    certificate_code = Column(String(128))
    sample_base = Column(Numeric(8, 0, asdecimal=False))
    sample_place = Column(String(1024), nullable=False)
    tested_deparment = Column(String(200), nullable=False)
    tested_address = Column(String(512), nullable=False)
    tested_legalrep = Column(String(32))
    tested_linkman = Column(String(32))
    tested_linkmanphone = Column(String(32))
    tested_linkmanfax = Column(String(32))
    tested_person = Column(String(32), nullable=False)
    tested_personphone = Column(String(16))
    tested_personfax = Column(String(16))
    productions_tatus = Column(String(32))
    production_deparment = Column(String(200), nullable=False)
    production_address = Column(String(512), nullable=False)
    production_zipcode = Column(String(16))
    production_linkman = Column(String(32))
    production_linkmanphone = Column(String(32))
    production_linkmanfax = Column(String(32))
    sample_id = Column(String(64), nullable=False)
    sample_deparment = Column(String(200), nullable=False)
    sample_linkman = Column(String(32), nullable=False)
    sample_address = Column(String(512))
    sample_zipcode = Column(String(16))
    sample_phone = Column(String(16))
    sample_fax = Column(String(16))
    sample_email = Column(String(16))
    proof = Column(String(1024))
    sample_person = Column(String(32), nullable=False)
    sample_date = Column(DateTime, nullable=False)
    sample_report = Column(String(32))
    COMMENT = Column(String(1024))
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    producing_area = Column(String(1024))
    producing_area_name = Column(String(1024))
    product_traceability_code = Column(String(200), nullable=False)


class AdsMonitorTask(Base):
    __tablename__ = 'ads_monitor_task'

    id = Column(String(64), primary_key=True)
    task_name = Column(String(256), index=True)
    monitor_class = Column(String(32), index=True)
    release_unit = Column(String(256), index=True)
    check_model = Column(String(64))
    year = Column(String(6))
    batch = Column(String(32))
    separation = Column(Numeric(asdecimal=False))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    deadline = Column(DateTime)
    attachment = Column(String(128))
    attachmentcode = Column(String(64))
    COMMENT = Column(String(1024))
    publish_status = Column(Numeric(asdecimal=False))
    industry = Column(String(1024))
    judge_standard = Column(String(1024))
    sample_link = Column(String(1024))
    check_object = Column(String(1024))
    check_project = Column(String(1024))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    task_source = Column(String(32), server_default=text("""\
'DEPTASK'
"""))
    numbers = Column(Numeric(asdecimal=False))
    leve = Column(String(64))
    attachment_address = Column(String(1024))
    abolish = Column(String(1), server_default=text("""\
'1'
"""))
    organ_id = Column(String(64))
    sup_id = Column(String(64))
    industry_id = Column(String(64))


class AdsOrganTask(Base):
    __tablename__ = 'ads_organ_task'

    id = Column(String(64), primary_key=True)
    monitor_task_id = Column(String(64))
    sample_organ = Column(String(200))
    sample_organ_id = Column(String(64))
    detection_organ = Column(String(200))
    detection_organ_id = Column(String(64))
    reg_id = Column(String(64))
    numbers = Column(Numeric(asdecimal=False))
    deparment = Column(String(200))
    upload_time = Column(DateTime)
    finish_num = Column(Numeric(asdecimal=False))
    report_status = Column(String(32))
    report_time = Column(DateTime)
    tasks_status = Column(String(32))
    sample_finish_num = Column(Numeric(asdecimal=False))
    check_finish_num = Column(Numeric(asdecimal=False))
    sample_finish_status = Column(Numeric(asdecimal=False))
    check_finish_status = Column(Numeric(asdecimal=False))
    sample_report_status = Column(Numeric(asdecimal=False))
    check_report_status = Column(Numeric(asdecimal=False))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    check_report_time = Column(DateTime)
    sample_report_time = Column(DateTime)
    city_code = Column(String(40))
    city_name = Column(String(80))
    deparment_id = Column(String(64))


class AdsRecipe(Base):
    __tablename__ = 'ads_recipe'

    id = Column(String(64), primary_key=True)
    organ_name = Column(String(32), nullable=False)
    organ_task_id = Column(String(64), nullable=False, index=True)
    organ_id = Column(String(64), nullable=False)
    task_num = Column(Numeric(asdecimal=False))
    receipt_class = Column(String(64), nullable=False, index=True)
    receipt_time = Column(DateTime, nullable=False)
    reason = Column(String(64), nullable=False)
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    finish_num = Column(Numeric(asdecimal=False))
    s_name = Column(String(1024))
    s_code = Column(String(1024))


class AlesDailyEnforceLaw(Base):
    __tablename__ = 'ales_daily_enforce_law'

    id = Column(String(64), primary_key=True)
    task_name = Column(String(100))
    task_begin_time = Column(DateTime)
    task_end_time = Column(DateTime)
    enterprise_id = Column(String(64))
    area_id = Column(String(64))
    enterprise_address = Column(String(300))
    task_person_count = Column(String(100))
    task_person_id = Column(String(64))
    enforce_law_result = Column(String(1000))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    enable = Column(String(1))
    del_flag = Column(String(1))
    enterprise_name = Column(String(150))


class AlesEntrustDetection(Base):
    __tablename__ = 'ales_entrust_detection'

    id = Column(String(64), primary_key=True)
    task_name = Column(String(100))
    task_begin_time = Column(DateTime)
    task_end_time = Column(DateTime)
    detection_id = Column(String(64))
    file_url = Column(String(1000))
    file_code = Column(String(100))
    remark = Column(String(1000))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    enable = Column(String(1))
    state = Column(String(20))
    taskyear = Column(String(4))
    del_flag = Column(String(1))
    task_type = Column(String(100))
    task_release_unit = Column(String(100))
    task_area_id = Column(String(64))
    create_org_region_id = Column(String(64))
    cy_unit_id = Column(String(64))
    cy_unit_name = Column(String(50))
    jc_unit_id = Column(String(64))
    jc_unit_name = Column(String(50))
    judge_standard = Column(String(100))
    judge_standard_id = Column(String(64))
    detection_standard = Column(String(100))
    detection_standard_id = Column(String(64))
    parent_task_id = Column(String(64))
    parent_task_name = Column(String(50))
    create_org_id = Column(String(64))
    create_org_name = Column(String(50))
    st_unit_id = Column(String(64))
    st_unit_name = Column(String(50))


class AlesEntrustSample(Base):
    __tablename__ = 'ales_entrust_sample'

    id = Column(String(64), primary_key=True)
    product_code = Column(String(200))
    sample_code = Column(String(200))
    entrust_detection_id = Column(String(64))
    enterprise_id = Column(String(64))
    sample_address = Column(String(200))
    sample_information = Column(String(1000))
    sample_unit_id = Column(String(64))
    remark = Column(String(200))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    enable = Column(String(1))
    del_flag = Column(String(1))


class AlesProduceAdminPunish(Base):
    __tablename__ = 'ales_produce_admin_punish'

    id = Column(String(64), primary_key=True)
    punish_code = Column(String(100))
    legal_person = Column(String(100))
    case_name = Column(String(100))
    product_name = Column(String(100))
    enterprise_name = Column(String(200))
    manufacture_date = Column(String(100))
    punish_qualitative = Column(String(1000))
    punish_result = Column(String(1000))
    punish_files = Column(String(100))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    enable = Column(String(1))
    enterprise_id = Column(String(64))
    enterprise_code = Column(String(100))
    enforce_law_id = Column(String(64))
    enforce_law_people = Column(String(200))
    enforce_law_time = Column(DateTime)
    del_flag = Column(String(1))


class AlesSample(Base):
    __tablename__ = 'ales_sample'

    id = Column(String(64), primary_key=True)
    prodcut_code = Column(String(200))
    sample_code = Column(String(200))
    check_task_id = Column(String(64))
    enterprise_id = Column(String(64))
    sample_address = Column(String(200))
    sample_information = Column(String(1000))
    sample_unit_id = Column(String(64))
    remark = Column(String(200))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    enable = Column(String(1))
    del_flag = Column(String(1))


class AlesTaskSample(Base):
    __tablename__ = 'ales_task_sample'

    id = Column(String(64), primary_key=True)
    organ_task_id = Column(String(64))
    product_traceability_code = Column(String(64))
    sample_bar_code = Column(Numeric(asdecimal=False))
    sample_name = Column(String(32))
    sample_code = Column(String(32))
    trade_mark = Column(String(32))
    packing = Column(String(32))
    grade = Column(String(32))
    identify = Column(String(32))
    specification_gx = Column(String(32))
    standard = Column(String(32))
    produce_date = Column(DateTime)
    produce_certificate = Column(String(1024))
    certificate_code = Column(String(128))
    sample_base = Column(Numeric(8, 0, asdecimal=False))
    sample_place = Column(String(1024))
    tested_deparment = Column(String(32))
    tested_address = Column(String(512))
    tested_legalrep = Column(String(32))
    tested_linkman = Column(String(32))
    tested_linkmanphone = Column(String(16))
    tested_linkmanfax = Column(String(16))
    tested_person = Column(String(32))
    tested_personphone = Column(String(16))
    tested_personfax = Column(String(16))
    productions_tatus = Column(String(32))
    production_deparment = Column(String(32))
    production_address = Column(String(512))
    production_zipcode = Column(String(16))
    production_linkman = Column(String(32))
    production_linkmanphone = Column(String(16))
    production_linkmanfax = Column(String(16))
    sample_id = Column(String(64))
    sample_deparment = Column(String(32))
    sample_linkman = Column(String(32))
    sample_address = Column(String(512))
    sample_zipcode = Column(String(16))
    sample_phone = Column(String(16))
    sample_fax = Column(String(16))
    sample_email = Column(String(16))
    proof = Column(String(1024))
    sample_person = Column(String(16))
    sample_date = Column(DateTime)
    sample_report = Column(String(32))
    comment_gx = Column(String(1024))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    producing_area = Column(String(1024))
    producing_area_name = Column(String(1024))
    is_sync = Column(String(4))


class AlesWtTaskSample(Base):
    __tablename__ = 'ales_wt_task_sample'

    id = Column(String(64), primary_key=True)
    wt_task_id = Column(String(64))
    product_traceability_code = Column(String(64))
    sample_bar_code = Column(Numeric(asdecimal=False))
    sample_name = Column(String(32))
    sample_code = Column(String(32))
    trade_mark = Column(String(32))
    packing = Column(String(32))
    grade = Column(String(32))
    identify = Column(String(32))
    specification_gx = Column(String(32))
    standard = Column(String(32))
    produce_date = Column(DateTime)
    produce_certificate = Column(String(1024))
    certificate_code = Column(String(128))
    sample_base = Column(Numeric(8, 0, asdecimal=False))
    sample_place = Column(String(1024))
    tested_deparment = Column(String(32))
    tested_address = Column(String(512))
    tested_legalrep = Column(String(32))
    tested_linkman = Column(String(32))
    tested_linkmanphone = Column(String(16))
    tested_linkmanfax = Column(String(16))
    tested_person = Column(String(32))
    tested_personphone = Column(String(16))
    tested_personfax = Column(String(16))
    productions_tatus = Column(String(32))
    production_deparment = Column(String(32))
    production_address = Column(String(512))
    production_zipcode = Column(String(16))
    production_linkman = Column(String(32))
    production_linkmanphone = Column(String(16))
    production_linkmanfax = Column(String(16))
    sample_id = Column(String(64))
    sample_deparment = Column(String(32))
    sample_linkman = Column(String(32))
    sample_address = Column(String(512))
    sample_zipcode = Column(String(16))
    sample_phone = Column(String(16))
    sample_fax = Column(String(16))
    sample_email = Column(String(16))
    proof = Column(String(1024))
    sample_person = Column(String(16))
    sample_date = Column(DateTime)
    sample_report = Column(String(32))
    comment_gx = Column(String(1024))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    producing_area = Column(String(1024))
    producing_area_name = Column(String(1024))
    is_sync = Column(String(4))


class AsmsBaseInspection(Base):
    __tablename__ = 'asms_base_inspection'

    id = Column(String(64), primary_key=True)
    enterprise_id = Column(String(64))
    inspection_type = Column(String(100))
    inspection_result = Column(String(100))
    inspection_view = Column(String(1000))
    inspection_images = Column(String(1000))
    inspection_time = Column(DateTime)
    inspection_sv_name = Column(String(200))
    inspection_sv_id = Column(String(64))
    inspection_user_name = Column(String(200))
    el_check_state = Column(String(64))
    head_sign = Column(String(50))
    head_sign_file = Column(String(200))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    enable = Column(String(1))
    del_flag = Column(String(1), nullable=False)
    inspection_type_name = Column(String(100))


class AsmsBaseUser(Base):
    __tablename__ = 'asms_base_user'

    id = Column(String(64), primary_key=True)
    base_inspection_id = Column(String(64))
    inspection_user_id = Column(String(64))


class AsmsCheckBearUnit(Base):
    __tablename__ = 'asms_check_bear_unit'

    id = Column(String(64), primary_key=True)
    supervise_check_task_id = Column(String(64))
    supervise_bear_unit_id = Column(String(64))
    del_flag = Column(String(1))
    lead_unit_name = Column(String(70))


class AsmsCheckTask(Base):
    __tablename__ = 'asms_check_task'

    id = Column(String(64), primary_key=True)
    task_name = Column(String(100))
    task_type = Column(String(100))
    task_year = Column(String(4))
    task_begin_time = Column(DateTime)
    task_end_time = Column(DateTime)
    task_release_unit = Column(String(100))
    task_is_separate = Column(String(1))
    task_area_id = Column(String(64))
    task_industry = Column(String(100))
    task_sample_deadline = Column(DateTime)
    files = Column(String(1000))
    file_code = Column(String(100))
    remark = Column(String(1000))
    task_level = Column(String(2))
    state = Column(String(20))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    enable = Column(String(1))
    del_flag = Column(String(1))
    create_org_region_id = Column(String(64))
    base_inspection_id = Column(String(64))
    cy_unit_id = Column(String(64))
    cy_unit_name = Column(String(50))
    jc_unit_id = Column(String(64))
    jc_unit_name = Column(String(50))
    is_sample = Column(String(1))
    judge_standard = Column(String(100))
    judge_standard_id = Column(String(64))
    detection_standard = Column(String(100))
    detection_standard_id = Column(String(64))
    parent_task_id = Column(String(64))
    parent_task_name = Column(String(50))
    create_org_id = Column(String(64))
    create_org_name = Column(String(50))
    jc_standard_link_id = Column(String(200))
    pd_standard_link_id = Column(String(200))


class AsmsCheckTaskEnterprise(Base):
    __tablename__ = 'asms_check_task_enterprise'

    id = Column(String(64), primary_key=True)
    enterprise_id = Column(String(64))
    enterprise_name = Column(String(300))
    check_task_object_id = Column(String(64))
    entity_type = Column(String(700))
    credit_code = Column(String(20))
    legal_name = Column(String(300))
    legal_phone = Column(String(15))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    check_task_id = Column(String(64))


class AsmsCheckTaskReport(Base):
    __tablename__ = 'asms_check_task_report'

    id = Column(String(64), primary_key=True)
    file_address = Column(String(1024))
    monitor_task_id = Column(String(64), nullable=False)
    monitor_task = Column(String(64))
    upload_department = Column(String(64))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("'N' "))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    file_name = Column(String(128))
    monitor_type = Column(String(16))
    years = Column(String(8))
    source = Column(String(32))
    folder = Column(String(64))
    field = Column(String(16))
    organ_task_id = Column(String(64))


class AsmsEmergencyExpert(Base):
    __tablename__ = 'asms_emergency_expert'

    id = Column(String(64), primary_key=True)
    emergency_id = Column(String(64))
    expert_id = Column(String(64))


class AsmsEmergencyTask(Base):
    __tablename__ = 'asms_emergency_task'

    id = Column(String(64), primary_key=True)
    task_name = Column(String(100))
    task_type = Column(String(100))
    area_id = Column(String(100))
    task_begin = Column(DateTime)
    task_end = Column(DateTime)
    release_unit = Column(String(100))
    release_unit_level = Column(String(100))
    is_bear_unit = Column(String(100))
    bear_unit = Column(String(100))
    files = Column(String(100))
    file_code = Column(String(100))
    remark = Column(String(100))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    enable = Column(String(1))
    del_flag = Column(String(1))
    expert_name = Column(String(100))


class AsmsInspectionAsses(Base):
    __tablename__ = 'asms_inspection_assess'

    id = Column(String(64), primary_key=True)
    inspection_task_id = Column(String(64))
    user_name = Column(String(100))
    user_id = Column(String(64))
    task_result = Column(String(100))
    inspection_real_count = Column(Numeric(10, 0, asdecimal=False))
    del_flag = Column(String(1))


class AsmsInspectionTask(Base):
    __tablename__ = 'asms_inspection_task'

    id = Column(String(64), primary_key=True)
    task_type = Column(String(100))
    task_date_type = Column(String(10))
    task_date = Column(String(20))
    inspection_area_id = Column(String(100))
    inspection_count = Column(Numeric(10, 0, asdecimal=False))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    enable = Column(String(1))
    del_flag = Column(String(1))
    task_date_year = Column(String(10))
    task_date_months = Column(String(10))
    task_date_quarter = Column(String(15))
    task_type_name = Column(String(100))


class AsmsJcStandard(Base):
    __tablename__ = 'asms_jc_standard'

    id = Column(String(64), primary_key=True)
    standard_id = Column(String(64))
    standard_name = Column(String(50))
    task_id = Column(String(64))
    task_name = Column(String(50))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    remark = Column(String(200))


class AsmsMonitorObject(Base):
    __tablename__ = 'asms_monitor_object'

    id = Column(String(64), primary_key=True)
    supervise_check_task_id = Column(String(64))
    product_type = Column(String(100))
    product_name = Column(String(100))
    task_begin_time = Column(DateTime)
    task_end_time = Column(DateTime)
    sample_unit_id = Column(String(64))
    detection_unit_id = Column(String(64))
    detection_standard = Column(String(100))
    judge_standard = Column(String(100))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    enable = Column(String(1))
    monitor_num = Column(String(5))
    del_flag = Column(String(1))
    is_sample = Column(String(1))
    detection_item = Column(String(100))
    detection_item_id = Column(String(64))
    product_type_id = Column(String(64))
    product_name_id = Column(String(64))
    area_id = Column(String(64))
    industry = Column(String(400))


class AsmsPdStandard(Base):
    __tablename__ = 'asms_pd_standard'

    id = Column(String(64), primary_key=True)
    standard_id = Column(String(64))
    standard_name = Column(String(50))
    task_id = Column(String(64))
    task_name = Column(String(50))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    remark = Column(String(200))


class AsmsRecheckObject(Base):
    __tablename__ = 'asms_recheck_object'

    id = Column(String(64), primary_key=True)
    recheck_task_id = Column(String(64))
    recheck_sample_name = Column(String(200))
    recheck_sample_code = Column(String(200))
    recheck_unit_id = Column(String(64))
    recheck_standard = Column(String(200))
    recheck_judge_standard = Column(String(200))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    enable = Column(String(1))
    del_flag = Column(String(1))
    recheck_unit_name = Column(String(80))


class AsmsRecheckTask(Base):
    __tablename__ = 'asms_recheck_task'

    id = Column(String(64), primary_key=True)
    recheck_task_name = Column(String(200))
    recheck_task_year = Column(String(4))
    recheck_task_begin = Column(DateTime)
    recheck_task_end = Column(DateTime)
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    enable = Column(String(1))
    state = Column(String(20))
    del_flag = Column(String(1))
    init_task_type = Column(String(50))
    init_task_name = Column(String(50))
    init_task_id = Column(String(64))
    recheck_unit_id = Column(String(64))
    recheck_unit_name = Column(String(100))
    create_org_id = Column(String(64))
    create_org_name = Column(String(100))
    batch = Column(String(32))
    create_org_region_id = Column(String(64))


class AsmsRoutineLeadUnit(Base):
    __tablename__ = 'asms_routine_lead_unit'

    id = Column(String(64), primary_key=True)
    routine_monitor_id = Column(String(64))
    lead_unit_id = Column(String(64))
    del_flag = Column(String(1))
    lead_unit_name = Column(String(70))


class AsmsRoutineMonitor(Base):
    __tablename__ = 'asms_routine_monitor'

    id = Column(String(64), primary_key=True)
    rm_name = Column(String(200))
    rm_type = Column(String(50))
    rm_model_id = Column(String(64))
    rm_year = Column(String(4))
    rm_batch = Column(String(20))
    rm_date_begin = Column(DateTime)
    rm_date_end = Column(DateTime)
    rm_release_unit = Column(String(64))
    rm_file = Column(String(200))
    rm_file_num = Column(String(100))
    rm_remark = Column(String(1000))
    rm_state = Column(String(20))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    enable = Column(String(1))
    del_flag = Column(String(1))
    create_org_region_id = Column(String(64))
    create_org_name = Column(String(200))
    create_org_id = Column(String(64))


class AsmsSpecialLeadUnit(Base):
    __tablename__ = 'asms_special_lead_unit'

    id = Column(String(64), primary_key=True)
    special_monitor_id = Column(String(64))
    lead_unit_id = Column(String(64))
    del_flag = Column(String(1))
    lead_unit_name = Column(String(70))


class AsmsSpecialMonitor(Base):
    __tablename__ = 'asms_special_monitor'

    id = Column(String(64), primary_key=True)
    sm_name = Column(String(200))
    sm_type = Column(String(50))
    sm_model_id = Column(String(64))
    sm_year = Column(String(4))
    sm_batch = Column(String(20))
    sm_date_begin = Column(DateTime)
    sm_date_end = Column(DateTime)
    sm_release_unit = Column(String(64))
    sm_file = Column(String(200))
    sm_file_num = Column(String(100))
    sm_remark = Column(String(1000))
    sm_state = Column(String(20))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    enable = Column(String(1))
    del_flag = Column(String(1))
    create_org_region_id = Column(String(64))
    create_org_id = Column(String(64))
    create_org_name = Column(String(200))


class AsmsSubjDetection(Base):
    __tablename__ = 'asms_subj_detection'

    id = Column(String(64), primary_key=True)
    dt_name = Column(String(200), nullable=False)
    dt_code = Column(String(150), nullable=False)
    dt_type = Column(String(50))
    dt_nature = Column(String(64))
    dt_qualifications = Column(String(64))
    dt_rely_on_unit = Column(String(150))
    dt_level = Column(String(64), nullable=False)
    dt_area_id = Column(String(64), nullable=False)
    dt_address = Column(String(200), nullable=False)
    dt_legal_man = Column(String(150))
    dt_leader = Column(String(150), nullable=False)
    dt_leader_phone = Column(String(20))
    dt_contact = Column(String(150), nullable=False)
    dt_contact_phone = Column(String(20), nullable=False)
    dt_contact_q_q = Column(String(20))
    dt_contact_email = Column(String(150))
    dt_postcode = Column(String(6))
    dt_technical_director = Column(String(150))
    dt_quality_director = Column(String(150))
    dt_parameter = Column(String(150))
    dt_product_range = Column(String(150))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    status = Column(String(1))
    del_flag = Column(String(1))
    dt_level_id = Column(String(64))
    dt_nature_id = Column(String(64))
    dt_qualifications_id = Column(String(64))
    dt_type_id = Column(String(64))
    dt_area = Column(String(200))


class AsmsSubjDtCancel(Base):
    __tablename__ = 'asms_subj_dt_cancel'

    id = Column(String(64), primary_key=True)
    dt_id = Column(String(64), nullable=False)
    apply_reason = Column(String(900), nullable=False)
    apply_user_id = Column(String(64), nullable=False)
    apply_time = Column(DateTime, nullable=False)
    audit_user_id = Column(String(64))
    audit_sv_id = Column(String(64))
    audit_time = Column(DateTime)
    audit_suggestion = Column(String(900))
    audit_state = Column(String(1))
    del_flag = Column(String(1))


class AsmsSubjDtChange(Base):
    __tablename__ = 'asms_subj_dt_change'

    id = Column(String(64), primary_key=True)
    dt_name = Column(String(200))
    dt_code = Column(String(150))
    dt_type = Column(String(50))
    dt_nature = Column(String(64))
    dt_qualifications = Column(String(64))
    dt_rely_on_unit = Column(String(150))
    dt_level = Column(String(64))
    dt_area_id = Column(String(64))
    dt_address = Column(String(200))
    dt_legal_man = Column(String(150))
    dt_leader = Column(String(200))
    dt_leader_phone = Column(String(200))
    dt_contact = Column(String(150))
    dt_contact_phone = Column(String(20))
    dt_contact_q_q = Column(String(20))
    dt_contact_email = Column(String(150))
    dt_postcode = Column(String(6))
    dt_technical_director = Column(String(150))
    dt_quality_director = Column(String(150))
    dt_parameter = Column(String(150))
    dt_product_range = Column(String(150))
    dt_file = Column(String(1000))
    change_before_field = Column(String(1500))
    change_content = Column(String(1500))
    apply_user_id = Column(String(64), nullable=False)
    apply_time = Column(DateTime, nullable=False)
    apply_dt_id = Column(String(64), nullable=False)
    apply_reason = Column(String(900), nullable=False)
    audit_user_id = Column(String(64))
    audit_sv_id = Column(String(64))
    audit_time = Column(DateTime)
    audit_suggestion = Column(String(900))
    audit_state = Column(String(1))
    del_flag = Column(String(1))
    dt_level_id = Column(String(64))
    dt_nature_id = Column(String(64))
    dt_qualifications_id = Column(String(64))
    dt_type_id = Column(String(64))
    dt_area = Column(String(200))


class AsmsSubjDtRevoke(Base):
    __tablename__ = 'asms_subj_dt_revoke'

    id = Column(String(64), primary_key=True)
    dt_id = Column(String(64), nullable=False)
    apply_reason = Column(String(900), nullable=False)
    apply_user_id = Column(String(64), nullable=False)
    apply_sv_id = Column(String(64), nullable=False)
    apply_time = Column(DateTime, nullable=False)
    audit_user_id = Column(String(64))
    audit_sv_id = Column(String(64))
    audit_time = Column(DateTime)
    audit_suggestion = Column(String(900))
    audit_state = Column(String(1))
    del_flag = Column(String(1))


class AsmsSubjElCancel(Base):
    __tablename__ = 'asms_subj_el_cancel'

    id = Column(String(64), primary_key=True)
    el_id = Column(String(64), nullable=False)
    apply_reason = Column(String(1000), nullable=False)
    apply_user_id = Column(String(64), nullable=False)
    apply_time = Column(DateTime, nullable=False)
    audit_user_id = Column(String(64))
    audit_sv_id = Column(String(64))
    audit_time = Column(DateTime)
    audit_suggestion = Column(String(1000))
    audit_state = Column(String(1))
    del_flag = Column(String(1))


class AsmsSubjElChange(Base):
    __tablename__ = 'asms_subj_el_change'

    id = Column(String(64), primary_key=True)
    el_name = Column(String(200))
    el_code = Column(String(150))
    el_type = Column(String(100))
    el_level = Column(String(50))
    el_area_id = Column(String(64))
    el_address = Column(String(200))
    el_leader = Column(String(150))
    el_leader_phone = Column(String(20))
    el_contact = Column(String(150))
    el_contact_phone = Column(String(20))
    el_contact_q_q = Column(String(20))
    el_contact_email = Column(String(150))
    el_postcode = Column(String(6))
    el_unit_nature = Column(String(150))
    el_work_body = Column(String(150))
    el_file = Column(String(1000))
    change_before_field = Column(String(1500))
    change_content = Column(String(1500))
    apply_time = Column(DateTime, nullable=False)
    apply_user_id = Column(String(64), nullable=False)
    apply_el_id = Column(String(64), nullable=False)
    apply_reason = Column(String(900), nullable=False)
    audit_user_id = Column(String(64))
    audit_sv_id = Column(String(64))
    audit_time = Column(DateTime)
    audit_suggestion = Column(String(900))
    audit_state = Column(String(1))
    del_flag = Column(String(1))
    el_level_id = Column(String(64))
    el_type_id = Column(String(64))
    el_area = Column(String(200))
    el_people_num = Column(String(20))


class AsmsSubjElRevoke(Base):
    __tablename__ = 'asms_subj_el_revoke'

    id = Column(String(64), primary_key=True)
    el_id = Column(String(64), nullable=False)
    apply_reason = Column(String(1000), nullable=False)
    apply_user_id = Column(String(64), nullable=False)
    apply_sv_id = Column(String(64), nullable=False)
    apply_time = Column(DateTime, nullable=False)
    audit_user_id = Column(String(64))
    audit_sv_id = Column(String(64))
    audit_time = Column(DateTime)
    audit_suggestion = Column(String(1000))
    audit_state = Column(String(1))
    del_flag = Column(String(1))


class AsmsSubjEnforceLaw(Base):
    __tablename__ = 'asms_subj_enforce_law'

    id = Column(String(64), primary_key=True)
    el_name = Column(String(200), nullable=False)
    el_code = Column(String(150), nullable=False)
    el_type = Column(String(50))
    el_level = Column(String(64), nullable=False)
    el_area_id = Column(String(100), nullable=False)
    el_address = Column(String(200), nullable=False)
    el_leader = Column(String(150), nullable=False)
    el_leader_phone = Column(String(20))
    el_contact = Column(String(150), nullable=False)
    el_contact_phone = Column(String(20), nullable=False)
    el_contact_q_q = Column(String(20))
    el_contact_email = Column(String(150))
    el_postcode = Column(String(6))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    status = Column(String(1))
    el_unit_nature = Column(String(150))
    el_work_body = Column(String(200))
    del_flag = Column(String(1))
    el_level_id = Column(String(64))
    el_type_id = Column(String(64))
    el_area = Column(String(200))
    el_people_num = Column(String(20))


class AsmsSubjEntBadrecord(Base):
    __tablename__ = 'asms_subj_ent_badrecord'

    id = Column(String(64), primary_key=True)
    enterprise_id = Column(String(300))
    badrecord_content = Column(String(1000))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    badrecord_file = Column(String(1000))
    del_flag = Column(String(1))
    source_id = Column(String(64))
    source_type = Column(String(1))


class AsmsSubjEntTemp(Base):
    __tablename__ = 'asms_subj_ent_temp'

    id = Column(String(64), primary_key=True)
    entity_name = Column(String(200), nullable=False)
    entity_scale = Column(String(100), nullable=False)
    entity_scale_id = Column(String(64))
    entity_type = Column(String(200), nullable=False)
    entity_type_id = Column(String(64))
    entity_industry = Column(String(200))
    entity_industry_id = Column(String(520))
    cred_type = Column(String(20))
    cred_time = Column(String(100))
    org_code = Column(String(64), nullable=False)
    area_id = Column(String(100), nullable=False)
    contact_name = Column(String(200), nullable=False)
    contact_phone = Column(String(100))
    contact_email = Column(String(100))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    create_supervise_id = Column(String(64))
    update_by = Column(String(64))
    update_time = Column(DateTime)
    enable = Column(String(1))
    del_flag = Column(String(1), nullable=False)
    address = Column(String(200))
    identity_code = Column(String(64))


class AsmsSubjSupervise(Base):
    __tablename__ = 'asms_subj_supervise'

    id = Column(String(64), primary_key=True)
    sv_name = Column(String(150), nullable=False)
    sv_code = Column(String(150), nullable=False)
    sv_type = Column(String(100), nullable=False)
    sv_level = Column(String(100), nullable=False)
    sv_level_id = Column(String(64), nullable=False)
    sv_area_id = Column(String(64), nullable=False)
    sv_address = Column(String(150), nullable=False)
    sv_leader = Column(String(150), nullable=False)
    sv_leader_phone = Column(String(20))
    sv_contact = Column(String(150), nullable=False)
    sv_contact_phone = Column(String(20), nullable=False)
    sv_contact_q_q = Column(String(20))
    sv_contact_email = Column(String(150))
    sv_postcode = Column(String(6))
    create_by = Column(String(64), nullable=False)
    create_time = Column(DateTime, nullable=False)
    status = Column(String(1), nullable=False)
    del_flag = Column(String(1), nullable=False)
    sv_type_id = Column(String(64))
    sv_area = Column(String(200))


class AsmsSubjSvCancel(Base):
    __tablename__ = 'asms_subj_sv_cancel'

    id = Column(String(64), primary_key=True)
    sv_id = Column(String(64), nullable=False)
    apply_reason = Column(String(1000), nullable=False)
    apply_user_id = Column(String(64), nullable=False)
    apply_time = Column(DateTime, nullable=False)
    audit_user_id = Column(String(64))
    audit_sv_id = Column(String(64))
    audit_time = Column(DateTime)
    audit_suggestion = Column(String(1000))
    audit_state = Column(String(1))
    del_flag = Column(String(1))


class AsmsSubjSvChange(Base):
    __tablename__ = 'asms_subj_sv_change'

    id = Column(String(64), primary_key=True)
    sv_name = Column(String(150))
    sv_code = Column(String(150))
    sv_type = Column(String(100))
    sv_level = Column(String(100))
    sv_level_id = Column(String(64))
    sv_area_id = Column(String(64))
    sv_address = Column(String(150))
    sv_leader = Column(String(150))
    sv_leader_phone = Column(String(20))
    sv_contact = Column(String(150))
    sv_contact_phone = Column(String(20))
    sv_contact_q_q = Column(String(20))
    sv_contact_email = Column(String(150))
    sv_postcode = Column(String(6))
    sv_file = Column(String(1000))
    change_before_field = Column(String(1000))
    change_content = Column(String(1000))
    apply_user_id = Column(String(64), nullable=False)
    apply_time = Column(DateTime, nullable=False)
    apply_sv_id = Column(String(64), nullable=False)
    apply_reason = Column(String(900), nullable=False)
    audit_user_id = Column(String(64))
    audit_sv_id = Column(String(64))
    audit_time = Column(DateTime)
    audit_suggestion = Column(String(900))
    audit_state = Column(String(1))
    del_flag = Column(String(1))
    sv_type_id = Column(String(64))
    sv_area = Column(String(200))


class AsmsSubjSvRevoke(Base):
    __tablename__ = 'asms_subj_sv_revoke'

    id = Column(String(64), primary_key=True)
    sv_id = Column(String(64), nullable=False)
    apply_reason = Column(String(1000), nullable=False)
    apply_user_id = Column(String(64), nullable=False)
    apply_sv_id = Column(String(64), nullable=False)
    apply_time = Column(DateTime, nullable=False)
    audit_user_id = Column(String(64))
    audit_sv_id = Column(String(64))
    audit_time = Column(DateTime)
    audit_suggestion = Column(String(1000))
    audit_state = Column(String(1))
    del_flag = Column(String(1))


t_dbcopytest = Table(
    'dbcopytest', metadata,
    Column('remarks', String(10))
)


class OaLeave(Base):
    __tablename__ = 'oa_leave'

    id = Column(String(64), primary_key=True)
    process_instance_id = Column(String(64))
    user_id = Column(String(64))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    leave_type = Column(String(64))
    reason = Column(String(64))
    apply_time = Column(DateTime)
    reality_start_time = Column(DateTime)
    reality_end_time = Column(DateTime)


t_plan_table = Table(
    'plan_table', metadata,
    Column('statement_id', String(30)),
    Column('timestamp', DateTime),
    Column('remarks', String(80)),
    Column('operation', String(30)),
    Column('options', String(30)),
    Column('object_node', String(128)),
    Column('object_owner', String(30)),
    Column('object_name', String(30)),
    Column('object_instance', Numeric(38, 0, asdecimal=False)),
    Column('object_type', String(30)),
    Column('optimizer', String(255)),
    Column('search_columns', Numeric(asdecimal=False)),
    Column('id', Numeric(38, 0, asdecimal=False)),
    Column('parent_id', Numeric(38, 0, asdecimal=False)),
    Column('position', Numeric(38, 0, asdecimal=False)),
    Column('cost', Numeric(38, 0, asdecimal=False)),
    Column('cardinality', Numeric(38, 0, asdecimal=False)),
    Column('bytes', Numeric(38, 0, asdecimal=False)),
    Column('other_tag', String(255)),
    Column('partition_start', String(255)),
    Column('partition_stop', String(255)),
    Column('partition_id', Numeric(38, 0, asdecimal=False)),
    Column('other', Text),
    Column('distribution', String(30))
)


t_qrtz_cron_triggers = Table(
    'qrtz_cron_triggers', metadata,
    Column('sched_name', Unicode(120), nullable=False),
    Column('trigger_name', Unicode(200), nullable=False),
    Column('trigger_group', Unicode(200), nullable=False),
    Column('cron_expression', Unicode(200), nullable=False),
    Column('time_zone_id', Unicode(80))
)


t_qrtz_fired_triggers = Table(
    'qrtz_fired_triggers', metadata,
    Column('sched_name', Unicode(120), nullable=False),
    Column('entry_id', Unicode(95), nullable=False),
    Column('trigger_name', Unicode(200), nullable=False),
    Column('trigger_group', Unicode(200), nullable=False),
    Column('instance_name', Unicode(200), nullable=False),
    Column('fired_time', Numeric(20, 0, asdecimal=False), nullable=False),
    Column('sched_time', Numeric(20, 0, asdecimal=False), nullable=False),
    Column('priority', Numeric(11, 0, asdecimal=False), nullable=False),
    Column('state', Unicode(16), nullable=False),
    Column('job_name', Unicode(200)),
    Column('job_group', Unicode(200)),
    Column('is_nonconcurrent', Unicode(1)),
    Column('requests_recovery', Unicode(1))
)


t_qrtz_job_details = Table(
    'qrtz_job_details', metadata,
    Column('sched_name', Unicode(120), nullable=False),
    Column('job_name', Unicode(200), nullable=False),
    Column('job_group', Unicode(200), nullable=False),
    Column('description', Unicode(250)),
    Column('job_class_name', Unicode(250), nullable=False),
    Column('is_durable', Unicode(1), nullable=False),
    Column('is_nonconcurrent', Unicode(1), nullable=False),
    Column('is_update_data', Unicode(1), nullable=False),
    Column('requests_recovery', Unicode(1), nullable=False),
    Column('job_data', LargeBinary)
)


t_qrtz_locks = Table(
    'qrtz_locks', metadata,
    Column('sched_name', Unicode(120), nullable=False),
    Column('lock_name', Unicode(40), nullable=False)
)


t_qrtz_paused_trigger_grps = Table(
    'qrtz_paused_trigger_grps', metadata,
    Column('sched_name', Unicode(120), nullable=False),
    Column('trigger_group', Unicode(200), nullable=False)
)


t_qrtz_scheduler_state = Table(
    'qrtz_scheduler_state', metadata,
    Column('sched_name', Unicode(120), nullable=False),
    Column('instance_name', Unicode(200), nullable=False),
    Column('last_checkin_time', Numeric(20, 0, asdecimal=False), nullable=False),
    Column('checkin_interval', Numeric(20, 0, asdecimal=False), nullable=False)
)


t_qrtz_simple_triggers = Table(
    'qrtz_simple_triggers', metadata,
    Column('sched_name', Unicode(120), nullable=False),
    Column('trigger_name', Unicode(200), nullable=False),
    Column('trigger_group', Unicode(200), nullable=False),
    Column('repeat_count', Numeric(20, 0, asdecimal=False), nullable=False),
    Column('repeat_interval', Numeric(20, 0, asdecimal=False), nullable=False),
    Column('times_triggered', Numeric(20, 0, asdecimal=False), nullable=False)
)


t_qrtz_simprop_triggers = Table(
    'qrtz_simprop_triggers', metadata,
    Column('sched_name', Unicode(120), nullable=False),
    Column('trigger_name', Unicode(200), nullable=False),
    Column('trigger_group', Unicode(200), nullable=False),
    Column('str_prop_1', Unicode(512)),
    Column('str_prop_2', Unicode(512)),
    Column('str_prop_3', Unicode(512)),
    Column('int_prop_1', Numeric(11, 0, asdecimal=False)),
    Column('int_prop_2', Numeric(11, 0, asdecimal=False)),
    Column('long_prop_1', Numeric(20, 0, asdecimal=False)),
    Column('long_prop_2', Numeric(20, 0, asdecimal=False)),
    Column('dec_prop_1', Numeric(asdecimal=False)),
    Column('dec_prop_2', Numeric(asdecimal=False)),
    Column('bool_prop_1', Unicode(1)),
    Column('bool_prop_2', Unicode(1))
)


t_qrtz_triggers = Table(
    'qrtz_triggers', metadata,
    Column('sched_name', Unicode(120), nullable=False),
    Column('trigger_name', Unicode(200), nullable=False),
    Column('trigger_group', Unicode(200), nullable=False),
    Column('job_name', Unicode(200), nullable=False),
    Column('job_group', Unicode(200), nullable=False),
    Column('description', Unicode(250)),
    Column('next_fire_time', Numeric(20, 0, asdecimal=False)),
    Column('prev_fire_time', Numeric(20, 0, asdecimal=False)),
    Column('priority', Numeric(11, 0, asdecimal=False)),
    Column('trigger_state', Unicode(16), nullable=False),
    Column('trigger_type', Unicode(8), nullable=False),
    Column('start_time', Numeric(20, 0, asdecimal=False), nullable=False),
    Column('end_time', Numeric(20, 0, asdecimal=False)),
    Column('calendar_name', Unicode(200)),
    Column('misfire_instr', Numeric(6, 0, asdecimal=False)),
    Column('job_data', LargeBinary)
)


class SysArgiProduct(Base):
    __tablename__ = 'sys_argi_product'

    id = Column(String(64), primary_key=True)
    parent_id = Column(String(64))
    product_code = Column(String(100))
    use_code = Column(String(100))
    name = Column(String(100))
    alias = Column(String(255), server_default=text("NULL"))
    enname = Column(String(255), server_default=text("NULL"))
    gb_code = Column(String(255), server_default=text("NULL"))
    description = Column(String(1000))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    type_id = Column(String(64))
    parent_name = Column(String(255))


class SysCodeRule(Base):
    __tablename__ = 'sys_code_rule'

    id = Column(String(64), primary_key=True)
    rule_name = Column(String(64))
    rule_code = Column(String(64))
    create_by = Column(String(64))
    create_time = Column(DateTime, server_default=text("NULL"))
    update_by = Column(String(64))
    update_time = Column(DateTime, server_default=text("NULL"))
    del_flag = Column(String(1))
    reserved_field2 = Column(String(200))
    reserved_field1 = Column(Text)


class SysCodeRuleDatum(Base):
    __tablename__ = 'sys_code_rule_data'

    id = Column(String(64), primary_key=True)
    item_name = Column(String(64))
    item_val = Column(String(64))
    rule_id = Column(String(64))
    field_id = Column(String(64))
    sort_id = Column(String(32))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    field_name = Column(String(64))


class SysCodeRuleField(Base):
    __tablename__ = 'sys_code_rule_field'

    id = Column(String(64), primary_key=True)
    field_name = Column(String(64))
    rule_id = Column(String(64))
    sort_id = Column(String(32))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1))
    fixed = Column(String(1))
    group_mode = Column(String(32))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))


class SysDept(Base):
    __tablename__ = 'sys_dept'

    id = Column(String(64), primary_key=True)
    parent_id = Column(String(64))
    is_subitem = Column(String(1))
    dept_type = Column(String(64))
    dept_level = Column(String(64))
    region_id = Column(String(64))
    dept_name = Column(String(30))
    dept_manager = Column(String(50))
    phone = Column(String(50))
    status = Column(String(64))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))


class SysDictDatum(Base):
    __tablename__ = 'sys_dict_data'

    id = Column(String(64), primary_key=True)
    type_id = Column(String(64))
    categorie_id = Column(String(100))
    dict_code = Column(String(32), nullable=False, unique=True)
    dict_name = Column(String(100), nullable=False, unique=True)
    spell_name = Column(String(100))
    dict_value = Column(String(32), nullable=False)
    fixed = Column(String(1))
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    enable = Column(String(1))
    remark = Column(String(500))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    simple_name = Column(String(32))


class SysDictType(Base):
    __tablename__ = 'sys_dict_type'

    id = Column(String(64), primary_key=True)
    code = Column(String(32))
    pid = Column(String(64))
    name = Column(String(50))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    remark = Column(String(500))
    enable = Column(String(1))
    mark = Column(String(32))


class SysFlow(Base):
    __tablename__ = 'sys_flow'

    id = Column(String(64), primary_key=True)
    flow_name = Column(String(64))
    flow_file = Column(String(64))
    flow_img = Column(String(64))
    flow_url = Column(String(64))
    flow_flag = Column(String(50))
    status = Column(String(64))
    remark = Column(String(200))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))


class SysFlowActer(Base):
    __tablename__ = 'sys_flow_acter'

    id = Column(String(64), primary_key=True)
    flow_id = Column(String(64))
    flow_node_id = Column(String(64))
    role_id = Column(String(64))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))


class SysFlowNode(Base):
    __tablename__ = 'sys_flow_node'

    id = Column(String(64), primary_key=True)
    flow_id = Column(String(64))
    node_name = Column(String(64))
    node_code = Column(String(64))
    sortno = Column(String(64))
    status = Column(String(64))
    remark = Column(String(10))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))


class SysMenu(Base):
    __tablename__ = 'sys_menu'

    id = Column(String(64), primary_key=True)
    menu_name = Column(String(50))
    parent_id = Column(String(64))
    is_subitem = Column(Numeric(asdecimal=False))
    menu_type = Column(String(64))
    menu_value = Column(String(50))
    numbers = Column(String(64))
    url = Column(String(500))
    image = Column(String(500))
    describes = Column(String(500))
    status = Column(String(64))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))


class SysNoticerelease(Base):
    __tablename__ = 'sys_noticerelease'

    id = Column(String(64), primary_key=True)
    release_time = Column(DateTime, server_default=text("NULL"))
    release_person = Column(String(64))
    organ_id = Column(String(64))
    dept_id = Column(String(64))
    phone = Column(String(50))
    email = Column(String(50))
    user_type = Column(String(64))
    release_range = Column(String(64))
    notice_type = Column(String(64))
    title = Column(String(100))
    content = Column(String(4000))
    create_by = Column(String(64))
    create_time = Column(DateTime, server_default=text("NULL"))
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))


class SysOperateLog(Base):
    __tablename__ = 'sys_operate_log'

    id = Column(String(64), primary_key=True)
    operate_userid = Column(String(64))
    operate_username = Column(String(50))
    operate_time = Column(DateTime)
    operate_ip = Column(String(50))
    user_token = Column(String(100))
    visit_url = Column(String(500))
    visit_param = Column(String(500))
    status = Column(String(1))
    fail_info = Column(String(500))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    operate_type = Column(String(32), server_default=text("NULL "))
    operate_describe = Column(String(200))


class SysOrganization(Base):
    __tablename__ = 'sys_organization'

    id = Column(String(64), primary_key=True)
    org_name = Column(String(64))
    org_type = Column(String(64))
    org_level = Column(String(64))
    region_name = Column(String(64))
    type_id = Column(String(64))
    level_id = Column(String(64))
    region_id = Column(String(64))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    org_id = Column(String(64))


class SysPost(Base):
    __tablename__ = 'sys_post'

    id = Column(String(64), primary_key=True)
    dept_id = Column(String(64))
    post_type = Column(String(64))
    post_level = Column(String(64))
    post_name = Column(String(50))
    status = Column(String(64))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))


class SysRegion(Base):
    __tablename__ = 'sys_region'

    id = Column(String(64), primary_key=True)
    parent_id = Column(String(64))
    region_name = Column(String(50))
    region_code = Column(String(64))
    region_pinyin = Column(String(100))
    region_type = Column(String(64))
    region_fullname = Column(String(50))
    sortid = Column(Numeric(asdecimal=False))
    remark = Column(String(400))
    create_by = Column(String(64))
    create_time = Column(DateTime, server_default=text("NULL"))
    update_by = Column(String(64))
    update_time = Column(DateTime, server_default=text("NULL"))
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    status = Column(String(8))


class SysResource(Base):
    __tablename__ = 'sys_resource'

    id = Column(String(64), primary_key=True)
    resourcetype = Column(String(64))
    name = Column(String(64))
    professionalfiled = Column(String(255))
    jobtitle = Column(String(255))
    unit = Column(String(255))
    location = Column(String(255))
    address = Column(String(255))
    contract = Column(String(64))
    status = Column(String(64))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))


class SysRole(Base):
    __tablename__ = 'sys_role'

    id = Column(String(64), primary_key=True)
    dept_id = Column(String(64))
    role_name = Column(String(50))
    describe = Column(String(500))
    status = Column(String(64))
    sortid = Column(Numeric(asdecimal=False))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    organization_id = Column(String(64))
    role_code = Column(String(32))


class SysRoleMenu(Base):
    __tablename__ = 'sys_role_menu'

    id = Column(String(64), primary_key=True)
    role_id = Column(String(64), nullable=False)
    menu_id = Column(String(64), nullable=False)
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    authority = Column(String(1))


class SysRuleClas(Base):
    __tablename__ = 'sys_rule_class'

    id = Column(String(64), primary_key=True)
    rule_name = Column(String(100))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))


class SysTemplate(Base):
    __tablename__ = 'sys_template'

    id = Column(String(64), primary_key=True)
    template_name = Column(String(50))
    template_type = Column(String(64))
    template_filename = Column(String(50))
    remark = Column(String(500))
    status = Column(String(64))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    file_address = Column(String(255))
    pdf_address = Column(String(255))


class SysUser(Base):
    __tablename__ = 'sys_user'

    id = Column(String(64), primary_key=True)
    account = Column(String(64))
    password = Column(String(50))
    user_name = Column(String(50))
    dept_id = Column(String(64))
    role_id = Column(String(64))
    post_id = Column(String(64))
    phone = Column(String(50))
    email = Column(String(50))
    status = Column(String(64))
    create_by = Column(String(64))
    create_time = Column(DateTime, server_default=text("NULL"))
    update_by = Column(String(64))
    update_time = Column(DateTime, server_default=text("NULL"))
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200), server_default=text("""\
'0'
"""))
    reserved_field2 = Column(String(200))
    organization_id = Column(String(64))
    user_type = Column(String(16))


class SysUserRole(Base):
    __tablename__ = 'sys_user_role'

    id = Column(String(64), primary_key=True)
    user_id = Column(String(64), nullable=False)
    role_id = Column(String(64), nullable=False)
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(1), server_default=text("""\
'N'
"""))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))


class TDgapAlertConfig(Base):
    __tablename__ = 't_dgap_alert_config'

    id = Column(String(64), primary_key=True)
    alert_type = Column(String(20), nullable=False, server_default=text("NULL"))
    target_id = Column(String(64), nullable=False)
    description = Column(String(100), nullable=False)
    threshold = Column(Numeric(asdecimal=False), nullable=False)
    need_send_alert = Column(String(1), server_default=text("'Y'"))
    create_by = Column(String(64))
    create_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    update_by = Column(String(64))
    update_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    del_flag = Column(String(10), nullable=False, server_default=text("'N'"))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))


class TDgapAlertLog(Base):
    __tablename__ = 't_dgap_alert_log'

    id = Column(String(64), primary_key=True)
    alert_config_id = Column(ForeignKey(u't_dgap_alert_config.id'), nullable=False)
    target_id = Column(ForeignKey(u't_dgap_resource.id'), nullable=False)
    description = Column(String(100), nullable=False)
    alert_date = Column(DateTime, nullable=False)
    solve_date = Column(DateTime)
    solve_user_id = Column(String(64))
    solve_status = Column(String(10))
    create_by = Column(String(64))
    create_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    update_by = Column(String(64))
    update_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    del_flag = Column(String(10), nullable=False, server_default=text("'N'"))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))

    alert_config = relationship(u'TDgapAlertConfig')
    target = relationship(u'TDgapResource')


class TDgapAlertReceipt(Base):
    __tablename__ = 't_dgap_alert_receipt'

    id = Column(String(64), primary_key=True)
    alert_id = Column(ForeignKey(u't_dgap_alert_config.id'), nullable=False)
    receipt_by = Column(String(64), nullable=False)
    create_by = Column(String(64))
    create_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    update_by = Column(String(64))
    update_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    del_flag = Column(String(10), nullable=False, server_default=text("'N'"))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))

    alert = relationship(u'TDgapAlertConfig')


class TDgapDataImportField(Base):
    __tablename__ = 't_dgap_data_import_field'

    id = Column(String(64), primary_key=True)
    chinese_name = Column(String(20))
    english_name = Column(String(20))
    type = Column(String(64))
    len = Column(String(64))
    data_import_table_id = Column(ForeignKey(u't_dgap_data_import_table.id'))
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    update_by = Column(String(64), nullable=False)
    update_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    del_flag = Column(String(10), nullable=False, server_default=text("'N'"))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    status = Column(String(10))

    data_import_table = relationship(u'TDgapDataImportTable')


class TDgapDataImportTable(Base):
    __tablename__ = 't_dgap_data_import_table'

    id = Column(String(64), primary_key=True)
    chinese_name = Column(String(20))
    english_name = Column(String(20))
    resource_id = Column(ForeignKey(u't_dgap_resource.id'))
    status = Column(String(10))
    create_by = Column(String(64), nullable=False)
    create_date = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    update_by = Column(String(64), nullable=False)
    update_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    del_flag = Column(String(10), nullable=False, server_default=text("'N'"))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))

    resource = relationship(u'TDgapResource')


class TDgapResource(Base):
    __tablename__ = 't_dgap_resource'

    id = Column(String(64), primary_key=True)
    name = Column(String(30))
    type = Column(String(10))
    directory_id = Column(ForeignKey(u't_dgap_resource_directory.id'))
    description = Column(String(300))
    wsdl_url = Column(String(100))
    flag = Column(String(1), server_default=text("'Y'"))
    create_by = Column(String(64))
    create_time = Column(DateTime, server_default=text("SYSDATE"))
    update_by = Column(String(64))
    update_time = Column(DateTime, server_default=text("SYSDATE"))
    del_flag = Column(String(10), server_default=text("'N'"))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))

    directory = relationship(u'TDgapResourceDirectory')


class TDgapResourceApplication(Base):
    __tablename__ = 't_dgap_resource_application'

    id = Column(String(64), primary_key=True)
    resource_id = Column(ForeignKey(u't_dgap_resource.id'), nullable=False)
    user_id = Column(String(64), nullable=False)
    status = Column(String(10), nullable=False, server_default=text("'NEW'"))
    effective_date = Column(DateTime, nullable=False)
    expire_date = Column(DateTime)
    reason = Column(String(200), nullable=False)
    audit_user_id = Column(String(64))
    pass_or_not = Column(String(10))
    approval = Column(String(50))
    contact_number = Column(String(20))
    caller_token = Column(String(64), unique=True)
    create_by = Column(String(64))
    create_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    update_by = Column(String(64))
    update_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    del_flag = Column(String(10), nullable=False, server_default=text("'N'"))
    user_name = Column(String(50))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    audit_time = Column(DateTime)

    resource = relationship(u'TDgapResource')


class TDgapResourceDirectory(Base):
    __tablename__ = 't_dgap_resource_directory'

    id = Column(String(64), primary_key=True)
    name = Column(String(32), nullable=False, unique=True)
    description = Column(String(200))
    create_by = Column(String(64))
    create_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    update_by = Column(String(64))
    update_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    del_flag = Column(String(10), nullable=False, server_default=text("'N'"))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))


class TDgapRoleResource(Base):
    __tablename__ = 't_dgap_role_resource'

    id = Column(String(64), primary_key=True)
    role_id = Column(String(64), nullable=False)
    resource_id = Column(ForeignKey(u't_dgap_resource.id'), nullable=False)
    create_by = Column(String(64))
    create_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    update_by = Column(String(64))
    update_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    del_flag = Column(String(10), nullable=False, server_default=text("'N'"))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))

    resource = relationship(u'TDgapResource')


t_t_dgap_tb_resource_config = Table(
    't_dgap_tb_resource_config', metadata,
    Column('id', String(64)),
    Column('resource_id', String(64)),
    Column('table_name', String(64)),
    Column('table_cn_name', String(64)),
    Column('field_name', String(64)),
    Column('field_cn_name', String(64)),
    Column('length', Numeric(22, 0, asdecimal=False)),
    Column('type', String(20)),
    Column('is_condition', String(1)),
    Column('create_by', String(64), nullable=False),
    Column('create_date', DateTime, nullable=False, server_default=text("SYSDATE")),
    Column('update_by', String(64), nullable=False),
    Column('update_time', DateTime, nullable=False, server_default=text("SYSDATE")),
    Column('del_flag', String(10), nullable=False, server_default=text("'N'")),
    Column('reserved_field1', String(200)),
    Column('reserved_field2', String(200)),
    Column('reserved_field3', String(200)),
    Column('reserved_field4', String(200)),
    Column('reserved_field5', String(200)),
    Column('reserved_field6', String(200)),
    Column('reserved_field7', String(200)),
    Column('reserved_field8', String(200)),
    Column('reserved_field9', String(200)),
    Column('reserved_field10', String(200)),
    Column('reserved_field11', String(200)),
    Column('reserved_field12', String(200)),
    Column('reserved_field13', String(200)),
    Column('reserved_field14', String(200)),
    Column('reserved_field15', String(200)),
    Column('reserved_field16', String(200)),
    Column('reserved_field17', String(200)),
    Column('reserved_field18', String(200)),
    Column('reserved_field19', String(200)),
    Column('reserved_field20', String(200))
)


class TDgapWsDailyStat(Base):
    __tablename__ = 't_dgap_ws_daily_stat'

    id = Column(String(64), primary_key=True)
    stat_date = Column(DateTime, nullable=False)
    resource_dir = Column(ForeignKey(u't_dgap_resource_directory.id'))
    web_service_id = Column(ForeignKey(u't_dgap_resource.id'))
    web_service_name = Column(String(50))
    bussness_name = Column(String(50))
    caller_user = Column(String(64))
    success_times = Column(Numeric(scale=0, asdecimal=False), nullable=False)
    fail_times = Column(Numeric(scale=0, asdecimal=False), nullable=False)
    avg_timecost = Column(Numeric(scale=0, asdecimal=False), nullable=False)
    create_by = Column(String(64))
    create_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    update_by = Column(String(64))
    update_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    del_flag = Column(String(10), nullable=False, server_default=text("'N'"))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))

    t_dgap_resource_directory = relationship(u'TDgapResourceDirectory')
    web_service = relationship(u'TDgapResource')


class TDgapWsErrorLog(Base):
    __tablename__ = 't_dgap_ws_error_log'

    id = Column(String(64), primary_key=True)
    resource_directory_id = Column(ForeignKey(u't_dgap_resource_directory.id'))
    web_service_id = Column(ForeignKey(u't_dgap_resource.id'))
    web_service_name = Column(String(50))
    method_name = Column(String(50), nullable=False)
    caller_user = Column(String(64))
    error_type = Column(String(10), nullable=False)
    error_desc = Column(String(100), nullable=False)
    error_date = Column(DateTime, nullable=False)
    create_by = Column(String(64))
    create_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    update_by = Column(String(64))
    update_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    del_flag = Column(String(20), nullable=False, server_default=text("'N'"))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))

    resource_directory = relationship(u'TDgapResourceDirectory')
    web_service = relationship(u'TDgapResource')


class TDgapWsLog(Base):
    __tablename__ = 't_dgap_ws_log'

    id = Column(String(64), primary_key=True)
    resource_dir = Column(ForeignKey(u't_dgap_resource_directory.id'))
    web_service_id = Column(ForeignKey(u't_dgap_resource.id'))
    web_service_name = Column(String(50))
    method_name = Column(String(50), nullable=False)
    caller_user = Column(String(64))
    error_type = Column(String(10))
    error_desc = Column(String(100))
    invoke_start_date = Column(DateTime, nullable=False)
    invoke_end_date = Column(DateTime)
    error_date = Column(DateTime)
    create_by = Column(String(64))
    create_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    update_by = Column(String(64))
    update_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    del_flag = Column(String(10), nullable=False, server_default=text("'N'"))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))

    t_dgap_resource_directory = relationship(u'TDgapResourceDirectory')
    web_service = relationship(u'TDgapResource')


t_t_mdm_basic_code = Table(
    't_mdm_basic_code', metadata,
    Column('id', String(64), nullable=False, unique=True),
    Column('name', String(64)),
    Column('mark', String(256)),
    Column('abbreviation', String(64)),
    Column('status', String(1)),
    Column('codes_id', String(64)),
    Column('parent_id', String(64)),
    Column('parent_ids', String(64)),
    Column('create_by', String(64)),
    Column('createdate', DateTime),
    Column('update_by', String(64)),
    Column('updatedate', DateTime),
    Column('del_flag', String(1)),
    Column('remarks', String(255))
)


t_t_mdm_basic_codes = Table(
    't_mdm_basic_codes', metadata,
    Column('id', String(64), nullable=False),
    Column('name', String(64)),
    Column('format', String(256)),
    Column('status', String(1)),
    Column('normal', String(256)),
    Column('mark', String(256)),
    Column('description', String(256)),
    Column('batch', String(256)),
    Column('principle', String(256)),
    Column('parent_id', String(64)),
    Column('parent_ids', String(64)),
    Column('create_by', String(64)),
    Column('createdate', DateTime),
    Column('update_by', String(64)),
    Column('updatedate', DateTime),
    Column('del_flag', String(1)),
    Column('remarks', String(255))
)


class TScltxxcjBase(Base):
    __tablename__ = 't_scltxxcj_base'

    id = Column(String(64), primary_key=True)
    name = Column(String(64), nullable=False)
    area = Column(String(32))
    address = Column(String(64))
    manager = Column(String(32))
    phone = Column(String(32))
    product_names = Column(String(4000))
    longitude = Column(String(32))
    latitude = Column(String(32))
    picture = Column(String(1024))
    status = Column(String(32))
    ip = Column(String(140))
    create_by = Column(String(100))
    create_time = Column(DateTime)
    update_by = Column(String(100))
    del_flag = Column(String(1))
    update_time = Column(DateTime)
    picture_two = Column(String(1024))
    user_idcode = Column(String(64))
    entity_idcode = Column(String(64))
    address_code = Column(String(64))
    address_name = Column(String(100))


class TScltxxcjEntity(Base):
    __tablename__ = 't_scltxxcj_entity'

    id = Column(String(64), primary_key=True, nullable=False)
    entity_idcode = Column(String(300), primary_key=True, nullable=False)
    entity_scale = Column(String(30), nullable=False)
    entity_type = Column(String(30), nullable=False)
    entity_industry = Column(String(30), nullable=False)
    enterprise_name = Column(String(300))
    card_type = Column(String(1))
    credit_code = Column(String(20))
    business_operation = Column(String(30))
    enterprise_industry = Column(String(30))
    annual_output = Column(String(60), server_default=text("NULL"))
    address = Column(String(600), nullable=False, server_default=text("NULL "))
    area = Column(String(60), nullable=False, server_default=text("NULL "))
    longitude = Column(Numeric(10, 5))
    latitude = Column(Numeric(10, 5))
    contact_name = Column(String(300))
    contact_phone = Column(String(15))
    contact_email = Column(String(120))
    legal_name = Column(String(300), nullable=False)
    legal_idnumber = Column(String(20), nullable=False)
    legal_phone = Column(String(15), nullable=False)
    legal_images = Column(String(600), nullable=False)
    fax_number = Column(String(15))
    document_images = Column(String(600))
    blacklist_status = Column(String(1), nullable=False)
    del_flag = Column(String(1), nullable=False)
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    entity_idcode_image = Column(String(300))
    entity_property = Column(String(60))
    business_operation_start = Column(DateTime)
    business_operation_end = Column(DateTime)
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))


class TScltxxcjRegister(Base):
    __tablename__ = 't_scltxxcj_register'

    id = Column(String(64), primary_key=True)
    account = Column(String(60), nullable=False)
    password = Column(String(50), nullable=False)
    real_name = Column(String(300), nullable=False)
    idcode = Column(String(18), nullable=False)
    entity_scale = Column(String(30), nullable=False)
    entity_type = Column(String(30))
    entity_property = Column(String(60))
    entity_industry = Column(String(100))
    enterprise_name = Column(String(300))
    card_type = Column(String(1))
    credit_code = Column(String(20))
    business_operation = Column(String(30))
    enterprise_industry = Column(String(30))
    annual_output = Column(String(60), server_default=text("NULL"))
    address = Column(String(600), nullable=False, server_default=text("NULL "))
    area = Column(String(60), nullable=False, server_default=text("NULL "))
    longitude = Column(Numeric(10, 5))
    latitude = Column(Numeric(10, 5))
    legal_name = Column(String(300), nullable=False)
    legal_idnumber = Column(String(20), nullable=False)
    legal_phone = Column(String(15), nullable=False)
    legal_images = Column(String(600), nullable=False)
    fax_number = Column(String(15))
    contact_name = Column(String(300))
    contact_phone = Column(String(15))
    contact_email = Column(String(120))
    document_images = Column(String(600))
    register_time = Column(DateTime, nullable=False)
    approve_status = Column(String(1), nullable=False)
    approve_opinion = Column(String(300))
    approve_user_idcode = Column(String(300))
    approve_name = Column(String(300))
    approve_time = Column(DateTime)
    user_idcode = Column(String(64))
    entity_idcode = Column(String(64))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))


t_task_fire_log = Table(
    'task_fire_log', metadata,
    Column('id_', Unicode(64), nullable=False),
    Column('group_name', Unicode(50), nullable=False),
    Column('task_name', Unicode(50), nullable=False),
    Column('start_time', DateTime, nullable=False),
    Column('end_time', DateTime),
    Column('status', Unicode(1), nullable=False),
    Column('server_host', Unicode(50)),
    Column('server_duid', Unicode(50)),
    Column('fire_info', Text)
)


t_task_group = Table(
    'task_group', metadata,
    Column('id_', Unicode(64), nullable=False),
    Column('group_name', Unicode(50), nullable=False),
    Column('group_desc', Unicode(50), nullable=False),
    Column('enable_', Numeric(4, 0, asdecimal=False)),
    Column('create_time', DateTime, nullable=False),
    Column('create_by', Unicode(64), nullable=False),
    Column('update_time', DateTime, nullable=False),
    Column('update_by', Unicode(64), nullable=False)
)


t_task_scheduler = Table(
    'task_scheduler', metadata,
    Column('id_', Unicode(64), nullable=False),
    Column('group_id', Unicode(64), nullable=False),
    Column('task_name', Unicode(50), nullable=False),
    Column('task_type', Unicode(50), nullable=False),
    Column('task_desc', Unicode(50)),
    Column('task_cron', Unicode(50), nullable=False),
    Column('task_previous_fire_time', DateTime, nullable=False),
    Column('task_next_fire_time', DateTime, nullable=False),
    Column('contact_email', Unicode(500)),
    Column('enable_', Numeric(4, 0, asdecimal=False)),
    Column('create_by', Unicode(64), nullable=False),
    Column('create_time', DateTime, nullable=False),
    Column('update_by', Unicode(64), nullable=False),
    Column('update_time', DateTime, nullable=False)
)


class TempDemo(Base):
    __tablename__ = 'temp_demo'

    id = Column(String(200), primary_key=True)
    name = Column(String(200))
    tel = Column(Numeric(scale=0, asdecimal=False))
    cjrq = Column(DateTime)


t_temprory_demo = Table(
    'temprory_demo', metadata,
    Column('id', String(100)),
    Column('name', String(20)),
    Column('age', String(10)),
    Column('sex', String(10))
)


class TtsScltxxcjCggl(Base):
    __tablename__ = 'tts_scltxxcj_cggl'

    id = Column(String(64), primary_key=True)
    product_name = Column(String(200))
    product_id = Column(String(200))
    product_industry = Column(String(200))
    product_sort = Column(String(200))
    product_scgl_id = Column(String(200))
    cg_amount = Column(Numeric(16, 4))
    entity_idcode = Column(String(200))
    user_idcode = Column(String(300))
    sale_entity_idcode = Column(String(200))
    sale_user_idcode = Column(String(300))
    confirm_state = Column(String(1))
    trace_code = Column(String(100))
    sale_time = Column(DateTime)
    confirm_time = Column(DateTime)
    product_model = Column(String(100))
    buy_com_user_id = Column(String(200))
    sale_user = Column(String(100))
    ip_address = Column(String(140))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    update_by = Column(String(64))
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    fromzsm = Column(String(200))
    tozsm = Column(String(200))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    product_cgpc = Column(String(200))
    product_cgpc_sl = Column(String(20))
    xsdjid = Column(String(200))
    zjcheck = Column(String(200))
    cg_dw = Column(String(200))
    zjresult = Column(String(200))
    unit_id = Column(String(64))


class TtsScltxxcjComplaint(Base):
    __tablename__ = 'tts_scltxxcj_complaint'

    id = Column(String(64), primary_key=True)
    entity_idcode = Column(String(100))
    user_idcode = Column(String(100))
    be_entity_idcode = Column(String(100))
    be_user_idcode = Column(String(100))
    acc_entity_idcode = Column(String(100))
    acc_user_idcode = Column(String(100))
    complaint_time = Column(DateTime)
    complaint_title = Column(String(200))
    content = Column(String(4000))
    type = Column(String(100))
    status = Column(String(1))
    acceptance = Column(String(2000))
    area_id = Column(String(100))
    acc_time = Column(DateTime)
    attachment_name = Column(String(200))
    complaint_ent_name = Column(String(100))
    attachment_path = Column(String(200))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    update_by = Column(String(64))
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    complaint_cop_name = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    type_name = Column(String(200))


class TtsScltxxcjCppchc(Base):
    __tablename__ = 'tts_scltxxcj_cppchc'

    id = Column(String(64), primary_key=True, nullable=False)
    hcid = Column(String(64), primary_key=True, nullable=False)
    product_id = Column(String(200))
    product_name = Column(String(64))
    medi_check = Column(String(100))
    medi_result = Column(String(100))
    product_amount = Column(Numeric(scale=0, asdecimal=False))
    store_count = Column(Numeric(scale=0, asdecimal=False))
    harvest_time = Column(DateTime)
    product_pc = Column(String(250))
    product_pc_new = Column(String(250))
    harvest_baseid = Column(String(100))
    harvest_basename = Column(String(100))
    product_inner_key = Column(String(200))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    update_by = Column(String(64))
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    product_source = Column(String(64))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    status = Column(String(100))
    bill_stratrus = Column(String(100))
    fromzsm = Column(String(200))
    hczsm = Column(String(200))


class TtsScltxxcjCustomer(Base):
    __tablename__ = 'tts_scltxxcj_customer'

    id = Column(String(64), primary_key=True)
    name = Column(String(255))
    type = Column(String(255))
    organization_type = Column(String(255))
    legal_representative = Column(String(255))
    user_name = Column(String(64))
    id_card_no = Column(String(64))
    phone = Column(String(64))
    email = Column(String(255))
    address = Column(String(500))
    status = Column(String(38))
    createtime = Column(DateTime)
    entity_id_code = Column(String(255))
    user_id_code = Column(String(255))
    customer_entity_id_code = Column(String(255))
    customer_user_id_code = Column(String(255))
    ip_address = Column(String(64))
    delflag = Column(String(1))
    createby = Column(String(64))
    updateby = Column(String(64))
    updatetime = Column(DateTime)


class TtsScltxxcjEntity(Base):
    __tablename__ = 'tts_scltxxcj_entity'

    id = Column(String(64), primary_key=True, nullable=False)
    entity_idcode = Column(String(300), primary_key=True, nullable=False)
    entity_scale = Column(String(30), nullable=False)
    entity_type = Column(String(30), nullable=False)
    entity_industry = Column(String(30), nullable=False)
    enterprise_name = Column(String(300))
    card_type = Column(String(1))
    credit_code = Column(String(20))
    business_operation = Column(String(30))
    business_operation_start = Column(String(64))
    business_operation_end = Column(String(64))
    enterprise_industry = Column(String(30))
    annual_output = Column(String(60), server_default=text("NULL"))
    address = Column(String(600), nullable=False, server_default=text("NULL "))
    area = Column(String(60), nullable=False, server_default=text("NULL "))
    longitude = Column(Numeric(10, 5))
    latitude = Column(Numeric(10, 5))
    contact_name = Column(String(300))
    contact_phone = Column(String(15))
    contact_email = Column(String(120))
    legal_name = Column(String(300), nullable=False)
    legal_idnumber = Column(String(20), nullable=False)
    legal_phone = Column(String(15), nullable=False)
    legal_images = Column(String(600), nullable=False)
    fax_number = Column(String(15))
    document_images = Column(String(600))
    blacklist_status = Column(String(1), nullable=False)
    del_flag = Column(String(1), nullable=False)
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))


class TtsScltxxcjNotification(Base):
    __tablename__ = 'tts_scltxxcj_notification'

    id = Column(String(64), primary_key=True)
    be_entity_idcode = Column(String(64))
    be_user_idcode = Column(String(64))
    entity_idcode = Column(String(64))
    user_idcode = Column(String(64))
    title = Column(String(200))
    content = Column(String(1000))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    del_flag = Column(String(2))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))


class TtsScltxxcjProduct(Base):
    __tablename__ = 'tts_scltxxcj_product'

    id = Column(String(64), primary_key=True)
    industry = Column(String(400))
    name = Column(String(400))
    type = Column(String(255))
    model = Column(String(255))
    picture = Column(String(1024))
    status = Column(String(32))
    self_check = Column(String(64))
    authentication = Column(String(64))
    ip = Column(String(140))
    create_by = Column(String(32))
    create_time = Column(DateTime)
    update_by = Column(String(32))
    update_time = Column(DateTime)
    del_flag = Column(String(1))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    user_idcode = Column(String(64))
    entity_idcode = Column(String(64))
    product_code = Column(String(100))
    type_name = Column(String(100))


class TtsScltxxcjProductType(Base):
    __tablename__ = 'tts_scltxxcj_product_type'

    id = Column(String(64), primary_key=True)
    name = Column(String(100))
    status = Column(String(2))
    create_time = Column(DateTime)
    create_by = Column(String(50))
    update_time = Column(DateTime)
    update_by = Column(String(50))
    del_flag = Column(String(1))
    type_code = Column(String(150))
    user_idcode = Column(String(64))
    entity_idcode = Column(String(64))


class TtsScltxxcjProductionManage(Base):
    __tablename__ = 'tts_scltxxcj_production_manage'

    id = Column(String(64), primary_key=True)
    product_id = Column(String(64))
    product_name = Column(String(400))
    product_type = Column(String(255))
    product_industry = Column(String(255))
    product_sort = Column(String(255))
    product_amount = Column(String(255))
    freeze_count = Column(String(255))
    store_count = Column(String(255))
    harvest_unit = Column(String(255))
    harvest_time = Column(DateTime)
    product_pc = Column(String(64))
    check_imagename = Column(String(255))
    check_imagepath = Column(String(255))
    product_inner_key = Column(String(100))
    product_source = Column(String(255))
    medi_check = Column(String(100))
    medi_result = Column(String(100))
    harvest_baseid = Column(String(100))
    harvest_basename = Column(String(255))
    statrus = Column(String(1))
    bill_stratrus = Column(String(1))
    ip = Column(String(140))
    create_by = Column(String(32))
    create_time = Column(DateTime)
    update_by = Column(String(32))
    update_time = Column(DateTime)
    enable = Column(String(1))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))


class TtsScltxxcjProductypename(Base):
    __tablename__ = 'tts_scltxxcj_productypename'

    id = Column(String(32), primary_key=True)
    product_name = Column(String(255))
    product_unit = Column(String(255))
    ip = Column(String(140))
    createby = Column(String(32))
    createtime = Column(DateTime)
    updateby = Column(String(32))
    updatetime = Column(DateTime)
    del_flag = Column(String(1))
    product_slaughter_name = Column(String(255))
    product_id = Column(String(64))


class TtsScltxxcjProposal(Base):
    __tablename__ = 'tts_scltxxcj_proposal'

    id = Column(String(64), primary_key=True)
    title = Column(String(200))
    content = Column(String(4000))
    time = Column(DateTime)
    attach_name = Column(String(100))
    attach_path = Column(String(300))
    entity_idcode = Column(String(64))
    user_idcode = Column(String(64))
    ip = Column(String(140))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    update_by = Column(String(64))
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))


class TtsScltxxcjRegister(Base):
    __tablename__ = 'tts_scltxxcj_register'

    id = Column(String(64), primary_key=True)
    account = Column(String(60), nullable=False)
    real_name = Column(String(300), nullable=False)
    idcode = Column(String(18), nullable=False)
    entity_scale = Column(String(700), nullable=False)
    entity_type = Column(String(700))
    entity_property = Column(String(700))
    entity_industry = Column(String(700))
    enterprise_name = Column(String(300))
    card_type = Column(String(64))
    credit_code = Column(String(20))
    business_operation = Column(String(30))
    business_operation_start = Column(DateTime)
    business_operation_end = Column(DateTime)
    enterprise_industry = Column(String(30))
    annual_output = Column(String(60), server_default=text("NULL"))
    unit = Column(String(100))
    address = Column(String(600), nullable=False, server_default=text("NULL "))
    document_images = Column(String(600))
    area = Column(String(60), nullable=False, server_default=text("NULL "))
    longitude = Column(Numeric(20, 14))
    latitude = Column(Numeric(20, 14))
    legal_name = Column(String(300), nullable=False)
    legal_idnumber = Column(String(20), nullable=False)
    legal_phone = Column(String(15), nullable=False)
    legal_images = Column(String(600), nullable=False)
    fax_number = Column(String(15))
    contact_name = Column(String(300))
    contact_phone = Column(String(15))
    contact_email = Column(String(120))
    register_time = Column(DateTime, nullable=False)
    approve_status = Column(String(1), nullable=False)
    approve_opinion = Column(String(300))
    approve_user_idcode = Column(String(300))
    approve_name = Column(String(300))
    approve_time = Column(DateTime)
    user_idcode = Column(String(64))
    entity_idcode = Column(String(64))
    del_flag = Column(String(1), nullable=False)
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    entity_scale_name = Column(String(200))
    entity_type_name = Column(String(200))
    entity_property_name = Column(String(200))
    entity_industry_name = Column(String(200))
    unit_name = Column(String(100))
    business_licenceimg = Column(String(200))
    organization_certificateimg = Column(String(200))
    positive_idcardeimg = Column(String(200))
    negative_idcardimg = Column(String(200))
    hand_idcardimg = Column(String(200))
    organization_code = Column(String(20))
    is_long = Column(String(20))


class TtsScltxxcjScgl(Base):
    __tablename__ = 'tts_scltxxcj_scgl'

    id = Column(String(64), primary_key=True)
    product_name = Column(String(200), nullable=False)
    product_id = Column(String(64), nullable=False)
    product_sort = Column(String(200), nullable=False)
    user_idcode = Column(String(300), nullable=False)
    product_industry = Column(String(200))
    product_amount = Column(Numeric(16, 4))
    store_count = Column(Numeric(16, 4))
    freeze_count = Column(Numeric(16, 4))
    harvest_unit = Column(String(64), nullable=False)
    harvest_time = Column(DateTime)
    product_pc = Column(String(100))
    medi_check = Column(String(100))
    check_imagename = Column(String(200))
    check_imagepath = Column(String(200))
    product_inner_key = Column(String(100))
    medi_result = Column(String(100))
    product_source = Column(String(100))
    harvest_baseid = Column(String(64))
    harvest_basename = Column(String(100))
    status = Column(String(10))
    bill_stratrus = Column(String(1))
    ip = Column(String(140))
    create_time = Column(DateTime)
    create_by = Column(String(200))
    update_time = Column(DateTime)
    update_by = Column(String(200))
    enable = Column(String(1))
    entity_idcode = Column(String(64))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    del_flag = Column(String(1))
    join_flag = Column(String(1))
    fromzsm = Column(String(200))
    unit_id = Column(String(64))
    inside_trace_code = Column(String(100))


class TtsScltxxcjSlaPurchase(Base):
    __tablename__ = 'tts_scltxxcj_sla_purchase'

    id = Column(String(64), primary_key=True)
    product_name = Column(String(200))
    product_id = Column(String(200))
    product_industry = Column(String(200))
    product_sort = Column(String(200))
    product_scgl_id = Column(String(200))
    cg_amount = Column(Numeric(16, 4))
    entity_idcode = Column(String(200))
    user_idcode = Column(String(300))
    sale_entity_idcode = Column(String(200))
    sale_user_idcode = Column(String(300))
    confirm_state = Column(String(1))
    trace_code = Column(String(100))
    sale_time = Column(DateTime)
    confirm_time = Column(DateTime)
    product_model = Column(String(100))
    buy_com_user_id = Column(String(200))
    sale_user = Column(String(100))
    ip_address = Column(String(140))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    update_by = Column(String(64))
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    from_trace_code = Column(String(200))
    to_trace_code = Column(String(200))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    product_cgpc = Column(String(200))
    product_cgpc_sl = Column(String(20))
    xsdjid = Column(String(200))
    zjcheck = Column(String(200))
    cg_dw = Column(String(200))
    zjresult = Column(String(200))


class TtsScltxxcjSlaughterPchc(Base):
    __tablename__ = 'tts_scltxxcj_slaughter_pchc'

    id = Column(String(64), primary_key=True)
    product_name = Column(String(400))
    product_unit = Column(String(400))
    product_type = Column(String(400))
    slaughter_batch_no = Column(String(400))
    init_amount = Column(Numeric(16, 2))
    current_amount = Column(Numeric(16, 2))
    status = Column(String(64))
    inside_trace_code = Column(String(100))
    ip = Column(String(140))
    create_by = Column(String(32))
    create_time = Column(DateTime)
    update_by = Column(String(32))
    update_time = Column(DateTime)
    del_flag = Column(String(1))
    slaughter_batch_no_new = Column(String(400))
    bill_stratrus = Column(String(400))
    product_id = Column(String(64))
    product_hc_id = Column(String(64), server_default=text("''  "))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))


class TtsScltxxcjSlaughterRecord(Base):
    __tablename__ = 'tts_scltxxcj_slaughter_record'

    id = Column(String(64), primary_key=True)
    slaughter_time = Column(DateTime)
    name = Column(String(400))
    product_pc = Column(String(100))
    ip = Column(String(140))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    update_by = Column(String(64))
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    inside_trace_code = Column(String(100))
    slaughter_amount = Column(String(255))


class TtsScltxxcjSlaughterSale(Base):
    __tablename__ = 'tts_scltxxcj_slaughter_sale'

    id = Column(String(64), primary_key=True)
    product_name = Column(String(200))
    product_id = Column(String(200))
    product_industry = Column(String(200))
    product_sort = Column(String(200))
    product_scgl_id = Column(String(200))
    sale_amount = Column(Numeric(16, 4))
    entity_idcode = Column(String(200))
    user_idcode = Column(String(300))
    customer_entity_idcode = Column(String(200))
    customer_user_idcode = Column(String(300))
    is_circulates_end = Column(String(1))
    confirm_state = Column(String(1))
    to_trace_code = Column(String(100))
    trace_proof = Column(String(100))
    sale_time = Column(DateTime)
    confirm_time = Column(DateTime)
    product_model = Column(String(100))
    buy_com_user_id = Column(String(200))
    sale_user = Column(String(100))
    ip_address = Column(String(140))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    update_by = Column(String(64))
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    fromid = Column(String(64))
    stockid = Column(String(64))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    product_xspc = Column(String(200))
    product_xspc_sl = Column(String(20))
    customer_id = Column(String(200))
    from_trace_code = Column(String(100))
    trace_code = Column(String(100))


class TtsScltxxcjSlaughterSrecord(Base):
    __tablename__ = 'tts_scltxxcj_slaughter_srecord'

    id = Column(String(64), primary_key=True)
    product_name = Column(String(200))
    product_id = Column(String(200))
    product_industry = Column(String(200))
    product_sort = Column(String(200))
    product_scgl_id = Column(String(200))
    sale_amount = Column(Numeric(16, 4))
    entity_idcode = Column(String(200))
    user_idcode = Column(String(300))
    customer_entity_idcode = Column(String(200))
    customer_user_idcode = Column(String(300))
    is_circulates_end = Column(String(1))
    confirm_state = Column(String(1))
    trace_code = Column(String(100))
    trace_proof = Column(String(100))
    sale_time = Column(DateTime)
    confirm_time = Column(DateTime)
    product_model = Column(String(100))
    buy_com_user_id = Column(String(64))
    sale_user = Column(String(100))
    ip_address = Column(String(140))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    update_by = Column(String(64))
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    product_xspc = Column(String(200))
    xsdj_id = Column(String(200))
    customer_id = Column(String(200))
    from_trace_code = Column(String(100))
    to_trace_code = Column(String(100))


class TtsScltxxcjSlaughterStor(Base):
    __tablename__ = 'tts_scltxxcj_slaughter_stor'

    id = Column(String(64), primary_key=True)
    product_name = Column(String(400))
    product_unit = Column(String(400))
    product_type = Column(String(400))
    slaughter_batch_no = Column(String(400))
    init_amount = Column(Numeric(16, 2))
    current_amount = Column(Numeric(16, 2))
    status = Column(String(64))
    inside_trace_code = Column(String(100))
    ip = Column(String(140))
    create_by = Column(String(32))
    create_time = Column(DateTime)
    update_by = Column(String(32))
    update_time = Column(DateTime)
    del_flag = Column(String(1))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200), server_default=text("''  "))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    bill_stratrus = Column(String(1))
    harvest_time = Column(DateTime)
    sale_amount = Column(Numeric(16, 2), server_default=text("0.00  "))
    user_idcode = Column(String(300))
    freeze_count = Column(Numeric(16, 2))
    entity_idcode = Column(String(64))
    from_trace_code = Column(String(100))
    to_trace_code = Column(String(100))
    unit = Column(String(32))


class TtsScltxxcjUser(Base):
    __tablename__ = 'tts_scltxxcj_user'

    id = Column(String(64), primary_key=True)
    account = Column(String(64), nullable=False)
    user_idcode = Column(String(64))
    entity_idcode = Column(String(64))
    is_main = Column(String(1))
    status = Column(String(64))
    create_time = Column(DateTime, nullable=False)
    create_by = Column(String(64))
    update_by = Column(String(64))
    del_flag = Column(String(1))
    update_time = Column(DateTime)
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    name = Column(String(64))
    phone = Column(String(64))
    email = Column(String(64))
    password = Column(String(64))
    id_card = Column(String(64), unique=True)


class TtsScltxxcjUserChangerecord(Base):
    __tablename__ = 'tts_scltxxcj_user_changerecord'

    id = Column(String(64), primary_key=True)
    account = Column(String(60), nullable=False)
    real_name = Column(String(300), nullable=False)
    idcode = Column(String(18), nullable=False)
    entity_scale = Column(String(700), nullable=False)
    entity_type = Column(String(700))
    entity_property = Column(String(700))
    entity_industry = Column(String(700))
    enterprise_name = Column(String(300))
    card_type = Column(String(64))
    credit_code = Column(String(20))
    business_operation = Column(String(30))
    business_operation_start = Column(DateTime)
    business_operation_end = Column(DateTime)
    enterprise_industry = Column(String(30))
    annual_output = Column(String(60), server_default=text("NULL"))
    address = Column(String(600), nullable=False, server_default=text("NULL "))
    document_images = Column(String(600))
    area = Column(String(60), nullable=False, server_default=text("NULL "))
    longitude = Column(Numeric(10, 5))
    latitude = Column(Numeric(10, 5))
    legal_name = Column(String(300), nullable=False)
    legal_idnumber = Column(String(20), nullable=False)
    legal_phone = Column(String(15), nullable=False)
    legal_images = Column(String(600), nullable=False)
    fax_number = Column(String(15))
    contact_name = Column(String(300))
    contact_phone = Column(String(15))
    contact_email = Column(String(120))
    register_time = Column(DateTime, nullable=False)
    approve_status = Column(String(1), nullable=False)
    approve_opinion = Column(String(300))
    approve_user_idcode = Column(String(300))
    approve_name = Column(String(300))
    approve_time = Column(DateTime)
    user_idcode = Column(String(64))
    entity_idcode = Column(String(64))
    approve_type = Column(String(64), nullable=False)
    reason = Column(String(1000), nullable=False)
    update_content = Column(String(1000))
    apply_user_id = Column(String(64), nullable=False)
    apply_update_name = Column(String(300), nullable=False)
    apply_update_entity_idcode = Column(String(300))
    apply_update_user_idcode = Column(String(300))
    apply_update_time = Column(DateTime, nullable=False)
    del_flag = Column(String(1), nullable=False)
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    entity_scale_name = Column(String(200))
    entity_type_name = Column(String(200))
    entity_property_name = Column(String(200))
    entity_industry_name = Column(String(200))
    update_before_json = Column(String(4000))
    unit = Column(String(100))
    unit_name = Column(String(100))
    entity_id = Column(String(64))
    business_licenceimg = Column(String(200))
    organization_certificateimg = Column(String(200))
    positive_idcardeimg = Column(String(200))
    negative_idcardimg = Column(String(200))
    hand_idcardimg = Column(String(200))
    organization_code = Column(String(20))
    is_long = Column(String(20))


class TtsScltxxcjUsernumber(Base):
    __tablename__ = 'tts_scltxxcj_usernumber'

    id = Column(String(64), primary_key=True)
    entity_idcode = Column(String(100))
    user_number = Column(Numeric(scale=0, asdecimal=False))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    update_by = Column(String(64))
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))


class TtsScltxxcjXsdj(Base):
    __tablename__ = 'tts_scltxxcj_xsdj'

    id = Column(String(64), primary_key=True)
    product_name = Column(String(200))
    product_id = Column(String(200))
    product_industry = Column(String(200))
    product_sort = Column(String(200))
    product_scgl_id = Column(String(200))
    sale_amount = Column(Numeric(16, 4))
    entity_idcode = Column(String(200))
    user_idcode = Column(String(300))
    customer_entity_idcode = Column(String(200))
    customer_user_idcode = Column(String(300))
    is_circulates_end = Column(String(1))
    confirm_state = Column(String(1))
    trace_code = Column(String(100))
    trace_proof = Column(String(100))
    sale_time = Column(DateTime)
    confirm_time = Column(DateTime)
    product_model = Column(String(100))
    buy_com_user_id = Column(String(200))
    sale_user = Column(String(100))
    ip_address = Column(String(140))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    update_by = Column(String(64))
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    fromid = Column(String(64))
    stockid = Column(String(64))
    reserved_field1 = Column(String(200))
    reserved_field2 = Column(String(200))
    reserved_field3 = Column(String(200))
    reserved_field4 = Column(String(200))
    reserved_field5 = Column(String(200))
    reserved_field6 = Column(String(200))
    reserved_field7 = Column(String(200))
    reserved_field8 = Column(String(200))
    reserved_field9 = Column(String(200))
    reserved_field10 = Column(String(200))
    reserved_field11 = Column(String(200))
    reserved_field12 = Column(String(200))
    reserved_field13 = Column(String(200))
    reserved_field14 = Column(String(200))
    reserved_field15 = Column(String(200))
    reserved_field16 = Column(String(200))
    reserved_field17 = Column(String(200))
    reserved_field18 = Column(String(200))
    reserved_field19 = Column(String(200))
    reserved_field20 = Column(String(200))
    product_xspc = Column(String(200))
    product_xspc_sl = Column(String(20))
    customer_id = Column(String(200))
    zjcheck = Column(String(200))
    fromzsm = Column(String(200))
    tozsm = Column(String(200))
    harvest_unit = Column(String(20))
    join_flag = Column(String(1))
    unit_id = Column(String(64))


t_tts_scltxxcj_xsdjjl = Table(
    'tts_scltxxcj_xsdjjl', metadata,
    Column('id', String(64), nullable=False),
    Column('product_name', String(200)),
    Column('product_id', String(200)),
    Column('product_industry', String(200)),
    Column('product_sort', String(200)),
    Column('product_scgl_id', String(200)),
    Column('sale_amount', Numeric(16, 4)),
    Column('entity_idcode', String(200)),
    Column('user_idcode', String(300)),
    Column('customer_entity_idcode', String(200)),
    Column('customer_user_idcode', String(300)),
    Column('is_circulates_end', String(1)),
    Column('confirm_state', String(1)),
    Column('trace_code', String(100)),
    Column('trace_proof', String(100)),
    Column('sale_time', DateTime),
    Column('confirm_time', DateTime),
    Column('product_model', String(100)),
    Column('buy_com_user_id', String(64)),
    Column('sale_user', String(100)),
    Column('ip_address', String(140)),
    Column('del_flag', String(1)),
    Column('create_by', String(64)),
    Column('update_by', String(64)),
    Column('create_time', DateTime),
    Column('update_time', DateTime),
    Column('product_xspc', String(200)),
    Column('xsdj_id', String(200)),
    Column('customer_id', String(200)),
    Column('zjcheck', String(200)),
    Column('fromzsm', String(200)),
    Column('tozsm', String(200))
)


class TtsScltxxcjXsth(Base):
    __tablename__ = 'tts_scltxxcj_xsth'

    id = Column(String(64), primary_key=True)
    xsjlid = Column(String(64))
    product_name = Column(String(200))
    product_id = Column(String(200))
    product_industry = Column(String(200))
    product_sort = Column(String(200))
    sale_amount = Column(Numeric(16, 4))
    sale_time = Column(DateTime)
    sale_user = Column(String(100))
    product_xspc = Column(String(200))
    product_xspc_sl = Column(String(20))
    buy_com_user_id = Column(String(200))
    customer_entity_idcode = Column(String(200))
    customer_user_idcode = Column(String(300))
    entity_idcode = Column(String(200))
    user_idcode = Column(String(300))
    del_flag = Column(String(1))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)
    xsthyy = Column(String(1000))


t_tts_temp_xsjl = Table(
    'tts_temp_xsjl', metadata,
    Column('product_id', String(200)),
    Column('product_name', String(200)),
    Column('product_industry', String(200)),
    Column('product_sort', String(200)),
    Column('product_scgl_id', String(200)),
    Column('sale_amount', Numeric(16, 4)),
    Column('buy_com_user_id', String(32)),
    Column('product_amount', Numeric(16, 4)),
    Column('store_count', Numeric(16, 4)),
    Column('freeze_count', Numeric(16, 4)),
    Column('id', String(200)),
    Column('del_flag', String(200)),
    Column('zjcheck', String(200)),
    Column('fromzsm', String(200)),
    Column('unit_id', String(64)),
    Column('join_flag', String(1)),
    Column('harvest_unit', String(64))
)

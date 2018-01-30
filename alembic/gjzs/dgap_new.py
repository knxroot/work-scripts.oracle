# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Index, LargeBinary, Numeric, String, Table, Text, Unicode, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class TDgapFileResource(Base):
    __tablename__ = 't_dgap_file_resource'

    id = Column(String(64), primary_key=True)
    file_path = Column(String(64), nullable=False, server_default=text("NULL"))
    resource_id = Column(ForeignKey(u't_dgap_resource.id'))
    create_by = Column(String(64))
    create_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    update_by = Column(String(64))
    update_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    del_flag = Column(String(10), nullable=False, server_default=text("'N'"))


class TDgapFileResourceLog(Base):
    __tablename__ = 't_dgap_file_resource_log'

    id = Column(String(64), primary_key=True)
    file_resource_id = Column(ForeignKey(u't_dgap_file_resource.id'))
    operation = Column(String(1))
    detail_message = Column(String(256))
    create_by = Column(String(64))
    create_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    update_by = Column(String(64))
    update_time = Column(DateTime, nullable=False, server_default=text("SYSDATE"))
    del_flag = Column(String(10), nullable=False, server_default=text("'N'"))


#class TDgapResource(Base):
#    __tablename__ = 't_dgap_resource'
#
#    id = Column(String(64), primary_key=True)
#    name = Column(String(30))
#    type = Column(String(10))
#    directory_id = Column(ForeignKey(u't_dgap_resource_directory.id'))
#    description = Column(String(300))
#    wsdl_url = Column(String(100))
#    flag = Column(String(1), server_default=text("'Y'"))
#    create_by = Column(String(64))
#    create_time = Column(DateTime, server_default=text("SYSDATE"))
#    update_by = Column(String(64))
#    update_time = Column(DateTime, server_default=text("SYSDATE"))
#    del_flag = Column(String(10), server_default=text("'N'"))

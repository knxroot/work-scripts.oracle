-- ----------------------------------------------------------------------- 
-- t_mdm_basic_code 
-- ----------------------------------------------------------------------- 

CREATE TABLE t_mdm_basic_code
(
    id VARCHAR2(64 char) NOT NULL,
    name VARCHAR2(64 char),
    mark VARCHAR2(256 char),
    abbreviation VARCHAR2(64 char),
    status CHAR(1) DEFAULT '0',
    codes_id VARCHAR2(64 char),
    parent_id VARCHAR2(64 char),
    parent_ids VARCHAR2(64 char),
    create_by VARCHAR2(64 char),
    createDate DATE,
    update_by VARCHAR2(64 char),
    updateDate DATE,
    del_flag CHAR(1) DEFAULT '0',
    remarks VARCHAR2(255 char),
    PRIMARY KEY (id)
);

-- ----------------------------------------------------------------------- 
-- t_mdm_basic_codes 
-- ----------------------------------------------------------------------- 

CREATE TABLE t_mdm_basic_codes
(
    id VARCHAR2(64 char) NOT NULL,
    name VARCHAR2(64 char),
    format VARCHAR2(256 char),
    status CHAR(1) DEFAULT '0',
    normal VARCHAR2(256 char),
    mark VARCHAR2(256 char),
    description VARCHAR2(256 char),
    batch VARCHAR2(256 char),
    principle VARCHAR2(256 char),
    parent_id VARCHAR2(64 char),
    parent_ids VARCHAR2(64 char),
    create_by VARCHAR2(64 char),
    createDate DATE,
    update_by VARCHAR2(64 char),
    updateDate DATE,
    del_flag CHAR(1) DEFAULT '0',
    remarks VARCHAR2(255 char),
    PRIMARY KEY (id)
);


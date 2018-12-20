local hosts=import "hosts.jsonnet";

local basic_oracle_service = {
    port: 1521,
    "service": "orcl",
    dba: "sys",
    dba_password: "Oe123qwe###",
};

local basic_oracle_schema = basic_oracle_service + {
    user: "",
    password: "",
    dsn: self.user + "/" + self.password + "@" +self.ip + ":1521" + "/" +self.service
};

{
    server_249:: hosts.db_249 + basic_oracle_schema + {
        service: "gjzs",
    },

    server_521:: hosts.db_52_1 + basic_oracle_schema + {
    },

    server_528:: hosts.db_52_8 + basic_oracle_schema + {
    },

    dev: self.server_249 + {
        "user": "gjzspt",
        "password": 12345678,
    },

    dev_mirror_bj: self.dev + {
        ip: "218.89.222.119",
    },

    test: self.server_521 + {
        "user": "gjzspt_demo2",
        "password": 12345678,
    },

    logview: self.server_528 + {
        "user": "log_monitor_intgr",
        "password": 12345678,
    },
}
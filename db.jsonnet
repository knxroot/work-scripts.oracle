local hosts=import "hosts.jsn";
local tpl=import "tpl.jsn";

{
    server_249:: hosts.vserver.db_249 + tpl.basic_oracle_schema + {
        service: "gjzs",
    },

    server_521:: hosts.vserver.db_52_1 + tpl.basic_oracle_schema + {
    },

    server_527:: hosts.vserver.db_52_7 + tpl.basic_oracle_schema + {
    },

    /*
    server_529:: hosts.vserver.db_52_9 + tpl.basic_oracle_schema + {
    },
    */

    mysql_server:: {
        ip: "10.0.51.15",
        db_user: "root",
        db_password: "root",
        db_names: ["sg_mall"],
    },

    dev: self.server_249 + {
        "user": "gjzspt",
        "password": 12345678,
    },

    dev_mirror_bj: self.dev + {
        ip: "218.89.222.119",
    },

    test: self.server_527 + {
        "user": "gjzspt_demo2",
        "password": 12345678,
    },

    hbzz: self.server_527 + {
        "user": "hbzz",
        "password": 12345678,
    },

    /*
    test: self.server_528 + {
        "user": "gjzspt_demo2",
        #"password": 12345678,
        "password": "Oe123qwe###2019",
        users: [
            {
                user: "gjzspt_demo2_dev",
                password: "12345678",
            },
        ],
    },

    logview: self.server_528 + {
        "user": "log_monitor_intgr",
        "password": 12345678,
    },
    */
}
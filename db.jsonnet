local basic_oracle_server = {
    "ip": "",
    port: 1521,
    "service": "orcl",
};

local basic_oracle_schema = basic_oracle_server + {
    user: "sys",
    password: "Oe123qwe###",
    dsn: self.user + "/" + self.password + "@" +self.ip + ":1521" + "/" +self.service
};

{
    server_249:: basic_oracle_schema + {
        ip: "192.168.21.249",
        service: "gjzs",
    },

    server_521:: basic_oracle_schema + {
        ip: "10.0.52.1",
    },


    cd_dev: self.server_249 + {
        "user": "gjzspt",
        "password": 12345678,
    },

    cd_test: self.server_521 + {
        "user": "gjzspt_demo3",
        "password": 12345678,
    },
}
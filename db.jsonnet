local basic_oracle = {
    "user": "",
    "password": 12345678,
    "ip": "",
    "service": "orcl",
    "dsn": self.user + "/" + self.password + "@" +self.ip + ":1521" + "/" +self.service
};

{
    cd_dev: basic_oracle + {
        "user": "gjzspt",
        "password": 12345678,
        "ip": "192.168.21.249",
        "service": "gjzs",
    },

}
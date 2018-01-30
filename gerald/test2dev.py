#!/usr/bin/env python
import gerald
testdb = gerald.OracleSchema('gjzspt', 'oracle+cx_oracle://gjzspt:12345678@10.0.52.1:1521/orcl')
devdb = gerald.OracleSchema('gjzspt', 'oracle+cx_oracle://gjzspt:12345678@192.168.21.249:1521/gjzs')
print testdb.compare(devdb)

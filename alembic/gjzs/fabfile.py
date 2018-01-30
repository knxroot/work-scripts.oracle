from fabric.api import *

@task
def sqlacodegen():
    local("sqlacodegen --noviews --outfile ./gjzs.py oracle+cx_oracle://gjzspt:12345678@192.168.21.249:1521/gjzs")

@task
def autogen():
    local('alembic revision --autogenerate -m "auto generated"')

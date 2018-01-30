#from fabric.api import local,cd,run
from fabric.api import *

env.hosts = ['192.168.21.245']
env.user = 'root'
env.password = 'sofn@123'

def run():
    local("""ansible-playbook -i env/ --tags="setup" ./oracle-dg.yaml""")


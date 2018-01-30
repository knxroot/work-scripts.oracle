FROM centos:7

WORKDIR /ansible-role
RUN yum -y install epel-release
RUN yum -y install python-devel python-pip
RUN yum -y groupinstall 'Development Tools'
RUN pip install ansible
ADD . .
RUN printf '[defaults]\nroles_path=../' >ansible.cfg

ENTRYPOINT ansible-playbook ./tests/test.yml

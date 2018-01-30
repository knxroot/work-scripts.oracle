FROM debian:jessie

WORKDIR /ansible-role
RUN apt-get update
RUN apt-get -y install python-pip python-setuptools python-dev build-essential
RUN pip install ansible
ADD . .
RUN printf '[defaults]\nroles_path=../' >ansible.cfg

ENTRYPOINT ansible-playbook ./tests/test.yml

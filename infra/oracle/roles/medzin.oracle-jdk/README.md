Ansible Role: oracle-jdk
=========

[![Build Status](https://travis-ci.org/medzin/ansible-oracle-jdk.svg?branch=master)](https://travis-ci.org/medzin/ansible-oracle-jdk)

Installs Oracle JDK for RedHat/CentOS and Debian/Ubuntu machines.

Requirements
------------

None.

Role Variables
--------------

To use role you don't need to specify any variables. If you want, you can customize java version by setting oracle_jdk_version and oracle_jdk_update variables. You can also specify desired java build number by setting oracle_jdk_build_number variable. By default role will install java 8.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      vars:
        oracle_jdk_version: 8
        oracle_jdk_update: 74
        oracle_jdk_build_number: b02
      roles:
        - role: medzin.oracle-jdk

License
-------

MIT License

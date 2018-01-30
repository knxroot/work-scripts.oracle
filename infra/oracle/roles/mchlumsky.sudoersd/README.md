sudoersd
=========

This role installs the sudo RPM, ensures that /etc/sudoers.d is included and creates or removes sudoers files in /etc/sudoers.d.

This is a fork of knopki's sudoers playbook (https://galaxy.ansible.com/list#/roles/325).

Requirements
------------

None.

Role Variables
--------------

 * sudoers_filename - file name in /etc/sudoers.d (required)
 * sudoers - A list of user who have some sort of sudo access (see example below).
   * default: []
 * sudoers_remove - if enabled, removes /etc/sudoers.d/{{ sudoers\_filename }} instead of creating it.
   * default: false

Dependencies
------------

None.

Example Playbook
----------------

```yaml
---
# The following playbook will generate these lines in /etc/sudoers.d/testing:
#
# testone  somehost=(vagrant, otheruser) NOPASSWD: /usr/bin/foo, /usr/bin/bar, (root) PASSWD: /usr/bin/baz
# testtwo  somehost=(ALL) PASSWD: /usr/bin/foo
# testthree  somehost=(ALL) PASSWD: /usr/bin/baz
# testfour  ALL=(ALL) PASSWD: ALL

- hosts: all
  sudo: yes
  vars:
    test_sudoers:
      - user: "testone"
        host: "somehost"
        user_commands:
          - runas_users:
              - "vagrant"
              - "otheruser"
            commands:
              - "/usr/bin/foo"
              - "/usr/bin/bar"
            nopasswd: true
          - runas_users:
              - "root"
            commands:
              - "/usr/bin/baz"
            nopasswd: false
      - user: "testtwo"
        host: "somehost"
        user_commands:
          - commands:
              - "/usr/bin/foo"
            nopasswd: false
      - user: "testthree"
        host: "somehost"
        user_commands:
          - nopasswd: false
            commands:
              - "/usr/bin/baz"
      - user: "testfour"
  roles:
    - { role: sudoersd, sudoers_filename: testing, sudoers: "{{ test_sudoers }}" }
# Uncomment following line to remove /etc/sudoers.d/testing
#    - { role: sudoersd, sudoers_filename: testing, sudoers_remove: true }

```


License
-------

BSD

Author Information
------------------

https://github.com/mchlumsky

https://github.com/knopki

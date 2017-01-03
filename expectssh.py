#!/usr/bin/env python2.7
#coding:utf-8
import pexpect
PROMPT=['#','>>>','>','\$']
def send_command(child,cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before
def connect(user,host,password):
    ssh_newkey='Are you sure you want to continue connecting'
    connStr='ssh '+user+'@'+host
    child=pexpect.spawn(connStr)
    ret=

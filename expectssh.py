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
    ret=child.expect([pexpect.TIMEOUT,ssh_newkey,'[P|p]assword'])
    if ret==0:
        print '[-] Error Connecting'
        return
    if ret==1:
        child.sendline('yes')
        ret=child.expect([pexpect.TIMEOUT,'[P|p]assword'])
        if ret == 0:
            print '[-] Error Connecting'
            return
        elif ret ==1:
            child.sendline(password)
            child.expect(PROMPT)
            return child
    if ret==2:
        child.sendline(password)
        child.expect(PROMPT)
        return child
def main():
    host='127.0.0.1'
    password='930918'
    user='root'
    child=connect(user,host,password)
    send_command(child,'ifconfig')
if __name__=='__main__':
    main()

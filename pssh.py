#!/usr/bin/env python2.7
#coding:utf-8
import pxssh
def send_cmd(child,cmd):
    child.sendline(cmd)
    child.prompt()
    print child.before
def connect(host,user,password):
    try:
        s=pxssh.pxssh()
        s.login(host,user,password)
        return s
    except Exception,e:
        print '[-] Error Connecting'
        exit(0)
    s=connect('127.0.0.1','root','930918')
    send_cmd(s,'ifconfig')

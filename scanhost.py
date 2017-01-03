#!/usr/bin/env python2.7
#coding:utf-8
import argparse
import socket
import threading
screenLock=threading.Semaphore(value=1)
def connscan(tgthost,tgtport):
    try:
        connstk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connstk.connect((tgthost,int(tgtport)))
        connstk.send('ViolentPython\r\n')
        results=connstk.recv(100)
        screenLock.acquire()
        print "scan port "+tgtport
        print "[+]%d/tcp open" %int(tgtport)
        print "[+]"+str(results)+'\r\n'
    except Exception,e:
        screenLock.acquire()
        print "scan port "+tgtport
        print "[-]%d/tcp closed\r\n" %int(tgtport)
    finally:
        screenLock.release()
        connstk.close()

def portscan(tgthost,portlist):
    print tgthost
    for port in portlist:
        t=threading.Thread(target=connscan,args=(tgthost,port))
        t.start() 
    
parser = argparse.ArgumentParser(prog='hostscan.py',usage='hostscan.py -H host -p 22^3306')
parser.add_argument('-H',dest='tgthost',type=str,help="hostname")
parser.add_argument('-p',dest='tgtport',type=str,help="port,split with '^'")
args=parser.parse_args()
tgthost=args.tgthost
tgtport=args.tgtport
if all([tgthost,tgtport]):
    port_list=tgtport.split('^')
    portscan(tgthost,port_list)
else:
    print parser.usage
    exit(1)

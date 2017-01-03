#!/usr/bin/env python2.7
#coding:utf-8
import argparse
import nmap
def nmapScan(tgtHost,tgtPort):
    nmScan=nmap.PortScanner()
    results=nmScan.scan(tgtHost,tgtPort)
    state=results['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
    print " [*] " + tgtHost + " tcp/" + tgtPort + " " + state
def main():
    parser = argparse.ArgumentParser(prog='hostscan.py',usage='hostscan.py -H host -p 22^3306....')
    parser.add_argument('-H',dest='tgthost',type=str,help="hostname")
    parser.add_argument('-p',dest='tgtport',type=str,help="port,split with '^'")
    args=parser.parse_args()
    tgthost=args.tgthost
    tgtport=args.tgtport
    if all([tgthost,tgtport]):
        port_list=tgtport.split('^')
        for port in port_list:
            nmapScan(tgthost,port)
    else:
        print parser.usage
        exit(1)
if __name__=='__main__':
    main()


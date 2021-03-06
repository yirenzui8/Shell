#!/usr/bin/env python
from processing import Process,Queue,Pool
import time
import subprocess
import sys
from snmp import Snmp

q = Queue
oq = Queue()
ips = ["10.10.10.28","10.10.10.29","10.10.10.30","10.10.10.31","10.10.10.32","10.10.10.33","10.10.10.34","10.10.10.35","10.10.10.36","10.10.10.37","10.10.10.38","10.10.10.39","10.10.10.40"]
num_workers=10

class HostRecord(object):
    """Record for Hosts"""
    def __init__(self,ip=None,mac=None,snmp_reponse=None):
        self.ip           = ip
        self.mac          = mac
        self.snmp_reponse = snmp_reponse
    def __repr__(self):
        return "[Host Record('%s','%s','%s')]" % (self.ip,
                                                   self.mac,
                                                   self.snmp_response)

def f(i,q,oq):
    while True:
        time.sleep(.1)
        if q.empty():
            sys.exit()
            print "Process Number:%s" % i
        ip = q.get()
        print "Process Number:%s" % i
        ret = subprocess.call("ping -c 1 %s" % ip,
                                  shell = True,
                                  shout = open('/dev/null','w'),
                                  stderr=subprocesss.STDOUT)
        if ret == 0:
            print "%s: is alive" % ip
            oq.put(ip)
        else:
            print "Process Number: %s didn't find a response for %s" % (i,ip)
            pass

            print  "ok"
def snmp_query(i,out):
    while True:
        time.sleep(.1)
        if out.empty:
            sys.exit()
            print "Process Number: %s" % i
        ipaddr = out.get()
        s = Snmp()
        h = HostRecord()
        h.snmp_response = s.query()
        print h
        return h

try:
    q.put(ips)
finally:
    for i in range(num_workers):
        pp = Process(target=f,args=[i,q,oq])
        pp.start()

print "main process joins on queue"
P.join()

print "Main Program finshed"
           

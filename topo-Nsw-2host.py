#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController

__author__ =  "Alan Veloso"

class LinearSwitchTopo(Topo):
    "N switch connected to 2 hosts in the edge. Where N is difided as switchs_count"
    def __init__(self, switchs_count = 1):

	Topo.__init__(self)
	
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
	
	for s in range(switchs_count):
		switch = self.addSwitch('s%s' % (s + 1))
		if s == 0:
			self.addLink(host1, switch)
		if s > 0:
			self.addLink(switch_prev, switch)
		switch_prev = switch
	self.addLink(host2, switch)

def simpleTest():
    "Create and test a simple network"
    topo = LinearSwitchTopo(switchs_count = 5)
    net = Mininet( topo=topo, controller=lambda name: RemoteController( name, ip='10.126.1.25', port=6653) )
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    net.stop()

topos = { 'lineartopo': ( lambda: LinearSwitchTopo(switchs_count = 5) ) }

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()

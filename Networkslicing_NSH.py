#!/usr/bin/python
"""
This Network Emulation architecture is designed by Sidra Hussain and implemented by Maria Majid.
This Network Emulation is implemented on Containernet. Its Open VirualSwitch based network topology,
which consists of only one IP network '172.10.0.0/24".
This Network emulation architecture consists of three network slices.
The detailed explaination of all three slices is presented in Project Documentation.
"""
from mininet.net import Containernet
from mininet.node import Controller, Node, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
import os
import time

setLogLevel('info')

net = Containernet()
info('*** Adding controller\n')

info('*** Creating Access network 1\n')
h11 = net.addHost('h11', ip='172.10.0.21/24',  mac='00:00:00:00:00:01', dpid='1000000000000001')
h12 = net.addHost('h12', ip='172.10.0.22/24',  mac='00:00:00:00:00:02', dpid='1000000000000002')

info('*** Creating Access network 2\n')
h21 = net.addHost('h21', ip='172.10.0.31/24',  mac='00:00:00:00:04:01', dpid='1000000000000006')
h22 = net.addHost('h22', ip='172.10.0.32/24',  mac='00:00:00:00:04:02', dpid='1000000000000007')

info('*** Creating Access network 3\n')
h31 = net.addHost('h31', ip='172.10.0.51/24',  mac='00:00:00:00:06:01', dpid='1000000000000012')
h32 = net.addHost('h32', ip='172.10.0.52/24',  mac='00:00:00:00:06:02', dpid='1000000000000013')
h33 = net.addHost('h33', ip='172.10.0.53/24',  mac='00:00:00:00:06:03', dpid='1000000000000014')


info('*** Adding switches in Access and Edge Network\n')
s1 = net.addSwitch('s1', cls=OVSSwitch, dpid='1000000000000001')		#Switch in AccessNetwork 1
s2 = net.addSwitch('s2', cls=OVSSwitch, dpid='1000000000000006')		#Switch in AccessNetwork 2
s3 = net.addSwitch('s3', cls=OVSSwitch, dpid='1000000000000012')		#Switch in AccessNetwork 3

s11 = net.addSwitch('s11', cls=OVSSwitch, dpid='1000000000000005')		#Switch in EdgeNetwork 1
s22 = net.addSwitch('s22', cls=OVSSwitch, dpid='1000000000000011')		#Switch in EdgeNetwork 2
s33 = net.addSwitch('s33', cls=OVSSwitch, dpid='1000000000000016')		#Switch in EdgeNetwork 3

sd1 = net.addSwitch('sd1', cls=OVSSwitch, dpid='1000000000000017')		#Switch in DataCenter1
sd2 = net.addSwitch('sd2', cls=OVSSwitch, dpid='1000000000000018')	 	#Switch in DataCenter2
sd3 = net.addSwitch('sd3', cls=OVSSwitch, dpid='1000000000000019')	 	#Switch in DataCenter3

#Chatroom Service on data centers d1, d2 and d3 is implemented by Sidra Hussain
info('*** Adding data centers\n')
d1 = net.addDocker('d1', dimage="ubuntu:trusty", ip='172.10.0.1/24', mac='00:00:00:00:00:30', dpid='1000000000000017')	#slice1 datacenter
d2 = net.addDocker('d2', dimage="ubuntu:trusty", ip='172.10.0.2/24', mac='00:00:00:00:00:40', dpid='1000000000000018')	#slice2 datacenter
d3 = net.addDocker('d3', dimage="ubuntu:trusty", ip='172.10.0.3/24', mac='00:00:00:00:00:50', dpid='1000000000000019')	#slice3 datacenter

#Possible Extension "DHCP service" on Edge Servers e1, e2 & e3 is implemented by Maria Majid 
info('*** Adding edge networks\n')
e1 = net.addDocker('e1', dimage="ubuntu:trusty", ip='172.10.0.20/24', mac='00:00:00:00:00:35', dpid='1000000000000005')	#DHCP server for Access nw 1
e2 = net.addDocker('e2', dimage="ubuntu:trusty", ip='172.10.0.30/24', mac='00:00:00:00:00:46', dpid='1000000000000011')	#DHCP server for Access nw 2
e3 = net.addDocker('e3', dimage="ubuntu:trusty", ip='172.10.0.50/24', mac='00:00:00:00:00:55', dpid='1000000000000016')	#DHCP server for Access nw 3

info('*** Adding Edge OvS switches\n')
sr1 = net.addSwitch('sr1', cls=OVSSwitch, dpid='1000000000000020')		#EdgeSwitch1 linking Access n/w & Edge n/w 1
sr2 = net.addSwitch('sr2', cls=OVSSwitch, dpid='1000000000000021')		#EdgeSwitch2 linking Access n/w & Edge n/w 2
sr3 = net.addSwitch('sr3', cls=OVSSwitch, dpid='1000000000000022')		#EdgeSwitch3 linking Access n/w & Edge n/w 3

info('*** Adding Transport OvS switches\n')
st1 = net.addSwitch('st1', cls=OVSSwitch, dpid='1000000000000023')
st2 = net.addSwitch('st2', cls=OVSSwitch, dpid='1000000000000024')
st3 = net.addSwitch('st3', cls=OVSSwitch, dpid='1000000000000025')
st4 = net.addSwitch('st4', cls=OVSSwitch, dpid='1000000000000026')
st5 = net.addSwitch('st5', cls=OVSSwitch, dpid='1000000000000027')
st6 = net.addSwitch('st6', cls=OVSSwitch, dpid='1000000000000028')
st7 = net.addSwitch('st7', cls=OVSSwitch, dpid='1000000000000029')
st8 = net.addSwitch('st8', cls=OVSSwitch, dpid='1000000000000030')
st9 = net.addSwitch('st9', cls=OVSSwitch, dpid='1000000000000031')
st10 = net.addSwitch('st10', cls=OVSSwitch, dpid='1000000000000032')
st11 = net.addSwitch('st11', cls=OVSSwitch, dpid='1000000000000033')
st12 = net.addSwitch('st12', cls=OVSSwitch, dpid='1000000000000034')

info('*** Creating links for AccessNetworks\n')

#linking tenants h11 and h12 of Access network 1 with access n/w switch s1
net.addLink(h11, s1)
net.addLink(h12, s1)

#linking tenants h21 and h22 of Access network 2 with access n/w switch s2
net.addLink(h21, s2)
net.addLink(h22, s2)

#linking tenants h31, h32 and h33 of Access network 1 with access n/w switch s3
net.addLink(h31, s3)
net.addLink(h32, s3)
net.addLink(h33, s3)

#linking edge servers with switches
info('*** Creating links for Edge Networks\n')
net.addLink(e1, s11)
net.addLink(e2, s22)
net.addLink(e3, s33)

#linking data centers in transport network with their respective switches
info('*** Creating links for DataCenters\n')
net.addLink(d1, sd1)
net.addLink(d2, sd2)
net.addLink(d3, sd3)

#linking Edge switches
info('*** Creating links with Edge OVSs\n')
net.addLink(s1, sr1)
net.addLink(s11, sr1)
net.addLink(s2, sr2)
net.addLink(s22, sr2)
net.addLink(s3, sr3)
net.addLink(s33, sr3)

#linking transport switches as per the defined path of network slices
info('*** Creating links with Transport OVSs')

net.addLink(sr1, st1)
net.addLink(st1, st2)
net.addLink(st2, st3)
net.addLink(st3, sd1)

net.addLink(sr2, st4)
net.addLink(st4, st5)
net.addLink(st5, st6)
net.addLink(st6, sd1)

net.addLink(sr3, st7)
net.addLink(st7, st8)
net.addLink(st8, sd1)

net.addLink(st1, st9)
net.addLink(st9, sd2)
net.addLink(st7, st10)
net.addLink(st10, sd2)

net.addLink(st4, st12)
net.addLink(st12, sd3)
net.addLink(st7, st11)
net.addLink(st11, sd3)

info('*** Starting network\n')
net.start()

info('*** Running CLI\n')
CLI(net)

info('*** Stopping network')
net.stop()


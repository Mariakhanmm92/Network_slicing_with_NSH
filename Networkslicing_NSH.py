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
#A python script for Chatroom service is deployed on ubuntu:trusty image and configured on the basis of datacenters available in the network emulation
#In the network topology there are 3 datacenters, so 3 containers for chatroom service are created and deployed on each data center.

info('*** Adding data centers\n')
d1 = net.addDocker('d1', dimage="mariamajid/chatserver:latest", ip='172.10.0.1/24', mac='00:00:00:00:00:30', dpid='1000000000000017')	#slice1 datacenter
d2 = net.addDocker('d2', dimage="mariamajid/chatserver2:latest", ip='172.10.0.2/24', mac='00:00:00:00:00:40', dpid='1000000000000018')	#slice2 datacenter
d3 = net.addDocker('d3', dimage="mariamajid/chatserver3:latest", ip='172.10.0.3/24', mac='00:00:00:00:00:50', dpid='1000000000000019')	#slice3 datacenter

#Possible Extension "DHCP service" on Edge Servers e1, e2 & e3 is implemented by Maria Majid 
#A package "dnsmasq" is installed on ubuntu:trusty image. The file "dnsmasq.conf" is configured with dhcp listen interface, IP & dhcp range.
#Similarly, three containers are created for edge server e1, e2, e3, to allocate dynamic IP to their respective slice tenants.

info('*** Adding edge networks\n')
e1 = net.addDocker('e1', dimage="mariamajid/dhcp1", ip='172.10.0.20/24', mac='00:00:00:00:00:35', dpid='1000000000000005')	#DHCP server for Access nw 1
e2 = net.addDocker('e2', dimage="mariamajid/dhcp2", ip='172.10.0.30/24', mac='00:00:00:00:00:46', dpid='1000000000000011')	#DHCP server for Access nw 2
e3 = net.addDocker('e3', dimage="mariamajid/dhcp3", ip='172.10.0.50/24', mac='00:00:00:00:00:55', dpid='1000000000000016')	#DHCP server for Access nw 3

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
info('*** Creating links with Transport OVSs\n')

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

#Adding Configuration of Flow rules on Open Virtual switches for network slices creation
#Configurations of slice 1 and 3 are implemented by Maria Majid
#Configurations of slice 2 are implemented by Sidra Hussain

info('*** Adding Flow rules on Access & Edge Network 1 OVSs\n')

s1.cmd('ovs-ofctl -Oopenflow13 add-flows s1 s1flow.txt')	#configured by maria/sidra
s11.cmd('ovs-ofctl -Oopenflow13 add-flows s11 s11flow.txt')	#configured by maria/sidra
sr1.cmd('ovs-ofctl -Oopenflow13 add-flows sr1 sr1flow.txt')	#configured by maria/sidra

info('*** Adding Flow rules on Access & Edge Network 2 OVSs\n')

s2.cmd('ovs-ofctl -Oopenflow13 add-flows s2 s2flow.txt')	#configured by maria
s22.cmd('ovs-ofctl -Oopenflow13 add-flows s22 s22flow.txt')	#configured by maria
sr2.cmd('ovs-ofctl -Oopenflow13 add-flows sr2 sr2flow.txt')	#configured by maria

info('*** Adding Flow rules on Access & Edge Network 3 OVSs\n')

s3.cmd('ovs-ofctl -Oopenflow13 add-flows s3 s3flow.txt')	#configured by maria/sidra
s33.cmd('ovs-ofctl -Oopenflow13 add-flows s33 s33flow.txt')	#configured by maria/sidra
sr3.cmd('ovs-ofctl -Oopenflow13 add-flows sr3 sr3flow.txt')	#configured by maria/sidra

info('*** Adding Flow rules on Datacenter 1 OVS\n')
sd1.cmd('ovs-ofctl -Oopenflow13 add-flows sd1 sd1flow.txt')	#configured by maria

info('*** Adding Flow rules on Datacenter 2 OVS\n')
sd2.cmd('ovs-ofctl -Oopenflow13 add-flows sd2 sd2flow.txt')	#configured by sidra

info('*** Adding Flow rules on Datacenter 3 OVS\n')
sd3.cmd('ovs-ofctl -Oopenflow13 add-flows sd3 sd3flow.txt')	#configured by maria

info('*** Adding Flow rules on Transport Network OVSs\n')

st1.cmd('ovs-ofctl -Oopenflow13 add-flows st1 st1flow.txt')	#configured by maria/sidra
st2.cmd('ovs-ofctl -Oopenflow13 add-flows st2 st2flow.txt')	#configured by maria
st3.cmd('ovs-ofctl -Oopenflow13 add-flows st3 st3flow.txt')	#configured by maria
st4.cmd('ovs-ofctl -Oopenflow13 add-flows st4 st4flow.txt')	#configured by maria
st5.cmd('ovs-ofctl -Oopenflow13 add-flows st5 st5flow.txt')	#configured by maria
st6.cmd('ovs-ofctl -Oopenflow13 add-flows st6 st6flow.txt')	#configured by maria
st7.cmd('ovs-ofctl -Oopenflow13 add-flows st7 st7flow.txt')	#configured by maria/sidra
st8.cmd('ovs-ofctl -Oopenflow13 add-flows st8 st8flow.txt')	#configured by maria
st9.cmd('ovs-ofctl -Oopenflow13 add-flows st9 st9flow.txt')	#configured by sidra
st10.cmd('ovs-ofctl -Oopenflow13 add-flows st10 st10flow.txt')	#configured by sidra
st11.cmd('ovs-ofctl -Oopenflow13 add-flows st11 st11flow.txt')	#configured by maria
st12.cmd('ovs-ofctl -Oopenflow13 add-flows st12 st12flow.txt')	#configured by maria

#Adding Delay
time.sleep(1)

#Following DHCP configurations are added by  maria

info('***Restarting DHCP service on e1\n')
#Restarting DHCP service on Edge Server e1
e1.cmd('service dnsmasq restart')

#Tenants of Access Network 1 getting dynamic IPs from DHCP server e1
info('*** tenant 1 h11 getting dynamic IP\n')
h11.cmd('ifconfig h11-eth0 0')
h11.cmd('dhclient h11-eth0')

info('*** tenant 2 h12 getting dynamic IP\n')
#In Process
h12.cmd('ifconfig h12-eth0 0')
h12.cmd('dhclient h12-eth0')

#Adding Delay
time.sleep(1)

info('***Restarting DHCP service on e2\n')
#Restarting DHCP service on Edge Server e2
e2.cmd('service dnsmasq restart')

#Tenants of Access Network 2 getting dynamic IPs from DHCP server e2
info('*** tenant 1 h21 getting dynamic IP\n')
h21.cmd('ifconfig h21-eth0 0')
h21.cmd('dhclient h21-eth0')

info('*** tenant 2 h22 getting dynamic IP\n')
#In Process
h22.cmd('ifconfig h22-eth0 0')
h22.cmd('dhclient h22-eth0')

#Adding Delay
time.sleep(1)

info('***Restarting DHCP service on e3\n')
#Restarting DHCP service on Edge Server e3
e3.cmd('service dnsmasq restart')

#Tenants of Access Network 3 getting dynamic IPs from DHCP server e3
info('*** tenant 1 h31 getting dynamic IP\n')
#In Process
h31.cmd('ifconfig h31-eth0 0')
h31.cmd('dhclient h31-eth0')

info('*** tenant 2 h32 getting dynamic IP\n')
#In Process
h32.cmd('ifconfig h32-eth0 0')
h32.cmd('dhclient h32-eth0')

info('*** tenant 3 h33 getting dynamic IP\n')
#In Process
h33.cmd('ifconfig h33-eth0 0')
h33.cmd('dhclient h33-eth0')

time.sleep(1)
info('*** Welcome to Mobile Computing Project\n')


info('*** Running CLI\n')
CLI(net)

info('*** Stopping network')
net.stop()


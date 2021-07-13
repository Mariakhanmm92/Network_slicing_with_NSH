# Realization of 5G concept "Network Slicing" using Nework Service Header (NSH)

Network slicing plays an important role for enabling the 5G technology. It primarily provides means
to use network as a service for the use cases. This technology permits network operators to build 
multiple virtual networks on a physical single network infrastructure. This helps service providers to 
deploy new services flexibly and accommodate diversified services easily which in turn partitions 
different services for the provision of optimum support. In this project, network slicing is achieved 
using Network service header encapsulation to implement Chat room service across multiple hosts. 
For Software Defined Network approach, OpenFlow protocol is utilized in the extensively designed 
emulated network environment.

# Emulated Network Description
As depicted in fig. "Emulated Network Topology", the emulated network consists of three access networks, each with an edge network, and three datacenters or 
servers. This whole network emulation is pure OVS based network, so only one IP network is assigned to it which is “172.10.0.0/24”. 

The chat room service is deployed on datacenters d1, d2 and d3. The DHCP service is deployed on edge servers 
e1, e2 and e3. These services are implemented via containernet virtualization. The integrated switches are all 
OVS to implement OpenFlow protocol for SDN.

# Guidelines for Project Deployment

1. To run the configured network emulation for this project, Mininet, Containernet and ovs-vswitchd (Open vSwitch) version 2.9.8 must be pre-installed in the VM.
2. Wireshark must be installed in the system to analyze the traffic.
3. The docker images required to run in the emulation are already pushed on Dockerhub public repository. Therefore, whenever the network emulation runs, the images will automatically be pulled in the system.
4. The main program file for configured network emulation "NetworkSlicing_NSH.py", flow rules configuration files (.txt) for each Open virtual switch and client.py must be moved to a folder within the containernet directory in the testing system/VM.
5. Open the terminal of the VM and navigate to craeted folder in containernet, where all the files are saved.
6. Run the “NetworkSlicing_NSH.py” file with the command “sudo python3 nsh_project.py”. 
7. This will start the configured network emulation of this project. The images that required to be run on edge network’s dockers (e1, e2, e3) and Data centers (d1, d2, d3) will be pulled automatically in the running emulation infrastructure.
8. Before utilization of DHCP service by hosts, the service “dnsmasq” will be restarted in their respective docker containers (e1, e2, e3).
9. For DHCP services utilization by the hosts of respective access networks, the command “dhclient host.ethx” is already configured in the emulation. Therefore, it is most likely possible that all the hosts already got their dynamic Ips.
10. To analyze the DHCP traffic within the slices, comment out the configured “dhclient” commands. Run the wireshark on the respective interfaces to check the packet´s encapsulation within their defined network slices.
11. Take the terminal of the desired host (DHCP client) eg. h11. Run the command “ifconfig h11-eth0 0” on the h11 terminal. Take the terminal of e1 (DHCP server), restart the service “dnsmasq”. After this, run the command “dhclient h11-eth0”. 
12. Take the terminals of the tenant or hosts which are part of the same network slice as datacenter. For example, h11, h21, h31 are the hosts from access networks 1,2 and 3 and chatroom service to all these hosts are provided by d1. 
13. After taking the xterm of desired tenant, enter to the folder/directory where the client.py file is saved. 
14. Run the “client.py” file at the host h11 using “sudo python3 client.py”. Similar, take xterms of h21 and h31 and run the “client.py” on them too. 
15. After running the file, it will ask to “enter host name” and “enter port”. Give the IP address of d1 (172.10.0.1) in the host name and enter the same port which was provided previously to the d1 (80 in the above scenario). Then, “enter username” of own choice.
16. A message will appear on the data center d1 “new connection. Username:xyz”. Now, the data center d1 serves as the chatroom and the tenants of slice 1 h11, h21 and h31 will be able to communicate with each other in this chatroom.
17. Other slices will work on the similar pattern.

Note; To get the complete insight of this project, kindly refer to the project documentation in the Documentation folder.

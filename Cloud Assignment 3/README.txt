Task 1:
1. What is the output of "nodes" and "net"
	output of net:
		h1 h1-eth0:s3-eth2
		h2 h2-eth0:s3-eth3
		h3 h3-eth0:s4-eth2
		h4 h4-eth0:s4-eth3
		h5 h5-eth0:s6-eth2
		h6 h6-eth0:s6-eth3
		h7 h7-eth0:s7-eth2
		h8 h8-eth0:s7-eth3
		s1 lo:  s1-eth1:s2-eth1 s1-eth2:s5-eth1
		s2 lo:  s2-eth1:s1-eth1 s2-eth2:s3-eth1 s2-eth3:s4-eth1
		s3 lo:  s3-eth1:s2-eth2 s3-eth2:h1-eth0 s3-eth3:h2-eth0
		s4 lo:  s4-eth1:s2-eth3 s4-eth2:h3-eth0 s4-eth3:h4-eth0
		s5 lo:  s5-eth1:s1-eth2 s5-eth2:s6-eth1 s5-eth3:s7-eth1
		s6 lo:  s6-eth1:s5-eth2 s6-eth2:h5-eth0 s6-eth3:h6-eth0
		s7 lo:  s7-eth1:s5-eth3 s7-eth2:h7-eth0 s7-eth3:h8-eth0
		c0
	output of nodes:
		available nodes are: 
		0 h1 h2 h3 h4 h5 h6 h7 h8 s1 s2 s3 s4 s5 s6 s7



2. What is the output of "h7 ifconfig"
h7-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.7  netmask 255.0.0.0  broadcast 10.255.255.255
        inet6 fe80::7c17:2fff:fe89:1c2e  prefixlen 64  scopeid 0x20<link>
        ether 7e:17:2f:89:1c:2e  txqueuelen 1000  (Ethernet)
        RX packets 72  bytes 5480 (5.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 12  bytes 936 (936.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


Task 2:
1. Draw the function call graph of this controller
        _handle_PacketIn ---> act_like_hub ---> resend_packet
2. Have h1 ping h2 and h1 ping h8 for 100 times
	a and b. h1 ping h2 average: 20.175, min: 1.388, max: 50.262
                 h1 ping h8 average: 71.462  min: 12.106, max: 139.594
        c. The time takes from h1 to h2 is less than the time takes from h1 to h8.because there is only one switches 
           between h1 and h2, and there are five switches between h1 and h8
        
3. Run "iperf h1 h2" and "iperf h1 h8"
        a. Iperf is for testing TCP bandwidth between two nodes
        b. h1 and h2: Results: ['10.5 Mbits/sec', '12.4 Mbits/sec']
           h1 and h8: Results: ['2.04 Mbits/sec', '2.64 Mbits/sec']
        c. The bandwidth between h1 and h2 is greater than the bandwidth between h1 and h8, 
           beacuse the distance between h1 and h2 is shoeter therefore the bandwidth is greater.
4. switch 5,7,2,4,6,1,3 observe the traffic and I put print(self.connection) in the of_tutorial file.

Task 3:
1. if a source comes to the switch, the method will check if the source is in the table. if not in the table then it will
   insert the value in the table. Then the method will check if the destination is in the table. 
   if in the table, then it will send to the destination otherwise it will send to all. 
2. Have h1 ping h2 and h1 ping h8 for 100 times
	a and b. h1 ping h2 average: 43.112, min: 1.840, max: 131.330
                 h1 ping h8 average: 130.605, min: 8.684, max: 213.308 
        c. The average time increases.       
3. Run "iperf h1 h2" and "iperf h1 h8"
        a. h1 and h2: Results: ['7.08 Mbits/sec', '8.95 Mbits/sec']
           h1 and h8: Results: ['1.20 Mbits/sec', '1.65 Mbits/sec']
        b. The bandwidth decreases. 




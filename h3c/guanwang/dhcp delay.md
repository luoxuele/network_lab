# 1. 基本ip配置

	[S1]vlan 2
	[S1-vlan2]port g1/0/1
	[S1]int Vlan-interface 2
	[S1-Vlan-interface2]ip add 10.1.2.1 24
	[S1]vlan 3
	[S1-vlan3]port g1/0/2
	[S1-vlan3]quit
	[S1]int vlan-in 3
	[S1-Vlan-interface3]ip add 10.1.1.1 24



# 2. dhcp配置

	// 使能dhcp，并配置vlan3接口工作在dhcp服务器模式
	[S1]dhcp enable
	[S1]int Vlan-interface 3
	[S1-Vlan-interface3]dhcp select server
	
	// 配置地址池
	[S1]dhcp server ip-pool 1
	[S1-dhcp-pool-1]network 10.1.1.0 mask 255.255.255.0
	[S1-dhcp-pool-1]address range 10.1.1.2 10.1.1.100
	
	[S1-dhcp-pool-1]dns-list 10.1.1.3
	[S1-dhcp-pool-1]tftp-server ip-address 10.1.1.4
	[S1-dhcp-pool-1]domain-name com
	[S1-dhcp-pool-1]gateway-list 10.1.1.1
	[S1-dhcp-pool-1]forbidden-ip 10.1.1.3 10.1.1.4
	
	// vlan-intface 3 中引用地址池1
	[S1]int Vlan-interface 3
	[S1-Vlan-interface3]dhcp server apply ip-pool 1
	
	//option 82 功能
	[S1]dhcp class aa
	[S1-dhcp-class-aa]if-match rule 1 option 82 hex 0001 offset 4 length 2
	
	[S1]dhcp class bb
	[S1-dhcp-class-bb]if-match rule 1 option 82 hex 0003 offset 4 length 2
	
	//配置dhcp地址池2
	[S1]dhcp server ip-pool 2
	[S1-dhcp-pool-2]network 10.1.3.0 mask 255.255.255.0
	[S1-dhcp-pool-2]class aa range 10.1.3.2 10.1.3.48
	[S1-dhcp-pool-2]class bb range 10.1.3.49 10.1.3.100
	[S1-dhcp-pool-2]tftp-server ip-address 10.1.1.4
	[S1-dhcp-pool-2]dns-list 10.1.1.3
	[S1-dhcp-pool-2]domain-name com
	[S1-dhcp-pool-2]gateway-list 10.1.3.1
	
	//引用地址池
	[S1]interface Vlan-interface 2
	[S1-Vlan-interface2]dhcp server apply ip-pool 2
	
	//静态路由
	[S1]ip route-static 10.1.3.0 24 10.1.2.2
	




# reference

https://www.h3c.com/cn/d_201804/1074476_30005_0.htm
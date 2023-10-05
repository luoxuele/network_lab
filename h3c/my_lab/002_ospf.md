# 实验目标



# 配置步骤

## 1. 基本ip配置

[R1]int g0/0
[R1-GigabitEthernet0/0]ip add 10.1.1.2 24
[R1]int lo0
[R1-LoopBack0]ip add 2.2.2.2 32

[S1]in g1/0/1
[S1-GigabitEthernet1/0/1]port link-mode route
[S1-GigabitEthernet1/0/1]ip add 10.1.1.1 24
[S1]int g1/0/2
[S1-GigabitEthernet1/0/2]port link-mode route
[S1-GigabitEthernet1/0/2]ip add 192.168.1.254 24
[S1-GigabitEthernet1/0/2]description to link_1
[S1]int g1/0/3
[S1-GigabitEthernet1/0/3]port link-mode route
[S1-GigabitEthernet1/0/3]ip add 192.168.2.254 24
[S1-GigabitEthernet1/0/3]description to link_2

VPCS_3> ip 192.168.1.1 24 192.168.1.254
VPCS_4> ip 192.168.2.1 24 192.168.2.254

## 2. 配置ospf

[R1]ospf 1 router-id 2.2.2.2
[R1-ospf-1]area 0
[R1-ospf-1-area-0.0.0.0]network 2.2.2.2 0.0.0.0
[R1-ospf-1-area-0.0.0.0]network 10.1.1.0 0.0.0.255

[S1]ospf 1 router-id 1.1.1.1
[S1-ospf-1]area 0
[S1-ospf-1-area-0.0.0.0]network 1.1.1.1 0.0.0.0
[S1-ospf-1-area-0.0.0.0]network 10.1.1.0 0.0.0.255
[S1-ospf-1-area-0.0.0.0]network 192.168.1.0 0.0.0.255
[S1-ospf-1-area-0.0.0.0]network 192.168.2.0 0.0.0.255

## 3. 测试

VPCS_3> ping 2.2.2.2
VPCS_4> ping 2.2.2.2
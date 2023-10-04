# 实验需求

1. 按照图示配置 IP 地址，所有路由器配置环回口 IP 地址为 `X.X.X.X/32` 作为 Router-id，X 为设备编号（R7 除外）
2. 按照图示分区域配置 OSPF
3. R1 和 R6 上分别配置环回口来模拟业务网段，如拓扑图所示；业务网段中不允许出现协议报文
4. 正常情况下，Area 10 和 Area 100 的业务流量经过 R3-R5，当 R3 和 R5 之间的链路故障时，流量自动切换到 R2-R4
5. R2 和 R4 之间的链路只对到 `192.168.2.0` 的流量提供备份
6. Area 100 配置为 Stub 区域
7. 其他区域不允许出现 Area 10 的业务网段的明细路由
8. 适当调整链路 Cost，避免出现等价路由
9. 为了保证协议安全，Area 0 配置区域验证，验证密钥为 `123456`
10. R2 作为网络出口，配置默认路由指向 R7，并引入到 OSPF
11. R2 上配置 EASY IP，只对 `192.168.0.0/24` 和 `192.168.2.0/24` 提供访问互联网功能
12. 排除全部网络故障，并完成排错报告





# 1. 基本ip配置，所有的路由器（R5除外）都配置loopback0接口ip地址为x.x.x.x/32作为router-id ,x为设备编号

[R1-GigabitEthernet0/0]ip add 10.1.1.1 24
[R1-GigabitEthernet0/1]ip add 10.2.2.1 24
[R1-GigabitEthernet0/2]ip add 100.0.0.1 24
[R1-LoopBack0]ip add 1.1.1.1 32

[R2-GigabitEthernet0/0]ip add 10.1.1.2 24
[R2-GigabitEthernet0/1]ip add 10.3.3.2 24
[R2-GigabitEthernet0/2]ip add 10.4.4.2 24
[R2-LoopBack0]ip add 2.2.2.2 32

[R3-GigabitEthernet0/0]ip add 10.2.2.3 24
[R3-GigabitEthernet0/1]ip add 10.3.3.3 24
[R3-GigabitEthernet0/2]ip add 10.5.5.3 24
[R3-LoopBack0]ip add 3.3.3.3 32

[R4-GigabitEthernet0/0]ip add 10.4.4.4 24
[R4-GigabitEthernet0/1]ip add 10.5.5.4 24
[R4-LoopBack0]ip add 4.4.4.4 32
[R4-LoopBack1]ip add 192.168.0.1 24
[R4-LoopBack2]ip add 192.168.1.1 24
[R4-LoopBack3]ip add 192.168.2.1 24
[R4-LoopBack4]ip add 192.168.3.1 24

[R5-GigabitEthernet0/0]ip add 100.0.0.5 24

# 2. 按拓扑图配置ospf
[R1]ospf 1 router-id 1.1.1.1
[R1-ospf-1]area 0
[R1-ospf-1-area-0.0.0.0]network 10.1.1.0 0.0.0.255
[R1-ospf-1-area-0.0.0.0]network 10.2.2.0 0.0.0.255
[R1-ospf-1-area-0.0.0.0]network 1.1.1.1 0.0.0.0

[R2]ospf 1 router-id 2.2.2.2
[R2-ospf-1]area 0
[R2-ospf-1-area-0.0.0.0]network 2.2.2.2 0.0.0.0
[R2-ospf-1-area-0.0.0.0]network 10.1.1.0 0.0.0.255
[R2-ospf-1-area-0.0.0.0]network 10.3.3.0 0.0.0.255
[R2-ospf-1-area-0.0.0.0]quit
[R2-ospf-1]area 1
[R2-ospf-1-area-0.0.0.1]network 10.4.4.0 0.0.0.255

[R3]ospf 1 router-id 3.3.3.3
[R3-ospf-1]area 0
[R3-ospf-1-area-0.0.0.0]network 3.3.3.3 0.0.0.0
[R3-ospf-1-area-0.0.0.0]network 10.2.2.0 0.0.0.255
[R3-ospf-1-area-0.0.0.0]network 10.3.3.0 0.0.0.255
[R3-ospf-1-area-0.0.0.0]quit
[R3-ospf-1]area 1
[R3-ospf-1-area-0.0.0.1]network 10.5.5.0 0.0.0.255

[R4]ospf 1 router-id 4.4.4.4
[R4-ospf-1]area 1
[R4-ospf-1-area-0.0.0.1]network 4.4.4.4 0.0.0.0
[R4-ospf-1-area-0.0.0.1]network 192.168.0.0 0.0.0.255
[R4-ospf-1-area-0.0.0.1]network 192.168.1.0 0.0.0.255
[R4-ospf-1-area-0.0.0.1]network 192.168.2.0 0.0.0.255
[R4-ospf-1-area-0.0.0.1]network 192.168.3.0 0.0.0.255
[R4-ospf-1-area-0.0.0.1]network 10.4.4.0 0.0.0.255
[R4-ospf-1-area-0.0.0.1]network 10.5.5.0 0.0.0.255

[R4-ospf-1]silent-interface LoopBack 1
[R4-ospf-1]silent-interface LoopBack 2
[R4-ospf-1]silent-interface LoopBack 3
[R4-ospf-1]silent-interface LoopBack 4

# 3. r1上配置默认路由，指向R5,通往外部网络
[R1]ip route-static 0.0.0.0 0 100.0.0.5
[R1-ospf-1]default-route-advertise

# 4. area1为减小路由表规模，配置为stub区域
[R2-ospf-1-area-0.0.0.1]stub
[R3-ospf-1-area-0.0.0.1]stub
[R4-ospf-1-area-0.0.0.1]stub

# 5. r4上配置loopback口模拟业务网段，要求所有业务网段的路由聚合为一条后发布到area0
[R2-ospf-1-area-0.0.0.1]abr-summary 192.168.0.0 22
[R3-ospf-1-area-0.0.0.1]abr-summary 192.168.0.0 22
<R1>display ip routing-table

# 6. R2上不允许存在192.168.2.0/24网段和192.168.3.0/24网段的路由
路由过滤
 1. 配置acl，匹配要过滤的路由
[R2]acl basic 2000
[R2-acl-ipv4-basic-2000]rule deny source 192.168.2.0 0.0.1.255
[R2-acl-ipv4-basic-2000]rule permit

2. 在ospf协议视图 配置路由过滤
[R2-ospf-1]filter-policy 2000 import

# 7. 为了保证协议安全，area0配置区域验证，验证密钥123456
[R1-ospf-1-area-0.0.0.0]authentication-mode simple plain 123456
[R2-ospf-1-area-0.0.0.0]authentication-mode simple plain 123456
[R3-ospf-1-area-0.0.0.0]authentication-mode simple plain 123456

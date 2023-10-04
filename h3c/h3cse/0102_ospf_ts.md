# 实验需求

1. 按照图示配置 IP 地址
2. 按照图示分区域配置 OSPF，要求使用环回口作为 Router-id，ABR 的环回口只宣告进 Area 0
3. 业务网段不允许出现协议报文
4. R5 模拟互联网，内网通过 R1 连接互联网，在 R1 上配置默认路由并引入到 OSPF
5. R1 上配置 EASY IP，两个业务网段都可以访问互联网
6. 通过调整链路 Cost，避免网络中出现等价路由
7. 为了实现 Area 0 快速收敛，`10.1.1.0/24` 链路上修改 Hello time 为 5 秒
8. 排除所有网络故障，使环境符合需求，并完成排错报告



<R1>display ip interface brief
<R1>display current-configuration
<R1>display ip routing-table

[R1-GigabitEthernet0/0]ip add 10.2.2.1 24
[R1-ospf-1]default-route-advertise always
//或者添加一条默认路由
[R1]ip route-static 0.0.0.0 0 202.1.1.5

[R2]ospf 1 router-id 2.2.2.2
[R2-ospf-1]area 1
[R2-ospf-1-area-0.0.0.1]undo network 10.1.1.0 0.0.0.255
[R2-ospf-1-area-0.0.0.1]quit
[R2-ospf-1]area 0
[R2-ospf-1-area-0.0.0.0]network 10.1.1.0 0.0.0.255

[R2-GigabitEthernet0/1]ospf timer dead 15
[R1-GigabitEthernet0/1]ospf timer hello 5

[R3-GigabitEthernet0/1]undo ospf network-type
[R3-ospf-1-area-0.0.0.1]undo network 3.3.3.3 0.0.0.0
[R3-ospf-1-area-0.0.0.0]network 3.3.3.3 0.0.0.0
[R3-ospf-1]silent-interface g0/2

[R4-ospf-1-area-0.0.0.1]undo network 4.4.4.4 0.0.0.0
[R4-ospf-1-area-0.0.0.0]network 4.4.4.4 0.0.0.0
[R4-ospf-1]silent-interface g0/2

[R3-GigabitEthernet0/1]ospf cost 1000



VPCS_7> ping 202.1.1.1
VPCS_7> ping 202.1.1.5
VPCS_7> ping 100.1.1.1


# 1. 基本配置，（重命名，ip地址）
    [R1]int g0/2
    [R1-GigabitEthernet0/2]ip add 192.168.1.254 24
    [R1]int g0/0
    [R1-GigabitEthernet0/0]ip add 10.2.2.1 24
    [R1]int g0/1
    [R1-GigabitEthernet0/1]ip add 10.1.1.1 24

    [R2]int g0/0
    [R2-GigabitEthernet0/0]ip add 10.2.2.2 24
    [R2]int g0/1
    [R2-GigabitEthernet0/1]ip add 10.3.3.2 24

    [R3]int g0/0
    [R3-GigabitEthernet0/0]ip add 10.3.3.3 24
    [R3]int g0/1
    [R3-GigabitEthernet0/1]ip add 10.4.4.3 24
    [R3]int g0/2
    [R3-GigabitEthernet0/2]ip add 192.168.2.254 24

    [R4]int g0/0
    [R4-GigabitEthernet0/0]ip add 10.1.1.4 24
    [R4]int g0/1
    [R4-GigabitEthernet0/1]ip add 10.4.4.4 24
    [R4]int g0/2
    [R4-GigabitEthernet0/2]ip add 10.6.6.4 24
    [R4]int g5/0
    [R4-GigabitEthernet5/0]ip add 10.5.5.4 24

    [R5]int g0/0
    [R5-GigabitEthernet0/0]ip add 10.6.6.5 24
    [R5]int g0/1
    [R5-GigabitEthernet0/1]ip add 10.5.5.5 24
    [R5]int g0/2
    [R5-GigabitEthernet0/2]ip add 192.168.3.254 24

    pc的ip地址为网段的第一位，分别是
    192.168.1.1/24
    192.168.2.1/24
    192.168.3.1/24
    配置好后分别ping自己的网关，查看连通性
    ping 192.168.1.254

# 2. 配置静态路由 （实现pc互通,r4-r5实现等价路由）
    1.0 -> 2.0 r1,r2,r3
    1.0 -> 3.0 r1,r4,r5

    2-> 1 r3,r4,r1
    2-> 3 r3,r4,r5 

    3-> 1 r5,r4,r1
    3-> 2 r5,r4,r3

    1-2
    [R1]ip route-static 192.168.2.0 24 10.2.2.2
    [R2]ip route-static 192.168.2.0 24 10.3.3.3

    2-1
    [R3]ip route-static 192.168.1.0 24 10.4.4.4
    [R1]ip route-static 192.168.1.0 24 10.1.1.1

    1-3
    [R1]ip route-static 192.168.3.0 24 10.1.1.4
    [R4]ip route-static 192.168.3.0 24 10.5.5.5
    [R4]ip route-static 192.168.3.0 24 10.6.6.5

    3-1
    [R5]ip route-static 192.168.1.0 24 10.5.5.4
    [R5]ip route-static 192.168.1.0 24 10.6.6.4
    [R4]ip route-static 192.168.1.0 24 10.1.1.1

    2-3
    [R3]ip route-static 192.168.3.0 24 10.4.4.4
    R4-R5的静态路由在1-3中已经配了

    3-2 //R5->R4 用默认路由
    [R5]ip route-static 0.0.0.0 0 10.5.5.4
    [R5]ip route-static 0.0.0.0 0 10.6.6.4
    [R4]ip route-static 192.168.2.0 24 10.4.4.3

# 3. 测试连通性
    <H3C>ping 192.168.2.1
    <H3C>ping 192.168.3.1

    <H3C>ping 192.168.1.1
    <H3C>ping 192.168.3.1

    <H3C>ping 192.168.1.1
    <H3C>ping 192.168.2.1

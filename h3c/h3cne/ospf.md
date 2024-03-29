# 1. 基本配置 （设备重命名，ip地址）
    [R1]int g0/0
    [R1-GigabitEthernet0/0]ip add 100.1.1.1 24
    [R1]int g0/1
    [R1-GigabitEthernet0/1]ip add 100.3.3.1 24
    [R1]interface LoopBack 0
    [R1-LoopBack0]ip add 1.1.1.1 32

    [R2]int g0/0
    [R2-GigabitEthernet0/0]ip add 100.1.1.2 24
    [R2]int g0/1
    [R2-GigabitEthernet0/1]ip add 100.2.2.2 24
    [R2]int lo0
    [R2-LoopBack0]ip add 2.2.2.2 32

    [R3]int g0/0
    [R3-GigabitEthernet0/0]ip add 100.4.4.3 24
    [R3]int g0/1
    [R3-GigabitEthernet0/1]ip add 100.2.2.3 24
    [R3]int lo0
    [R3-LoopBack0]ip add 3.3.3.3 32

    [R4]int g0/0
    [R4-GigabitEthernet0/0]ip add 100.3.3.4 24
    [R4]int lo0
    [R4-LoopBack0]ip add 4.4.4.4 32

    [R5]int g0/0
    [R5-GigabitEthernet0/0]ip add 100.4.4.5 24
    [R5]int lo0
    [R5-LoopBack0]ip add 5.5.5.5 32

# 2. 配置ospf 
    [R1]ospf 1 router-id 1.1.1.1
    [R1-ospf-1]area 0
    [R1-ospf-1-area-0.0.0.0]network 100.1.1.0 0.0.0.255
    [R1-ospf-1-area-0.0.0.0]network 1.1.1.1 0.0.0.0
    [R1-ospf-1]area 1
    [R1-ospf-1-area-0.0.0.1]network 100.3.3.0 0.0.0.255

    [R2]ospf 1 router-id 2.2.2.2
    [R2-ospf-1]area 0
    [R2-ospf-1-area-0.0.0.0]network 100.1.1.0 0.0.0.255
    [R2-ospf-1-area-0.0.0.0]network 100.2.2.0 0.0.0.255
    [R2-ospf-1-area-0.0.0.0]network 2.2.2.2 0.0.0.0

    [R3]ospf 1 router-id 3.3.3.3
    [R3-ospf-1]area 0
    [R3-ospf-1-area-0.0.0.0]network 100.2.2.0 0.0.0.255
    [R3-ospf-1-area-0.0.0.0]network 3.3.3.3 0.0.0.0
    [R3-ospf-1]area 2
    [R3-ospf-1-area-0.0.0.2]network 100.4.4.0 0.0.0.255

    [R4]ospf 1 router-id 4.4.4.4
    [R4-ospf-1]area 1
    [R4-ospf-1-area-0.0.0.1]network 100.3.3.0 0.0.0.255
    [R4-ospf-1-area-0.0.0.1]network 4.4.4.4 0.0.0.0

    [R5]ospf 1 router-id 5.5.5.5
    [R5-ospf-1]area 2
    [R5-ospf-1-area-0.0.0.2]network 100.4.4.0 0.0.0.255
    [R5-ospf-1-area-0.0.0.2]network 5.5.5.5 0.0.0.0

# 3. 检测连通性，查看ospf信息
<R4>ping -a 4.4.4.4 5.5.5.5
<R4>ping 100.4.4.5

[R1]display ospf peer
[R1]display ospf routing
[R1]display ospf lsdb
[R1]display ip routing-table

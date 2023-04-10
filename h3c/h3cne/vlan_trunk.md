# 1. 设备重命名和基本配置
    <H3C>system-view
    [H3C]sysname S1
    <S1>save
    <S1>more startup.cfg

    <H3C>system-view
    [H3C]sysname S2
    <S2>save

     四台pc配置ip,然后ping测试
    [H3C]ping 192.168.1.1
    [H3C]ping 192.168.1.2
    [H3C]ping 192.168.1.3
    [H3C]ping 192.168.1.4


# 2. 创建vlan
    [S1]vlan 10
    [S1-vlan10]vlan 20

    [S2]vlan 10
    [S2-vlan10]vlan 20

# 3. 把pc连接的端口加入对应的vlan （）
    [S1]interface GigabitEthernet 1/0/1
    [S1-GigabitEthernet1/0/1]port access vlan 10
    [S1]interface GigabitEthernet 1/0/2
    [S1-GigabitEthernet1/0/2]port access vlan 20

    [S2]vlan 10
    [S2-vlan10]port g1/0/1
    [S2-vlan10]vlan 20
    [S2-vlan20]port g1/0/2

# 4. 配置trunk接口，（s1和s2的g1/0/3都配置为trunk，允许vlan10和vlan20通过）
    [S1]int g1/0/3
    [S1-GigabitEthernet1/0/3]port link-type trunk
    [S1-GigabitEthernet1/0/3]port trunk permit vlan 10 20

    [S2]int g1/0/3
    [S2-GigabitEthernet1/0/3]port link-type trunk
    [S2-GigabitEthernet1/0/3]port trunk permit vlan 10 20

# 5. 测试
    <H3C>ping 192.168.1.{1-4}
    //pc3 只能ping通自己和192.168.1.3
    //pc4 只能ping通自己和192.168.1.4


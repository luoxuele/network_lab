# 1. 基础配置 （设备重命名，ip地址，包括网关）

# 2. 创建vlan并加入对应的端口
    [S1]vlan 10
    [S1]int g1/0/1
    [S1-GigabitEthernet1/0/1]port access vlan 10

    [S1]vlan 20
    [S1-vlan20]port g1/0/2

# 3. 配置vlanif接口的ip地址 （vlan-interface 10, vlan-interface 20）
    [S1]int Vlan-interface 10
    [S1-Vlan-interface10]ip add 192.168.1.254 24

    [S1]int Vlan-interface 20
    [S1-Vlan-interface20]ip add 192.168.2.254 24


# 4. 查看路由，并测试连通性
    [S1]display ip routing-table
    //可以发现有192.168.1.0/24 和192.168.2.0/24两个网段的直连路由

    <H3C>ping 192.168.1.254
    <H3C>ping 192.168.2.254
    <H3C>ping 192.168.2.1

# 1. 基本配置 （设备重命名，ip地址）
    [R1]int g0/0
    [R1-GigabitEthernet0/0]ip add 192.168.1.1 24

    [R2]int g0/0
    [R2-GigabitEthernet0/0]ip add 192.168.1.2 24
    [R2]int g0/1
    [R2-GigabitEthernet0/1]ip add 192.168.2.254 24

# 2. dhcp server
    [R1]dhcp enable
    [R1]dhcp server ip-pool 1
    [R1-dhcp-pool-1]network 192.168.2.0 24
    [R1-dhcp-pool-1]gateway-list 192.168.2.254
    [R1-dhcp-pool-1]dns-list 8.8.8.8 114.114.114.114

# 3. dhcp delay
    [R2]dhcp enable
    [R2]int g0/1
    [R2-GigabitEthernet0/1]dhcp select relay
    [R2-GigabitEthernet0/1]dhcp relay server-address 192.168.1.1

# 4. 配置路由 （R1上没有192.168.2.0/24 网段的路由）
    [R1]ip route-static 192.168.2.0 24 192.168.1.2

# 5. pc用dhcp获取ip
    <H3C>ping 192.168.1.1
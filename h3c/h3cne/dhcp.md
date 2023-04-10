# 1. 基础配置 （设配重命名，ip地址）
    [R1]int g0/0
    [R1-GigabitEthernet0/0]ip address 192.168.1.254 24

# 2. 配置dhcp服务（在R1上）
    [R1]dhcp enable
    [R1]dhcp server ip-pool 1
    [R1-dhcp-pool-1]network 192.168.1.0 24
    [R1-dhcp-pool-1]gateway-list 192.168.1.254
    [R1-dhcp-pool-1]dns-list 8.8.8.8 114.114.114.114

    [R1-dhcp-pool-1]forbidden-ip-range 192.168.1.1 192.168.1.20
    [R1]dhcp server forbidden-ip 192.168.1.21 192.168.1.30


# 3. 验证dhcp (pc上设置dhcp自动获取ip)
    //由于dhcp server 禁止了192.168.1.{1..30}之间的30个ip地址
    //所以pc获取到的地址是从192.168.1.31开始


# 5. 查看dhcp server的一些信息
    <R1>display dhcp server free-ip
    <R1>display dhcp server ip-in-use
    <R1>display dhcp server pool

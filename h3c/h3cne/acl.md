# 1. 基本配置 （设备重命名，ip地址）

        [R1]int g0/1
        [R1-GigabitEthernet0/1]ip add 192.168.1.254 24
        [R1]int g0/0
        [R1-GigabitEthernet0/0]ip add 100.1.1.1 24

        [R2]int g0/0
        [R2-GigabitEthernet0/0]ip add 100.1.1.2 24
        [R2]int g0/1
        [R2-GigabitEthernet0/1]ip add 100.2.2.2 24
        [R2]int g0/2
        [R2-GigabitEthernet0/2]ip add 192.168.2.254 24

        [R3]int g0/0
        [R3-GigabitEthernet0/0]ip add 192.168.3.254 24
        [R3]int g0/1
        [R3-GigabitEthernet0/1]ip add 100.2.2.3 24

        //server
        username:   root
        password: 123456

        //修改对应的ip
        https://cloud-atlas.readthedocs.io/zh_CN/latest/linux/alpine_linux/alpine_static_ip.html
        vi /etc/network/interfaces

        localhost:~# cat /etc/network/interfaces
        auto eth1
        iface eth1 inet static
                address 192.168.3.1
                netmask 255.255.255.0
                gateway 192.168.3.254

        //重启网卡服务
        /etc/init.d/networking restart
        //查看ip地址，并ping测试网关
        localhost:~# ip a
        localhost:~# ping 192.168.3.254 -c 4

# 2， 网络互通
        [R1]ospf 1
        [R1-ospf-1]area 0
        [R1-ospf-1-area-0.0.0.0]network 192.168.1.254 0.0.0.0
        [R1-ospf-1-area-0.0.0.0]network 100.1.1.1 0.0.0.0

        [R2]ospf 1
        [R2-ospf-1]area 0
        [R2-ospf-1-area-0.0.0.0]network 100.1.1.2 0.0.0.0
        [R2-ospf-1-area-0.0.0.0]network 100.2.2.2 0.0.0.0
        [R2-ospf-1-area-0.0.0.0]network 192.168.2.254 0.0.0.0

        [R3]ospf 1
        [R3-ospf-1]area 0
        [R3-ospf-1-area-0.0.0.0]network 100.2.2.3 0.0.0.0
        [R3-ospf-1-area-0.0.0.0]network 192.168.3.254 0.0.0.0

        //server
        route -n
        localhost:~# route add -net 192.168.1.0/24 gw 192.168.3.254
        localhost:~# route add -net 192.168.2.0/24 gw 192.168.3.254

        localhost:~# ping 192.168.1.1 -c 4
        localhost:~# ping 192.168.2.1 -c 4

        //server 设置ip和route (临时)
        ip addr add 192.168.3.1/24 dev eth1
        ip a del 192.168.1.2/24 dev eth1

        localhost:~# ip route show
        localhost:~# ip route list

        //设置路由，单独的网段路由或者默认路由
        ip route add 192.168.1.0/24 via 192.168.3.254
        ip route add 192.168.2.0/24 via 192.168.3.254 dev eth1

        ip route add default via 192.168.3.254

        ping 192.168.1.1 -c 4
        ping 192.168.2.1 -c 4


# 3. 配置server 服务

# 4. 配置acl
## 1. 192.168.1.0/24 网段不能访问 192.168.2.0/24 网段，用基本acl实现
        分析：基本acl只能过滤源ip，只能在R2的g0/2接口的出方向配置 包过滤
        [R2]acl basic 2000
        [R2-acl-ipv4-basic-2000]rule deny source 192.168.1.0 0.0.0.255
        [R2]int g0/2
        [R2-GigabitEthernet0/2]packet-filter 2000 outbound

        <H3C>ping 192.168.2.254
        <H3C>ping 192.168.2.1
        254能ping通，1 ping不通

## 2. pc5 (192.168.1.1/24) 可以访问server的telnet服务，但不能访问ftp服务
## 3. pc6 (192.168.1.2/24) 可以访问server的ftp服务，但不能访问telnet服务

        分析：可以离源地址最近的接口入方向配置包过滤，（R1的g0/1）,因为h3c的acl用于包过滤的默认动作是允许，所以只需要分别禁止访问ftp和telnet就行了


        [R1]acl advanced 3000
        [R1-acl-ipv4-adv-3000]rule deny tcp source 192.168.1.1 0 destination 192.168.3.1 0 destination-port range 20 21
        [R1-acl-ipv4-adv-3000]rule deny tcp source 192.168.1.2 0 destination 192.168.3.1 0 destination-port eq 23

        [R1]int g0/1
        [R1-GigabitEthernet0/1]packet-filter 3000 inbound

        //删除规则
        [R1-acl-ipv4-adv-3000]undo rule 0

## 4. 192.168.2.0/24 网段不能访问server,要求通过高级acl实现
        分析：在R2的g0/2入方向设置包过滤，源地址是2.0/24网段，目的ip是192.168.3.1

        [R2]acl advanced 3000
        [R2-acl-ipv4-adv-3000]rule deny ip source 192.168.2.0 0.0.0.255 destination  192.168.3.1 0
        [R2-acl-ipv4-adv-3000]quit
        [R2]int g0/2
        [R2-GigabitEthernet0/2]packet-filter 3000 inbound

        <H3C>ping 192.168.3.254
        <H3C>ping 192.168.3.1

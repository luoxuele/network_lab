# 1. 基本配置 （pc的ip地址，设备重命名）

# 2. 开启802.1x身份认证 （在交换机S1上）
    //先全局开启，然后在每一个接口中开启
    [S1]dot1x
    [S1]int g1/0/1
    [S1-GigabitEthernet1/0/1]dot1x
    [S1-GigabitEthernet1/0/1]int g1/0/2
    [S1-GigabitEthernet1/0/2]dot1x
    [S1-GigabitEthernet1/0/2]int g1/0/3
    [S1-GigabitEthernet1/0/3]dot1x


# 3. 创建本地认证用户 （user:luoxue password:luoxue123 ,802.1x验证的用户类型必须是network,服务类型是lan-access）
    [S1]local-user luoxue class network
    [S1-luser-network-luoxue]password simple luoxue123
    [S1-luser-network-luoxue]service-type lan-access

    //模拟环境无法验证802.1x

# 4. 创建端口隔离组，并把对应的接口加入到隔离组（一个隔离组的端口无法互相访问，所以三台pc无法互相访问）
    [S1]port-isolate group 1
    [S1]int g1/0/1
    [S1-GigabitEthernet1/0/1]port-isolate enable group 1
    [S1]int g1/0/2
    [S1-GigabitEthernet1/0/2]port-isolate enable group 1
    [S1]int g1/0/3
    [S1-GigabitEthernet1/0/3]port-isolate enable group 1


# 1. 基本配置 （设备重命名，pc ip地址）

# 2. 创建bridge-Aggregation接口，并把对应的接口加入到聚合口中 （把g1/0/1和g1/0/2 加入到聚合口bridge-aggregation 1 中）
    [S1]interface Bridge-Aggregation 1
    [S1]interface GigabitEthernet 1/0/1
    [S1-GigabitEthernet1/0/1]port link-aggregation group 1
    [S1-GigabitEthernet1/0/1]int g1/0/2
    [S1-GigabitEthernet1/0/2]port link-aggregation group 1

    [S2]int bri 1
    [S2]int g1/0/1
    [S2-GigabitEthernet1/0/1]port link-aggregation group 1
    [S2-GigabitEthernet1/0/1]int g1/0/2
    [S2-GigabitEthernet1/0/2]port link-agg group 1


    [S1]display link-aggregation verbose
    [S1]display interface brief

# 3. 把聚合口的link-type设置成trunk，允许所有vlan通过
    [S1]interface Bridge-Aggregation 1
    [S1-Bridge-Aggregation1]port link-type trunk
    [S1-Bridge-Aggregation1]port trunk permit vlan all

    [S2]interface Bridge-Aggregation 1
    [S2-Bridge-Aggregation1]port link-type trunk
    [S2-Bridge-Aggregation1]port trunk permit vlan all

# 4. 断开聚合口的一条物理链路，测试连通性
    [S1]int g1/0/1
    [S1-GigabitEthernet1/0/1]shutdown

    <H3C>ping 192.168.1.2
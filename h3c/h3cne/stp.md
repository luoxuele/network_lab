
# 1. 基础配置 （设备重命名，pc要打开网口，不需要配ip地址）

# 2. 运行设备，等待stp收敛，查看stp运行状态，找到根网桥和闭塞端口
    <S1>display stp
    <S1>display stp brief
    <S1>display stp root
    <S4>display stp brief

    s1是根网桥，s4的g1/0/2端口是阻塞端口 （）


# 3. 使s4成为根网桥 （默认优先级是32768，把s4的stp优先级设置成4096就行了）
    [S4]stp priority 4096

    <S1>display stp root
    <S1>display stp brief
    //根网桥变成S4了，阻塞端口变成S1的g1/0/2了


# 4. 使阻塞端口出现在S2上 （把s2到s1的cost改大，让S4-> S3 -> S1的值更小,千兆口默认是20，）
    [S2]int g1/0/2
    [S2-GigabitEthernet1/0/2]stp cost 1000

    <S2>display stp brief
    //阻塞端口变成S2的g1/0/2了


# 5. 把s1连接pc的所有端口配置为边缘端口 （边缘端口不参与stp计算）
    <S1>display interface brief
    <S1>display stp brief

    [S1]int g1/0/3
    [S1-GigabitEthernet1/0/3]stp edged-port
    [S1]int g1/0/4
    [S1-GigabitEthernet1/0/4]stp edged-port

    <S1>display interface brief
    <S1>display stp brief


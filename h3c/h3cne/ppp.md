# 1. 基本配置 （设配重命名）

# 2. 

[R1-Serial1/0]ip add 192.168.1.1 24
[R2-Serial3/0]ip add 192.168.1.2 24
[R2]display ip interface brief
[R2]ping 192.168.1.1

[R2]local-user heheda class network
[R2-luser-network-heheda]password simple 123456
[R2-luser-network-heheda]service-type ppp
[R2-Serial3/0]ppp authentication-mode chap

[R1-Serial1/0]shutdown
[R1-Serial1/0]undo shutdown
[R1-Serial1/0]display ip interface brief

[R1-Serial1/0]ppp chap user heheda
[R1-Serial1/0]ppp chap password simple 123456
[R1]display ip interface brief
[R1]ping 192.168.1.2


# 3. ppp-mp
    [R2]interface MP-group 1
    [R2]int s1/0
    [R2-Serial1/0]ppp mp MP-group 1
    [R2]int s2/0
    [R2-Serial2/0]ppp mp MP-group 1
    [R2]display ip interface brief

    [R3]interface MP-group 1
    [R3]int s1/0
    [R3-Serial1/0]ppp mp MP-group 1
    [R3]int s2/0
    [R3-Serial2/0]ppp mp MP-group 1
    [R3]display ip interface brief

    [R2]int mp 1
    [R2-MP-group1]ip add 192.168.2.2 24
    [R3]int mp 1
    [R3-MP-group1]ip add 192.168.2.3 24
    [R2]ping 192.168.2.3

    [R2]local-user r2 class network
    [R2-luser-network-r2]password simple 123456
    [R2-luser-network-r2]service-type ppp

    [R2]int s1/0
    [R2-Serial1/0]ppp authentication-mode chap
    [R2-Serial1/0]ppp chap user r3
    [R2-Serial1/0]ppp chap password simple 123456
    [R2]int s2/0
    [R2-Serial2/0]ppp authentication-mode chap
    [R2-Serial2/0]ppp chap user r3
    [R2-Serial2/0]ppp chap password simple 123456

    [R3]local-user r3 class network
    [R3-luser-network-r3]password simple 123456
    [R3-luser-network-r3]service-type ppp

    [R3]int s1/0
    [R3-Serial1/0]ppp authentication-mode chap
    [R3-Serial1/0]ppp chap user r2
    [R3-Serial1/0]ppp chap password simple 123456
    [R3]int s2/0
    [R3-Serial2/0]ppp authentication-mode chap
    [R3-Serial2/0]ppp chap user r2
    [R3-Serial2/0]ppp chap password simple 123456

    [R3-MP-group1]shutdown
    [R3-MP-group1]display ip interface brief
    [R3-MP-group1]ping 192.168.2.2

    [R3-MP-group1]undo shutdown
    [R3-MP-group1]ping 192.168.2.2


    //如果双方验证密码一样，可以不用指定密码
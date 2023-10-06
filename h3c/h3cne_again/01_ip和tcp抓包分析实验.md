# 实验目标



# 实验步骤

## 1. 基本ip配置

    [R1]int g0/0
    [R1-GigabitEthernet0/0]ip add 1.1.1.1 24
    [R2]int g0/0
    [R2-GigabitEthernet0/0]ip add 1.1.1.2 24

## 2. 抓包，用R1 ping R2 ,查看ping包

    <R1>ping 1.1.1.2

## 3. R2开启ftp服务，创建用户ftpuser,密码abcd123456

    [R2]ftp server enable
    [R2]local-user ftpuser class manage
    [R2-luser-manage-ftpuser]authorization-attribute user-role level-15
    [R2-luser-manage-ftpuser]password simple abcd123456
    [R2-luser-manage-ftpuser]service-type ftp



### 4. R1登录R2的ftp服务,并查看抓包情况

    <R1>ftp 1.1.1.2
# 实验目标

配置password-control相关策略



# 实验步骤

## 1. 配置ssh本地aaa认证 （参考001_ssh）

    [R1]ssh server enable
    
    [R1]local-user admin
    [R1-luser-manage-admin]authorization-attribute user-role level-3
    [R1-luser-manage-admin]service-type ssh ter
    [R1-luser-manage-admin]service-type ssh terminal
    [R1-luser-manage-admin]password simple abcd123456
    
    [R1]user-interface vty 0 4
    [R1-line-vty0-4]authentication-mode scheme
    [R1-line-vty0-4]protocol inbound ssh
    
    [R1]user-interface aux 0
    [R1-line-aux0]authentication-mode scheme

## 2. 配置password-control
### 1. Enabling password control

    [R1]password-control enable
    [R1]undo password-control aging enable
    [R1]undo password-control history enable
    [R1]password-control length 10
    [R1]password-control composition type-number 4 type-length 1



### 2. 其它

    [R1]password-control login-attempt 5 exceed lock-time 10
    [R1]password-control update-interval 0
    [R1]password-control login idle-time 0
    [R1]password-control complexity user-name check
    [R1]password-control complexity same-character check

### 3. 参考链接

	https://www.h3c.com/en/d_201905/1179419_294551_0.htm
	https://www.h3c.com/en/d_202102/1383572_294551_0.htm

## 3. 测试

    PS C:\Users\admin\Desktop> ssh 192.168.56.2
    
    会提示需要修改密码
    老密码：abcd123456
    新密码：Abcd@123456

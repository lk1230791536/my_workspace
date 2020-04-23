### 连接
  - sh zkCli.sh -server 127.0.0.1:12181
### 基本命令
  - ls 查看 eg: ls /name
  - get 获取节点内容
  - stat（ls -s） 获取节点状态
  - create [-s] [-e] path data acl
    - create -e 创建临时节点,断开重连之后，临时节点自动消失
    - create -s 创建顺序节点 自动累加
  - set path /cjk [version] 修改节点
  - delete /cjk [version] 删除节点
  - stat -w /cjk 设置watch事件:创建cjk时触发
  - get -w /cjk 设置watch事件:修改节点触发watcher事件、删除触发watcher事件
### ACL权限控制
  - ZK的节点有5种操作权限：CREATE、READ、WRITE、DELETE、ADMIN 也就是 增、删、改、查、管理权限，这5种权限简写为crwda
  - 身份的认证有4种方式：
    - world：默认方式，相当于全世界都能访问
    - auth：代表已经认证通过的用户(cli中可以通过addauth digest user:pwd 来添加当前上下文中的授权用户)
    - digest：即用户名:密码这种方式认证，这也是业务系统中最常用的
    - ip：使用Ip地址认证
  - setAcl 设置权限
    - setAcl /merryyou/test world:anyone:crwa
  - acl Auth 密码明文设置
    - addauth digest test:change_me  #注册test:change_me 账号密码,生成V28q/NynI4JI3Rk54h0r8O5kMug=密文密码
    - setAcl /name auth:test:change_me:cdrwa
  - acl digest 密码密文设置
    - setAcl /age digest:test:V28q/NynI4JI3Rk54h0r8O5kMug=:cdra

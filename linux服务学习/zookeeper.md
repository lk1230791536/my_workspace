### 连接
  - sh zkCli.sh -server 127.0.0.1:12181
### 基本命令
  - ls 查看 eg: ls /name
  - get 获取节点内容
  - stat（ls -s） 获取节点状态
  - create [-s] [-e] path data acl
    - create -e 创建临时节点,断开重连之后，临时节点自动消失
    - create -s 创建顺序节点 自动累加
  - set path data [version] 修改节点
  - delete path [version] 删除节点
  - stat path [watch] 设置watch事件

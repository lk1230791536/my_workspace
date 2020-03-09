spawn               交互程序开始后面跟命令或者指定程序
expect              获取匹配信息匹配成功则执行expect后面的程序动作
send exp_send       用于发送指定的字符串信息
exp_continue        在expect中多次匹配就需要用到
send_user           用来打印输出 相当于shell中的echo
exit                退出expect脚本
eof                 expect执行结束 退出
set                 定义变量
puts                输出变量
set timeout         设置超时时间
interact 　　　　　　 允许用户交互
\r                  回车
\n                  换行
##################################################################################
#!/bin/bash 
ip=$1  
user=$2 
password=$3 

expect <<EOF  
    set timeout 10 
    spawn ssh $user@$ip 
    expect { 
        "yes/no" { send "yes\n";exp_continue } 
        "password" { send "$password\n" }
    } 
    expect "]#" { send "useradd hehe\n" } 
    expect "]#" { send "touch /tmp/test.txt\n" } 
    expect "]#" { send "exit\n" } expect eof 
 EOF  
 #./ssh5.sh 192.168.1.10 root 123456 
 
###########################################################
##instant
#!/bin/bash
#filename'cjk.sh'
read -p "please input your number: " aa
if [ "$aa"x == "3"x ];then
    echo "ok"
    exit 0
else
    exit 9
fi

#!/bin/bash
expect  << EOF
spawn sh cjk.sh
expect {
"*number:" {send "4\r";exp_continue}
}
catch wait result;  #将wait命令的返回值存储到result变量中. result变量并不是一个特殊变量, 你可以随意换一个新名字(比如retVal).
puts \$result;  #wait命令的返回值是一个"%d %s 0 %d"格式的字符串,第0个值是pid,第1个是spawn_id(不知道它具体带表了什么),第2个应当是代表脚本是否正常完成,第3个是子进程的返回值.
#这里须要加上转义字符\$。否则会把$result解析成shell里面的变量，但这里面的$result是须要expect解析的。
exit [lindex \$result 3]
EOF

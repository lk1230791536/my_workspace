#!/bin/bash
#查看CPU、内存等资源
w
vmstat
top
#查看监听端口号
netstat -ntlp
#watch指令可以间歇性的执行程序，将输出结果以全屏的方式显示，默认是2s执行一次。watch将一直运行，直到被中断。
watch -n 5 sh test.sh #隔5秒执行脚本
watch command
#根据端口号查进程
lsof -i:80
#根据进程号查端口号
lsof -i |grep pid

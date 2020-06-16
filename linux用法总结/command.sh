#!/bin/bash
function other(){
  #生成随机数
  systemid_temp=`cat /proc/sys/kernel/random/uuid`
  systemid=${systemid_temp//-/}
}
function commands(){
  #强制复制
  \cp -f *.txt tempry/
  #修改用户密码
  chage -l testuser #查看有效期
  chage -M 99999 testuser #修改为永久
  #系统时间
  date +%Y%m%d  #显示当天年月日
  date +%Y%m%d --date="+1 day"  #显示前一天的日期
  date +%Y%m%d --date="-1 day"  #显示后一天的日期
  date +%s  #从 1970 年 1 月 1 日 00:00:00 UTC 到目前为止的秒数（时间戳）可用于判断时间过期
  #控制程序运行的时间
  timeout 10 command
}
function search(){
  find $installDir/tomcat_*/webapps/*/WEB-INF  -name 'bootstrap.yml'
}
kill -0 uid #检查一个进程是否存在，存在返回0

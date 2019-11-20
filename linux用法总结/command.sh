#!/bin/bash
function other(){
  #生成随机数
  systemid_temp=`cat /proc/sys/kernel/random/uuid`
  systemid=${systemid_temp//-/}
}
function commands(){
  #强制复制
  \cp -f *.txt tempry/
}
function search(){
  find $installDir/tomcat_*/webapps/*/WEB-INF  -name 'bootstrap.yml'
}

#!/bin/bash
currentDir=$(dirname $0)
if [ ${currentDir} == "." ];then
    currentDir=$PWD
fi
#日志处理
function log_info ()
{
    if [ ! -d /var/log/huawei/robo/pwd ]; then
        mkdir -p /var/log/huawei/robo/pwd
    fi
    DATE_N=`date "+%Y-%m-%d %H:%M:%S"`
    USER_N=`whoami`
    echo "${DATE_N} ${USER_N} execute $0 [INFO] $@" >>${log_file}
}
function log_error ()
{
    if [ ! -d /var/log/huawei/robo/pwd ]; then
        mkdir -p /var/log/huawei/robo/pwd
    fi
    DATE_N=`date "+%Y-%m-%d %H:%M:%S"`
    USER_N=`whoami`
    echo -e "\033[41;37m ${DATE_N} ${USER_N} execute $0 [ERROR] $@ \033[0m"  >>${log_file}
}
function fn_log ()  {
    if [  $? -eq 0  ]
    then
        log_info "$@ successed."
        echo -e "\033[32m $@ successed. \033[0m"
    else
        log_error "$@ failed."
        echo -e "\033[41;37m $@ failed. \033[0m"
        exit 1
    fi
}
#密码复杂度校验
function ispwd () {
    passwd=$1
    strupp=`echo $passwd | grep -E --color '^(.*[A-Z]).*$'`
    strlow=`echo $passwd | grep -E --color '^(.*[a-z]+).*$'`
    strnum=`echo $passwd | grep -E --color '^(.*[0-9]).*$'`
    strts=`echo $passwd | grep -E --color '^(.*\W).*$'`
    symboltype=0
    if [ -n "${strupp}" ]; then
        symboltype=`expr $symboltype + 1`
    fi
    if [ -n "${strlow}" ]; then
        symboltype=`expr $symboltype + 1`
    fi
    if [ -n "${strnum}" ]; then
        symboltype=`expr $symboltype + 1`
    fi
    if [ -n "${strts}" ]; then
        symboltype=`expr $symboltype + 1`
    fi
    if [ `echo $passwd | awk '{print NF}'` -ne 1 ];then
        return 1
    fi
    if [[ $passwd =~ ";" ]];then
        return 1
    fi
    if [[ $passwd =~ '\' ]];then
        return 1
    fi
    if [[ $passwd =~ "'" ]];then
        return 1
    fi
    if [ $symboltype -lt 3 ]; then
        return 1
    fi
    return 0
}
#IP校验
function check_ip() {
    IP=$1
    if [[ $IP =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
        FIELD1=$(echo $IP|cut -d. -f1)
        FIELD2=$(echo $IP|cut -d. -f2)
        FIELD3=$(echo $IP|cut -d. -f3)
        FIELD4=$(echo $IP|cut -d. -f4)
        if [ $FIELD1 -le 255 -a $FIELD2 -le 255 -a $FIELD3 -le 255 -a $FIELD4 -le 255 ]; then
            :
        else
            echo -e "\033[41;37m IP $IP not available! \033[0m"
            return 1
        fi
    else
        echo -e "\033[41;37m IP format error! \033[0m"
        return 1
    fi
}
function get_ip(){
    count_1=1
    while true; do
        if [ $count_1 -le 3 ]; then
            read -r -p "Please enter the IP: " IP
            string_check $IP
            if [ $? -ne 0 ];then
                count_1=`expr $count_1 + 1`
                continue
            fi
            check_ip $IP
            if [ $? -ne 0 ];then
                count_1=`expr $count_1 + 1`
                continue
            fi
            break
        else
            log_error "Add vCenter user fail!"
            echo "Add vCenter user fail!"
            exit 1
        fi
    done
}

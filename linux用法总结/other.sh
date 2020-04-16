######修改后台为中文
vim vim /etc/locale.conf
LANG="zh_CN.UTF-8"

######生成随机数
#方法一：通过系统环境变量($RANDOM)实现：
echo "$RANDOM"|md5sum|cut -c 5-15
#方法二：通过openssl产生随机数，示例：
openssl rand -hex 8
#方法三：通过时间（date）获取随机数，示例：
date +%s%N  #%N微秒
#方法四:通过UUID生成随机数,示例：
cat /proc/sys/kernel/random/uuid
uuidgen
#上面的随机数长短不一,可以使用md5sum统一格式：
uuidgen|md5sum|cut -c 2-10

######进度条
printf #格式化输出："-"表示左对齐, "10 10 4 4" 表示占的字符位数；%s字符串；%%表示%本身
#!/bin/bash
function Proceess(){
spa=''
i=0
while [ $i -le 100 ]
do
 printf "[%-50s] %d%% \r" "$spa" "$i";
 sleep 0.5
 ((i=i+2))
 spa+='#'
done
echo
}

#!/bin/bash
nohup sh 123.sh >> /dev/null 2>&1 &
spa=''
i=0
echo "start"
while [ $i -le 4 ]
do
    if [[ $(ps -ef |grep 123.sh|grep -v grep|wc -l) -gt 0 ]];then
    printf "\r wait%-3s \r" "$spa" ;
    sleep 1
    ((i=i+1))
    if [ $i -gt 3 ];then
    i=1
    spa='.'
    fi
    spa+='.'
    else
        break
    fi
done
echo ""
echo "finish"
exit 0

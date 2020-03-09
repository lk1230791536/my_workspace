##修改后台为中文
vim vim /etc/locale.conf
LANG="zh_CN.UTF-8"

##生成随机数
#方法一：通过系统环境变量($RANDOM)实现：
echo "$RANDOM"|md5sum|cut -c 5-15
#方法二：通过openssl产生随机数，示例：
openssl rand -base64 8
#方法三：通过时间（date）获取随机数，示例：
date +%s%N  #%N微秒
#方法四:通过UUID生成随机数,示例：
cat /proc/sys/kernel/random/uuid
uuidgen
#上面的随机数长短不一,可以使用md5sum统一格式：
uuidgen|md5sum|cut -c 2-10

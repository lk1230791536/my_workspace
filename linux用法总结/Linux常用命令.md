# Linux常用命令1
- ***curl***
   - `curl -k -s http://127.0.0.1:port`
   - -k:允许不使用证书到SSL站点
   - -s:静音模式。不输出任何东西
   
- ***tee***
   - 读取标准输入的数据，并将其内容输出成文件，配合管道|使用
   - -a:追加到文件
   
- ***date***
   - date +%Y%m%d  #显示当天年月日
   - date +%Y%m%d --date="+1 day"  #显示前一天的日期
   - date +%Y%m%d --date="-1 day"  #显示后一天的日期
   - date +%s  #从 1970 年 1 月 1 日 00:00:00 UTC 到目前为止的秒数（时间戳）可用于判断时间过期
   
- ***timeout*** (控制程序运行的时间)
   - eg:timeout 10 command
   
- ***find*** [路径] [选项] [操作]
   - -name 文件名查找  #find /etc -name '*.conf'
   - -iname 不区分大小写
   - -user/-group 属主/属组查找
   - -type 文件类型查找
      - f 文件; d 目录; c 字符设备; b 块设备; l 链接文件; p 管道
   - -size 文件大小查询  #find /etc -size -2M
   - -mtime 根据时间(天)查找   #find /etc -mtime +5 -name '*.log'
      - -n n天内修改文件; +n n天外修改文件; n 第n天的修改文件
   - -mmin 根据时间（分）查找
   - -mindepth n 从第n级目录开始搜索
   - -maxdepth n 表示至多搜索到第 n-1 级子目录
- ***xargs*** (可以将管道或标准输入（stdin）数据转换成命令行参数，也能够从文件的输出中读取数据;多行变单行，单行变多行)
   - 多行输入单行输出  #cat test.txt | xargs
   - -n 选项多行输出 #cat test.txt | xargs -n3
   - -d 选项可以自定义一个定界符
   
- ***touch*** 
   - 修改文件时间 touch -mt 199209121515 test.log
      


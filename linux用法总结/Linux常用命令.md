# Linux常用命令
- curl 
   - `curl -k -s http://127.0.0.1:port`
   - -k:允许不使用证书到SSL站点
   - -s:静音模式。不输出任何东西
- tee
   - 读取标准输入的数据，并将其内容输出成文件，配合管道|使用
   - -a:追加到文件
- date
   - date +%Y%m%d  #显示当天年月日
   - date +%Y%m%d --date="+1 day"  #显示前一天的日期
   - date +%Y%m%d --date="-1 day"  #显示后一天的日期
   - date +%s  #从 1970 年 1 月 1 日 00:00:00 UTC 到目前为止的秒数（时间戳）可用于判断时间过期
- timeout (控制程序运行的时间)
   - eg:timeout 10 command


##flock文件锁之实际运用
#前面未获取到锁直接返回 直到其他运行完毕 这个才开始运行
#-x写入锁（排他锁）;-n非阻塞模式
* * * * * (flock -xn ./test.lock -c "sh /root/test.sh") #crontab运用flock防止重复执行

##timeout运行指定的命令，如果在指定时间后仍在运行，则杀死该进程
timeout 10 command

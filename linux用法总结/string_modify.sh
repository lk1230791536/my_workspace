#!/bin/bash
##sed字段操作
function sed(){
  ##(如果sed中有变量，将单引号变为双引号)
  #查找指定内容的行号
  LINE_NUM=$(sed -n -e '/xxxx/='  aaa.txt)
  #查找范围内指定的行号
  LINE_NUM=`sed -n "/start/,/target/=" aaa.txt |tail -n1`
  #显示特定行号内容
  awk 'NR==4 {print}' aaa.txt
  #根据已知行号整行替换（行头有两个空格）
  sed -i $LINE_NUM'c \  xxxx' aaa.txt
  #删除范围内容
  sed -i '/start/,/end/d' aaa.txt
  #替换范围中的内容
  sed -i '/start/,/end/ s/aa/bb/g' aaa.txt
  sed -n '/start/,/end/ s/aa/bb/p' aaa.txt
  #替换行内容
  sed -i '/aa/c bb' aaa.txt
  #替换变量
  sed -i s"/ip/$ip/g" *.txt
  #特定行号后追加内容
  sed -i ${LINE_NUM}'s/$/content/' aaa.txt
  #删除空行
  sed -i '/^\s*$/d' aaa.txt
}
function awk(){
    #第一行不显示
    awk '{if (NR>1){print $3}}' aaa.txt
    #显示特定行号内容
    awk 'NR==4 {print}' aaa.txt
}
function variable(){
  aa='cjk-fda-123'
  echo ${aa/-/#}  #/匹配第一个，替换
  echo ${aa//-/#} #/贪婪匹配全部，替换
  echo ${aa#*fda} #截取fda右测所有
  echo ${aa%fda*} #截取fda左侧所有
  echo ${aa:2:3}  #根据游标截取
  echo ${#aa} #显示字符串长度
}
function grep(){
  #grep 注：使用grep匹配时需使用双引号引起来（单引号为强引用），防止被系统误认为参数或者特殊命令而报错。
  --color=auto：#对匹配到的文本着色后进行高亮显示；
  -i：#忽略字符的大小写
  -o：#仅显示匹配到的字符串
  -v：#显示不能被模式匹配到的行
  -E：#支持使用扩展的正则表达式
  -q：#静默模式，即不输出任何信息
  -A #：显示被模式匹配的行及其后#行
  -B #：显示被模式匹配的行及其前#行
  -C #：显示被模式匹配的行及其前后各#行
  #过滤空行
  grep -e [[:alnum:]] -e [[:punct:]] aa
  grep -v ^$ aa
}


#!/bin/bash
##sed字段操作
function sed(){
  ##(如果sed中有变量，将单引号变为双引号)
  #查找指定内容的行号
  LINE_NUM=$(sed -n '/xxxx/='  aaa.txt)
  #查找范围内指定的行号
  LINE_NUM=`sed -n "/start/,/target/=" aaa.txt |tail -n1`
  #显示特定行号
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
}
function variable(){
  aa='cjk-fda-123'
  echo ${aa/-/#}  #/匹配第一个
  echo ${aa//-/#} #/贪婪匹配全部
  echo ${aa#*fda} #截取fda右测所有
}


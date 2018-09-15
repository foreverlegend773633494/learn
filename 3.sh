#!/bin/bash
read -p "请输入一个正整数字:" number
[ $number -eq 1 ] && echo "$number不是质数" && exit
[ $number -eq 2 ] && echo "$number是质数" && exit
for i in `seq 2 $[$number-1]`
	do
	 [ $[$number%$i] -eq 0 ] && echo "$number不是质数" && exit
	done
echo "$number是质数" && exit

#/root/.pyenv/versions/3.6.6/bin/python
# -*-coding:UTF-8 -*-
while True:
	print ("*"*10)
	print ("""请选择项目序号
1.项目一
2.项目二
3.项目三
输入q退出""")
	print ("*"*10)
	a = input("在此输入项目序号")
	if a == "1":
		print ("选择了项目1")
		break
	elif a == "2":
		print ("选择了项目2")
		break
	elif a == "3":
		print ("选择了项目3")
		break
	elif a == "q":
		print ("退出脚本")
		break
	else:
		continue

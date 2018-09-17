#/root/.pyenv/versions/3.6.6/bin/python
# -*-coding:UTF-8 -*-
import string,sys,random
def passsc (n,m):
	for j in range(m):
		pwd = ''
		a = string.ascii_letters + string.digits
		for i in range(n):
			pwd += random.choice(a)
		print(pwd)
if __name__ == '__main__' :
	passsc(int(sys.argv[1]),int(sys.argv[2]))

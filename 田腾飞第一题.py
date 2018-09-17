#/root/.pyenv/versions/3.6.6/bin/python
# -*-coding:UTF-8 -*-
def fun (m,n):
    a = open(m,'r')
    b = open(n,'w')
    for i in a:
        b.write(i)
    b.flush()
    a.close()
    b.close()
j1 = input("源文件")
j2 = input("目标文件")
fun (j1,j2)
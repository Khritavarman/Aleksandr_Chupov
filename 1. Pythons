#coding: utf-8

import os
lst = os.listdir('c:\prog2')     
#print (lst)

x = open("c:/prog2/result.txt", "w")      
x.write('')
x.close()

for i in lst:
    a = open('c:\prog2/' + i)
    b = a.read().count('python')

    if b > 0:
    	print (i, b)
    	x = open ('c:/prog2/result.txt', 'a')
    	x.write(str(i) + str('    -    ') + str(b) + '\n')
    	x.close()

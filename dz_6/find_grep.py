#coding: utf-8
import os, sys

#Функция-генератор find

def find (rash = '.py'):
    for filename in os.listdir('.'):
        if filename.endswith (rash):
            for i, line in enumerate(open(filename)): 
                yield filename,i, line

#Функция-генератор grep

def grep (gen, substr):
    for name, i, s in gen:
        if substr in s:
            yield name, i, s
            
#Запрос
str_vvod = input ('Введите данные для поиска:')

#Вывод
for name, i, s  in grep (gen=find ('.py'),substr=str_vvod):
    print(name, i, s)
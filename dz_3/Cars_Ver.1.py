#coding: utf-8
import pickle
import os


d = {}
data = {}
a = 0
i = 0
#Ввод данных

print("Input car and it's power. To exit input 'x': \n")

while True:
    
    a = input('Введите марку машины: ')
    a = a.replace(' ', '')
    a = a.lower()
    if a == 'x':
        break
    elif a.isalpha() == False:
            print('Название машины может содержать только буквы, попробуйте снова: ')
            continue
    
    b = input ('Введите мощность двигателя: ')
    if b.isnumeric() == False:
        print('Номер машины может содержать только цифры, попробуйте снова: ')
        continue
    
    d = dict.fromkeys([a], b)
    data.update(d)

f = open('c:/py3/db/cars.txt', 'wb')
pickle.dump(data, f)
f.close()

#Сортировка и вывод

cars = list(data)
cars.sort()

for i in cars:
    print (i, ' - ', data[i], end = '\n')

#Поиск

type_of_searching = int(input("For searching by name input 1\nFor searching by power input 2 \n"))


if type_of_searching == 1:

    search_by_name = int(input("For searching by the whole name input 1\nFor searching by the part of name input 2\n"))

    if search_by_name == 1:
                               
        a = input('Введите марку автомобиля: ')
        a = a.strip()
                               
        if a in data.keys():
            print(a, data[a])
        else:
            print('There is no such machines')


    if search_by_name == 2:
                               
        a = (input('Введите марку автомобиля: '))
        a = a.strip()
                               
        for i in data.keys():
            if a in i:
                print(i, data[i])
    
  

if type_of_searching == 2:

       
    search_by_power = int(input("For searching from lower input 1\nFor serching from higher input 2\nFor searchin from lower to higher input 3 \n"))

    if search_by_power == 1:

        power = input('Input power: ')

        for i in x:
            if data[i] > power:
                print('Cars: ' + i, data[i])


    if search_by_power == 2:
       
        power = int(input('Input power: '))

        for i in x:
            i = str(i)
            i = i.replace('(', '').replace(')', '').replace("'", "")
            a, b = i.split(',')
            b = int(b)
            if b < power:
               print('Cars: ' + a, b)


    if search_by_power == 3:
          
        power_lower = int(input('Input power: '))
        power_higher = int(input('Input power: '))
       
        for i in x:
            i = str(i)
            i = i.replace('(', '').replace(')', '').replace("'", "")
            a, b = i.split(',')
            b = int(b)
            if power_lower < b < power_higher:
                print('Cars: ' + a, b)






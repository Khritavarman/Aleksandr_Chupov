import math

a = open('c:/py3/numbers.txt')    
b = a.readlines()                 

arr = []                          

for i in b:                       
    arr.append(float(i))

sum_12 = arr[0] + arr[1]
print('Сумма первой пары чисел = ' + str(sum_12))

sqrt_34 = round (math.sqrt(arr[2] * arr[3]), 2)
print('Корень из произведения второй пары чисел = ' + str(sqrt_34))

c = max(sum_12, sqrt_34)
print('Максимальное из полученный чисел - ' + str(c))

d = round(math.cos(c), 3)
print('Косинус этого числа =  ' + str(d))


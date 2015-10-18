#1

students = [
    'Irina Yakovleva',
    'Svetlana Ivanova',
    'Irina Anufrieva',
    'Aleksandr Aleksandrov',
    'Elena Kuznetsova',
    'Aleksej Alekseev',
    'Aleksandr Ivanov'
]

#2

l = len(students)

i = int(input('Введите номер студента (не больше ' + str(l-1)+ '): '))
print(students[i] + '\n')


#3

c = int(input('Введите номер первого студента (не больше ' + str(l-1)+ '): '))
d = int(input('Введите номер последнего студента (не больше ' + str(l-1)+ '): '))
print(students[c:d+1])


#4
names = []

for i in students:
    name = i.split()[0]
    names.append(name)


i = 0

print("\nБуква 'r' встречается в следующих именах: ")

for a in names:
    if a.count('r') > 0:
        print (students[i])
    i += 1

#5
    
same_names = []
names_1 = []
print('\nСписки одинаковых имен: ')

for a in names:
    if names.count(a) > 1:
        if a not in names_1:
            names_1.append(a)
            same_names.append([a])
        else:
            same_names[ names_1.index(a) ].append(a)

for b in same_names:
    print (b)

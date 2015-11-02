import db

#Функция вывода на экран результатов работы первой части программы

def func_output(data, path):

    data = db.pickle_load(path)

    cars = list(data)
    cars.sort()

    for i in cars:
        a = print(i, ' - ' , data[i], end = ', ')
    return data

#Функция вывода на экран результатов работы второй части программы
def new_func_output(new_data, new_path):

    new_data = db.new_pickle_load(new_path)

    print(new_data)
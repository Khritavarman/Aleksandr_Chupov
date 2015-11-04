#coding: utf-8

#Вводим путь сохранения базы данных
import db
import debug


#Задаем путь к базе данных
def db_path():
    path = input('Ведите путь сохранения и название базы данных: ')
    return path

# Создаем меню
def main_menu():
    menu_item = input('''\n Чтобы ввести данные, нажмите 1\n Чтобы увидеть список автомобилей, нажмите 2\n Для поиска в базе по имени, нажмите 3
 Для поиска в базе по мощности, нажмите 4\n Для редактирования базы введите 5\n Для выхода введите 0\n''')
    return menu_item

#Поиск по имени
def search_by_name(data, path):

    data = db.pickle_load(path)

    try:
    
        search_by_name = int(input("Для поиска по имени целиком введите 1\nДля поиска по части имени введите 2\n"))



        if search_by_name == 1:
    
            a = input('Введите марку автомобиля: ')
            a = a.strip()
            if a in data:
                print ('\nНайдены следующие машины: ')
                s = '{} (мощность - {})'
                print(s.format(a, data[a]))

    
        if search_by_name == 2:
    
            i = input('Введите часть названия: ')
            i = i.strip()
            for a in data:
                if i in a:
                    print ('\nНайдены следующие машины: ')
                    s = '{} (мощность - {})'
                    print(s.format(a, data[a]))

    except ValueError:
        print ('Введено неверное значение (используйте цифры 1 или 2)')

#Поиск по мощности
def search_by_power(data, path):

    data = db.pickle_load(path)

    try:

        search_by_power = int(input("Для поиска по одному значению мощности введите 1\nДля поиска в промежутке между двумя значениями нажмите 2\n"))
    
        if search_by_power == 1:
    
            power = int(input('Введите значение мощности: '))
    
            lst = []
            lst_lower = []
            lst_higher = []
    
            for i in data:
                data[i] = int(data[i])
                if data[i] == power:
                    lst.append([i, data [i]])
                elif data[i] < power:
                    lst_lower.append([i, data [i]])
                elif data[i] > power:
                    lst_higher.append([i, data [i]])
    
            print('Автомобили с мощностью равной введенной:', lst)
            print('Автомобили с мощностью меньше введенной:', lst_lower)
            print('Автомобили с мощностью выше введенной:', lst_higher)
    
        if search_by_power == 2:
    
            lst_low_up = []
    
            power_lower = int(input('Введите нижнее значение мощности: '))
            power_higher = int(input('Введите верхнее значение мощности: '))
    
            for i in data:
                if power_lower <= int( data[i] ) <= power_higher:
                    lst_low_up.append([i, data[i]])
            if lst_low_up != []:
                s = 'В промежутке между {} и {} находятся следующие машины: \n'
                print(s.format(power_lower, power_higher), lst_low_up)
            else:
                print('В заданном промежутке нет ни одной машины')	

    except ValueError:
        print ('Введено неверное значение (используйте цифры 1 или 2)')


# Редактирование элементов
def edit_elements(data, path):

    data = db.pickle_load(path)

    action = input('\nЧтобы редактировать данные, введите 1\nЧтобы удалить автомобиль, нажмите 2\n')

    if action == '1':
        r = input('Введите название автомобиля, который хотите отредактировать: \n')
        for i in data:
            if r == i:
                data.pop(r)
                new_car = input('Введите новое название: ')
                new_power = input('Введите мощность: ')
                data [new_car] = new_power
                break

    if action == '2':
        r = input('Введите название автомобиля, который хотите удалить: \n')
        for i in data:
            if r == i:
                data.pop(r)
                break

    db.pickle_save(data, path)

#Главная программа
def main_prog(path, menu_item):
    

    data = db.pickle_load(path)
    while menu_item != '0':
        if menu_item == '1':
            db.data_input(data, path)
        elif menu_item == '2':
            debug.func_output(data, path)
        elif menu_item == '3':
            search_by_name(data, path)
        elif menu_item == '4':
            search_by_power(data, path)
        elif menu_item == '5':
            edit_elements(data, path)
        menu_item = main_menu()


main_prog(db_path(), main_menu())




#-----------------------------------------------------------------------
#                                     Вторая часть программы
# Создаем меню
def new_main_menu():
    new_menu_item = input('''\n Чтобы ввести новые данные, нажмите 1\n Чтобы увидеть список автомобилей, нажмите 2
 Для изменения координат машины нажмите 3\n Для выхода введите 0\n''')
    return new_menu_item

# Задаем путь к новому словарю
def new_db_path():
    new_path = input('Ведите путь сохранения новой базы данных: ')
    return new_path

#Главная программа для работы с обновленными данными

def new_main_prog(path, new_path, new_menu_item):

    data = db.pickle_load(path)
    new_data = db.new_pickle_load(new_path)
    while new_menu_item != '0':
        if new_menu_item == '1':
            db.create_new_data(data, path, new_path, new_data)
        elif new_menu_item == '2':
            debug.new_func_output(new_data, new_path)
        elif new_menu_item == '3':
            db.car_move(new_data, new_path)
        new_menu_item = new_main_menu()


new_main_prog(db_path(), new_db_path(), new_main_menu())

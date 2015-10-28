#Первая часть программы

# Сохраняем данные в файл 
def pickle_save(data, path):

	import pickle
	f = open(path, 'wb')
	pickle.dump(data,f)
	f.close

# Загружаем данные из файла
def pickle_load(path):
	
	import pickle
	try:
		f = open(path, 'rb')
		data = pickle.load(f)
	except EOFError:
		data = {}
	return data

#Вводим данные
def data_input(data, path):


	while True:	

		car_model = input('Введите марку машины: ')
		car_model.replace(' ','').lower()		
		if car_model == 'x':
			break

		elif car_model.isalpha() == False:
			print('Название машины может состоять только из букв, попробуйте еще раз: ')
			continue		
		car_power = input('Введите мощность двигателя: ')
		if car_power.isnumeric() == False:
			print('Значение мощности двигателя может состоять только из цифр, попробуйте еще раз: ')
			continue		

		data [car_model] = car_power

		pickle_save(data, path)

#--------------------------------- 
#Вторая часть программы (добавление координат)

# Сохраняем новые данные в файл
def new_pickle_save(new_data, new_path):

	import pickle
	f = open(new_path, 'wb')
	pickle.dump(new_data,f)
	f.close

# Загружаем новые данные из файла
def new_pickle_load(new_path):
	
	import pickle
	try:
		f = open(new_path, 'rb')
		new_data = pickle.load(f)
	except EOFError:
		data = {}
	return new_data

# Изменение словаря, добавление значений координат и пробега
def create_new_data(data, path, new_path, new_data):

	new_data = new_pickle_load(new_path)

	for i in data:
		if i.replace(' ','').isalpha() == True:
			print('\n', i)
			p = input('\nДля того, чтобы редактировать данные об автомобиле, нажмите 1\nЧтобы пропустить редактирование, нажмите любую клавишу\n')

			if p == '1':
				number = input('Введите номер: ')
				coorX = float(input('введите координату X: '))
				coorY = float(input('введите координату Y: '))
				dist = float(input('Введите величину пробега: '))
				new_data [number] = [i, coorX, coorY, dist]
			else: continue

	new_pickle_save(new_data, new_path)

# Перемещение в другие координаты
def car_move(new_data, new_path):

	import math
	new_data = new_pickle_load(new_path)
	
	car_to_edit = input('Введите номер автомобиля, который хотите отредактировать: \n')
	
	for i in new_data:
		if car_to_edit == i:
			coorX = float(input ('Введите новую координату Х: '))
			coorY = float(input ('Введите новую координату У: '))
			delta1 = abs(coorX - float(new_data[i][1]))
			delta2 = abs(coorY - float(new_data[i][2]))
			new_data[i][1] = coorX
			new_data[i][2] = coorY
			new_data[i][3] = float(new_data[i][3]) + round(math.sqrt(delta1 ** 2 + delta2 ** 2), 2)
	
	new_pickle_save(new_data, new_path)
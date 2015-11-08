i = 1
cars = []
car_status = []

count_tanks = 0
count_cars = 0
count_carts = 0


class Tank:

    def status(self):
        self.model = input('Введите модель танка: ')
        self.chasis = input("Имеется ли у танка шасси (ответьте 'есть' или 'отсутствуют'): ")
        self.gus = int(input('Введите количество гусениц: '))

        if self.chasis != 'есть' or self.gus != 2:
            self.speed = 0
            s = 'Танк: модель - {}, шасси - {} , количество гусениц - {}, Танк движется со скоростью - {}'
            a = s.format(self.model, self.chasis, self.gus, self.speed) 

        else:
            self.speed = int(input('Введите значение сокрости: '))
            s = 'Танк: модель - {}, шасси - {} , количество гусениц - {}, Танк движется со скоростью - {}'
            a = s.format(self.model, self.chasis, self.gus, self.speed)

        return a


    
class Car:

    def status(self):
        self.model = input('Введите модель машины: ')
        self.wheels = int(input("Сколько у машины колес: "))

        if self.wheels == 3:
            self.speed = 'Машина едет, но оочень осторожно'
            s = 'Машина: модель - {}, количество колес - {}, {}'
            a = s.format(self.model, self.wheels, self.speed)

        elif self.wheels !=3 and self.wheels != 4:
            self.speed = 'Машина стоит, т.к. у нее беда с колесами'
            s = 'Машина: модель - {}, количество колес - {}, {}'
            a = s.format(self.model, self.wheels, self.speed)

        else:
            self.speed = int(input('Введите значение сокрости: '))
            s = 'Машина: модель - {}, количество колес - {}, машина движется со скоростью - {}'
            a = s.format(self.model, self.wheels, self.speed)

        return a


class Cart:

    def status(self):
        self.horses = int(input('Сколько коней тянут телегу: '))
        self.wheels = int(input("Сколько у телеги колес: "))

        if self.horses < 1:
            self.speed = 'Телегу некому тащить'
            s = 'Телега: количество лошадей - {}, количество колес - {}, {}'
            a = s.format(self.horses, self.wheels, self.speed)

        else:
            if self.wheels == 3:
                self.speed = 'Телега едет, но оочень осторожно'
                s = 'Телега: количество лошадей - {}, количество колес - {}, {}'
                a = s.format(self.horses, self.wheels, self.speed)

            elif self.wheels < 3:
                self.speed = 'Телега едет, но лошадям очень тяжело'
                s = 'Телега: количество лошадей - {}, количество колес - {}, {}'
                a = s.format(self.horses, self.wheels, self.speed)

            else:
                self.speed = int(input('Введите значение сокрости: '))
                s = 'Телега: количество лошадей {}, количество колес - {}, телега движется со скоростью - {}'
                a = s.format(self.horses, self.wheels, self.speed)

        return a


while i!=0:

    print('\nЗаполняем список транспортных средств: ') 

    i = int(input("\nЧтобы добавить танк введите 1\nЧтобы добавить машину нажмите 2\nЧтобы добавить телегу нажмите 3\nЧтобы перейти к списку нажмите 0: "))
    
    if i == 1:

        tank = Tank()
        cars.append(tank)

        count_tanks += 1
        g = ('В списке танков - {}, машин - {}, телег - {}')
        print(g.format(count_tanks, count_cars, count_carts))

        continue

    if i == 2:

        car = Car()
        cars.append(car)

        count_cars += 1
        g = ('В списке танков - {}, машин - {}, телег - {}')
        print(g.format(count_tanks, count_cars, count_carts))

        continue

    if i == 3:
         
        cart = Cart()
        cars.append(cart)

        count_carts += 1
        g = ('В списке танков - {}, машин - {}, телег - {}')
        print(g.format(count_tanks, count_cars, count_carts))

        continue


for i in cars:
    car_status.append(i.status())

for object_status in car_status:
    print(object_status)
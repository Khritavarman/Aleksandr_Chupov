#coding: utf-8

from random import randint

class Animal:
 
    def __init__(self, year, name):

        self.year = year
        self.name = name

    def voice(self, sound, sound_number):     # Команда "Голос", сколько раз за день
        print (self.name, "сказал", sound, sound_number, "раз")
        
    def run(self, speed, time):    # Скорость бега (км/ч) и время (мин)
        dist = speed*(time/60)
        return dist

    def produce (self, product, product_quantity):    # Производить продукт со скоростью в день, выводит сколько было произведено за день
        print (self.name, "произведено", product_quantity, product)
        

class Duck(Animal):
    

    sound = 'Ква'
    speed = 2
    product = 'Яйца'
    
    def one_mounth(self):
        self.product_quantity = randint(20,40)
        self.sound_number = randint(100,1000)
        self.running = self.run(randint(15,25),randint (100, 200))
        self.death = randint (1,690)

class Cow(Animal):

    sound = 'Шазуу'
    speed = 5
    product = 'Молоко'
 
    def one_mounth(self):
        self.product_quantity = randint(350,500)
        self.sound_number = randint(500,1500)
        self.running = self.run(randint(15,25),randint (100, 200))
        self.death = randint (1,700)

class Dog(Animal):

    sound = 'АРРГХ!!!'
    speed = 35
    prodact = 'Съеденные воры'
    
    def one_mounth(self):
        self.product_quantity = randint(1,2)
        self.sound_number = randint(400,1000)
        self.running = self.run(randint(25,35),randint (100, 500))



class Farm:    
    
    def __init__(self, ducks, cows, dogs):    # Вводим количество уток, коров и собак

        self.ducks_lst = []      # Создаем список экземпляров классов: Duck, Cow, Dog
        for i in range(1,ducks+1):
            self.ducks_lst.append(Duck(year=randint(1,10), name="duck"+str(i)))   
                
        self.cows_lst = []
        for i in range(1,cows+1):
            self.cows_lst.append(Cow(year=randint(1,30), name="cow"+str(i)))
            
        self.dogs_lst = []
        for i in range(1, dogs+1):
            self.dogs_lst.append(Dog(year=randint(1,20), name="dog"+str(i)))


    def one_mounth(self):    # Прошел месяц на ферме
        for duck in self.ducks_lst:
            duck.one_mounth()
        for cow in self.cows_lst:
            cow.one_mounth()
        for dog in self.dogs_lst:
            dog.one_mounth()

    def information(self):    # Информация о ферме
       
        milk_count, shazoo_count, cow_run = 0, 0, 0  # Для коров
        death_cow = []

        for cow in self.cows_lst:
            if cow.death == 246:
                death_cow.append(cow.name)
                del cow
            else:
                milk_count += cow.product_quantity
                shazoo_count += cow.sound_number
                cow_run += cow.running
                print (cow.name, "произвела", cow.product_quantity, "литров молока, прощебетала", cow.sound_number, "раз и проскакала", round(cow.running), "км")
        if len(death_cow)>0:
            print ("Коровы", ','.join(death_cow), "покинули этот мир")
        print("#############################################################################################")      
        
        
        egg_count, kwa_count, duck_run = 0, 0, 0    # Для уток
        death_duck = []

        for duck in self.ducks_lst:
            if duck.death == 415:
                death_duck.append(c.name)
                del duck
            else:
                egg_count += duck.product_quantity
                kwa_count += duck.sound_number
                duck_run += duck.running
                print (duck.name ,"снесла", duck.product_quantity, "яиц, проквакала", duck.sound_number, "раз и проползла", round(duck.running), "км")
        if len (death_duck)>0:
            print ("Утки", ','.join(death_duck), "покинули этот мир")
        print("#############################################################################################")

        
        arrrhg_count, dog_run, thieves_count = 0, 0, 0    # Для собак

        for dog in self.dogs_lst:
            thieves_count += dog.product_quantity
            arrrhg_count += dog.sound_number
            dog_run += dog.running

            print (dog.name, "съела", dog.product_quantity, "воров, пролаяла", dog.sound_number, "раз и прошла", round(dog.running), "км")
        print("#############################################################################################")


        print ("Коровы произвели", milk_count, "литров молока, прощебетали", shazoo_count, "раз и проскакали", round(cow_run), "км")
        print ("Утки снесли", egg_count, "яиц, проквакали", kwa_count, "раз и проползли", round(duck_run), "км")
        print ("Собаки съели", thieves_count, "воров, пролаяли", arrrhg_count, "раз и прошли", round(dog_run), "км")
        
        
farm1 = Farm(20,15,5)
farm1.one_mounth()
farm1.information()

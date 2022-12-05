# Наследование
# Инкапсуляция
# Полимарфизм 

# Абстракция

# class Rectangle:
#     def __init__(self, x: int, y: int) -> None: 
#         self.x = x
#         self.y = y

#     def get_area(self):
#         return self.x * self.y  

#     def __str__(self) -> str:
#         return f"Это прямоугольник {self.x} * {self.y} = {self.get_area()}"

# class Square:
#     def __init__(self, x: int):
#         self.x = x

#     def get_area(self):
#         return self.x ** 2
    
#     def __str__(self) -> str:
#         return f"Это квадрат {self.x} ** 2 = {self.get_area()}"

# class Circle:
#     def __init__(self, r):
#         self.r = r
    
#     def get_area(self):
#         from math import pi
#         return pi * self.r**2

#     def __str__(self) -> str:
#         return f"Это Круг pi * {self.r} ** 2 = {self.get_area()}"



# r = Rectangle(160, 60)
# r1 = Rectangle(200, 140)
# s = Square(3)
# s1 = Square(5)
# c = Circle(50)
# c1 = Circle(25)


# list_obj = [r, r1, s, s1, c, c1]

# for i in list_obj:
#     print(i.get_area())







# @property


# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name    # Атрибут
#         self.age = age      # Атрибут
    
#     @property               # make attribut from method
#     def get_next_age(self): # Метод
#         return self.age + 1
    
#     @property
#     def full_name(self):
#         return self.name + ' ' + self.name


# p = Person('Marselle', 18) # Экземпляр или Объект
# print(p.full_name)

class Tomato:
    def __init__(self, index):
        self._index = index
        self.states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зелёный', 3: 'Красный'}
        self.i = 0
        self._state = self.states[self.i]

    def grow(self):
        self.i += 1
        self._state = self.states[self.i]
        print(self.info())

    def info(self):
        return f'{self._index} находится на стадии "{self._state}".'

    def is_ripe(self):
        if self.states[self.i] == self.states[3]:
            print(f'{self._index} достиг последней стадии созревания.')
        else:
            print(f'{self._index} ещё не достиг последней стадии созревания.')



class TomatoBush:
    def __init__(self, *count):
        self.tomatoes = count

    def grow_all(self):
        print('grow all')
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        count = 0
        for i in self.tomatoes:
            if i._state == 'Красный':
                count += 1
        if count == len(self.tomatoes):
            return True
        return False

    def give_away_all(self):    # ВЫЗЫВАТЬ ТОЛЬКО ПОСЛЕ СБОРА УРОЖАЯ ! ! !
        if self.all_are_ripe():
            self.tomatoes = []
            print('Растение очищено от томатов.')
        print('Ошибка при очистке растения от томатов.')

    def knowledge_base(self):
        a = []
        for i in self.tomatoes:
            a.append(f'"{i._index}" сейчас на стадии "{i._state}"')
        print(', '.join(a) + '.')


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f'{self.name} собрал урожай🍅👨‍🌾🍅')
        else:
            print('Урожай не готов.⛔️')


    

# list_tomat = []
# for i in range(10):
#     list_tomat.append(Tomato(i))
t1 = Tomato(1)
t2 = Tomato(2)
t3 = Tomato(3)
t4 = Tomato(4)
t5 = Tomato(5)
t6 = Tomato(6)
    


tb = TomatoBush(t1, t2, t3, t4, t5, t6)


garden = Gardener('Ali', tb)
garden.work()
garden.work()
garden.harvest()
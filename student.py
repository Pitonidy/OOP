class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name

        self.lastname = lastname
        self. department = department
        self. year_of_entrance = year_of_entrance

    def get_student_info(self):
        return f'{self.name} {self.lastname} поступил в {self.year_of_entrance} г. на факультет: {self.department}'

a = Student('Вася', 'Иванов', 'Программирование', 2017)
print(a.get_student_info())

class Airplane:
    def __init__(self, make, model, year, max_speed):
        self.make = make #делать
        self.model = model
        self.year = year
        self.max_speed = max_speed #скорость
        self.odometr = 0 #километраж
        self.is_flying = False #летает

    def take_off(self): #взлет
        self.is_flying = True
        message_take = f'{self.make} {self.model} был взлёт'
        return message_take
    def fly(self, km): #летать
        self.odometr = km
        message_fly = f'{self.make} летал {self.odometr} km, скорость во время полета {self.max_speed} km/h'
        return message_fly
    def land(self): #на земле
        self.is_flying = False
        message_land = f'{self.make} высадилься, одоментр показывает {self.odometr}km'
        return message_land

samolet = Airplane('Airbus', 'A320neo', 2018, 1013)
print(samolet.take_off())
print(samolet.fly(100))
print(samolet.land())
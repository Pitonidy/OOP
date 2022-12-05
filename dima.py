#       1

# class Student:
#     def __init__(self, name, lastname, department, year_of_entrance):
#         self.name = name
#         self.lastname = lastname
#         self.department= department
#         self.year_of_entrance = year_of_entrance

#     def get_student_info(self):
#         print(f'{self.name} {self.lastname} поступил в {self.year_of_entrance} г. на факультет: {self.department}.')

# dima = Student('Дима', 'Тетрадьсмерти', 'ITC школа программирования - Python+Django', '2022')
# dima.get_student_info()



#       2

class Airplane:
    def __init__(self, mark, model, year, maxspeed, odometr, is_flying=False):
        self.mark = mark
        self.model = model
        self.year = year
        self.maxspeed = maxspeed
        self.odometr = odometr
        self.is_flying = is_flying

    def take_off(self):
        print(f'Самолёт {self.model} взлетел.')
        self.is_flying = True

    def is_fly(self):
        if self.is_flying == True:
            print(f'{self.model} сейчас в полёте.')
            return True
        else:
            print(f'{self.model} сейчас на земле.')
            return False

    def fly(self, distance, speed):
        time = distance / speed
        if speed > self.maxspeed or speed < 400:
            print('С такой скоростью наш самолёт не летает.')
            return False
        else:
            print(f'Мы пролетим расстояние {distance} километров со скоростью {speed} км/ч за {int(time)} часов. Приятного полёта.')
            self.odometr += distance
            print(f'Километраж самолёта теперь {self.odometr} км.')
            return True


jet = Airplane('Samolet', 'SuperJet4000', '2022', 600, 400)
jet.take_off()
jet.is_fly()
jet.fly(600, 270)
jet.fly(700, 460)
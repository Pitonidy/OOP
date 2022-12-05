class Student:
    def __init__(self, name, lastname,department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.departmant = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        return f"{self.name} {self.lastname} поступил в {self.year_of_entrance} на факультет {self.departmant}"

s = Student('Бектур', 'Беков', 'Програмирование', 2018 )

print(s.get_student_info())
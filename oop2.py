class Mebel:
    def __init__(self, title: str, area: int):
        self.title = title
        self.area = area

    def __str__(self):
        return f"{self.title} {self.area}"

class Home:
    def __init__(self, title: str, area: int, mebels: list):
        self.title = title
        self.area = area
        self.mebels = mebels

    def __str__(self):
        return f"{self.title} {self.area}, мебели: {self.get_mebels()}"
    
    def get_area(self):
        count = 0
        for mebel in self.mebels:
            count += mebel.area
        return self.area - count
    
    def get_mebels(self):
        mebel_names = []
        for mebel in self.mebels:
            mebel_names.append(mebel.title)
        return mebel_names




shkaf = Mebel('Shkaf', 4)
shkaf1 = Mebel('Shkaf из Тайланда', 4)
table = Mebel('Table', 5)
bad = Mebel('Bad', 3)


home1  = Home(title='Дом Султана', area=125, mebels=[shkaf, shkaf1, table, bad, bad])
home1  = Home(title='Дом Султана1', area=85, mebels=[ shkaf1, table, bad])
home3  = Home(title='Дом Султана2', area=70, mebels=[ shkaf1, table, bad, bad])

print(home1.mebels[0])
################################################################


from time import sleep
from random import choice

class Gun:
    def __init__(self, name: str, number_bullets: int):
        self.name = name
        self.number_bullets = number_bullets
        self.bullets = 0
    def __str__(self):
        return  self.name
        
    def change_mag(self):
        self.bullets = self.number_bullets
        print('Перезаряжаюсь, Прикой!')
        sleep(2)
        
    
    def shot(self):
        if self.bullets == 0:
            print('Нет потронов! change mag!')

        if self.bullets > 0:
            for i in range(1, self.bullets+1):
                print(f'{choice("🎯💥🗿")}  <--     -      -    -    🔫 ')
                sleep(1.5)
                if self.bullets == 1:
                    print('Магазин закончился!')
                
                self.bullets -= 1

class Soldier:
    def __init__(self, name: str, weapon: Gun, mag: int):
           self.name = name
           self.weapon = weapon
           self.mag = mag

    def atak(self):
        while self.mag != 0:
            self.weapon.change_mag()
            self.mag -= 1
            print('Готов к бою!')
            if self.mag == 0:
                print('Последний магазин!')
                sleep(1)
            self.weapon.shot()

            if self.mag == 0:
                print('Конец магазинам, Нам кырдык!')
        else:
            print(self.weapon)
            print('Нет магазинам, Нам кырдык!')

# ak47 = Gun('Ak47', 30)

# soldier = Soldier('ITCMEN', ak47, 1)
# soldier.atak()
# soldier.atak()
# soldier.atak()

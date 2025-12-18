"""Task 1"""

# 1. Matematik sinf bilan dastur yozing.
# Ikki atribut yarating - a va b.
# Yozish usullari
# qo'shish - qo'shish, ko'paytirish - ko'paytirish,
# bo'lish - bo'lish, ayirish - ayirish.
# a va b parametrlarini ular bilan usullarga o'tkazishda
# tegishli harakatni amalga oshirishingiz va javobni chop etishingiz kerak.

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def minus(self):
        print(self.a - self.b)

    def multiply(self):
        print(self.a * self.b)

    def divide(self):
        print(self.a / self.b)


operation = Calculator(23, 31)

operation.divide()

"""Task 2"""

# 2. Quyidagi argumentlarni oladigan kompyuter sinfini yarating:
# egasi, protsessor, operatsion tizim, xotira, xotira, monitor.
# Klassning satrli tasviri uchun metodni yozing.Bu formatda kompyuter
# egasi nomini qaytaradigan usul yarating. : usulini oʻzingiz qiling.
# Keyin sinf yaratilganda usulni avtomatik ishga tushiring. Ikki sinfni
# operativ xotirasi boʻyicha solishtiradigan usullarni yarating.

class Computer:
    def __init__(self, owner, processor, os, ram, rom, monitor):
        self.owner = owner
        self.processor = processor
        self.os = os
        self.ram = ram
        self.rom = rom
        self.monitor = monitor

    def get_owner(self):
        print(f"Kompyuter egasi: {self.owner}")

    def get_info(self):
        print(f"{self.owner}ning kompyuteri\n"
              f"{self.processor} prosessoriga ega,\n"
              f"{self.os} tizimida ishlaydi,\n"
              f"tezkor xotirasi {self.ram} GB,\n"
              f"doimiy xotirasi esa {self.rom} GB hamda\n"
              f"{self.monitor} monitor bilan jihozlangan")

    def compare(self, owner1, processor1, os1, ram1, rom1, monitor1):
        self.ow1 = owner1
        self.prss1 = processor1
        self.os1 = os1
        self.ram1 = ram1
        self.rom1 = rom1
        self.monitor1 = monitor1

        if self.ram > self.ram1:
            print(f"Sizning kompyuteringizning tezkor xotirasi {self.ow1}ning \nkompyuteri tezkor xotirasidan kata "
                  f"ekan")
        elif self.ram1 == self.ram:
            print("Ikkala kompyuterning tezkor xotirasi bir xil")
        else:
            print(f"{self.ow1}ning kompyuteri tezkor xotirasi sizning \nkompyuteringizning tezkor xotirasidan kata "
                  f"ekan")


comp = Computer("Doston", "Rayzen 7 7000 series", "Windos 11", 16, 512, "oled")
comp.compare("Vali", "Rayzen 7 7000 series", "Windos 11", 8, 512, "oled")

"""Task 3"""

# 3. Uchta atributga ega bo'lgan talabalar sinfi bilan dastur yozing: ism,
# guruh raqami va yosh. Odatiy ism = Ivan, yosh = 18, groupNumber = 10A.
# Siz beshta usul yaratishingiz kerak: getName, getAge, getGroupNumber,
# setNameAge, setGroupNumber. getName usuli ma'lum bir talabaning nomi haqida
# ma'lumot olish uchun kerak, getAge usuli ma'lum bir talabaning yoshi haqida ma'lumot
# olish uchun kerak, setGroupNumber usuli aniq talabaning guruh raqami haqida ma'lumot olish
# uchun kerak. SetNameAge usuli standart atribut ma'lumotlarini o'zgartirishga imkon beradi,
# setGroupNumber usuli standart guruh raqamini o'zgartirishga imkon beradi. Dastur talabalar sinfining
# beshta nusxasini yaratishi, ularga turli nomlar, yosh va guruh raqamlarini belgilashi kerak.

class Student:
    def __init__(self, name, age, group_number):
        self.name = name
        self.age = age
        self.gn = group_number

    def get_name(self):
        print(f"Talabaning ismi: {self.name}")

    def get_age(self):
        print(f"Talaba {self.age} yoshda")

    def get_group(self):
        print(f"Siz kiritgan talaba {self.gn} guruhda o'qiydi")

    def set_name_age(self, name1, age1):
        self.name1 = name1
        self.age1 = age1
        print(f"Talabaning ismi {self.name} dan {self.name1}ga,\nyoshi {self.age} dan {self.age1} ga o'zgartirildi")

    def set_group_num(self, group_num):
        self.gr_n = group_num
        print(f"Guruh raqami {self.gn} dan {self.gr_n} ga o'zgartirildi")


talaba1 = Student("Doston", 20, 204)
talaba2 = Student("Shuhrat", 25, 323)
talaba3 = Student("Vali", 18, 234)
talaba4 = Student("Ali", 30, 456)
talaba5 = Student("Shox", 21, 304)

talaba1.get_name()
talaba2.get_age()
talaba3.get_group()
talaba4.set_name_age("Samandar", 26)
talaba5.set_group_num(404)

"""Task 4"""


class Animals:
    def __init__(self, animal, food, place):
        self.animal = animal
        self.food = food
        self.place = place

    def qushlar(self, wing_length, color):
        self.wing_length = wing_length
        self.color = color
        print(f"{self.animal} {self.color} rangda bo'lib {self.place}da uchraydi,\n"
              f"qanotini yozganda uzunligi {self.wing_length} m bo'ladi,\n"
              f"asosan {self.food} bilan ozuqlanadi")

    def sut_emizuvchilar(self, size, color):
        self.size = size
        self.color = color
        print(f"{self.animal} {self.color} rangda bo'lib {self.place} da uchraydi,\n"
              f"balandligi {self.size} m bo'ladi,\n"
              f"asosan {self.food} bilan ozuqlanadi")

    def reptilyalar(self, size1):
        self.size1 = size1
        print(f"{self.animal} {self.place} da uchraydi,\n"
              f"uzunligi {self.size1} m bo'ladi,\n"
              f"asosan {self.food} bilan oziqlanadi")

    def baliqlar(self, color2):
        self.color2 = color2
        print(f"{self.animal} balig'i {self.color2} rangda bo'lib {self.place} da uchraydi,\n"
              f"asosan {self.food} bilan ozuqlanadi")


qush1 = Animals("Burgut", "mayda jonzotlar", "tog'li hududlar")
qush1.qushlar(2, "jigarrqng")
qush1 = Animals("Tovuq", "don", "insonlar uylarida")
qush1.qushlar(0.2, "har xil")

sut_emizuvchi1 = Animals("Kalamush", "topgan narsasi", "odamlar kam joy")
sut_emizuvchi1.sut_emizuvchilar(0.1, "har xil")
sut_emizuvchi2 = Animals("Maymun", "o'simliklar", "Brazilya o'rmonlari")
sut_emizuvchi2.sut_emizuvchilar(1, "har xil")

reptilya1 = Animals("Ilon", "mayda jonzotlar", "tashlandiq joylar hamda o'rmonlar")
reptilya1.reptilyalar(1)
reptilya2 = Animals("Hamilyon", "hasharotlar", "Brazilya o'rmonlari")
reptilya2.reptilyalar(0.25)

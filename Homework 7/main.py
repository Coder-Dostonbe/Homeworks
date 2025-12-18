"""Task 1"""
# 1. Eng katta qiymatni toping
# ballar = {"Ali": 56, "Vali": 78, "Sami": 90, "Diyor": 66}
# Vazifa:
# Eng yuqori ball to‘plagan o‘quvchining ismi va ballini chiqaruvchi kod yozing.

ballar = {
    "Ali": 56,
    "Vali": 78,
    "Sami": 90,
    "Diyor": 66
}

for key, value in ballar.items():
    if value == max(ballar.values()):
        print(key, "-", value)

"""Task 2"""
#  2. Lug‘atdan faqat juft qiymatlarni ajrating
# sonlar = {"a": 11, "b": 20, "c": 7, "d": 42}
# Vazifa:
# Qiymati juft bo‘lgan elementlarni new_dict ga saqlang.
# Natija:
# {'b': 20, 'd': 42}

sonlar = {"a": 11, "b": 20, "c": 7, "d": 42}
juft_raqamlar = {}

for key, value in sonlar.items():
    if value % 2 == 0:
        juft_raqamlar[key] = value
print(juft_raqamlar)

"""Task 3"""
# 3. Ikki dict ni birlashtiring (qiymatlar qo‘shiladi)
# a = {"olma": 5, "uzum": 3}
# b = {"olma": 4, "nok": 7}
# Vazifa:
# Agar kalitlar bir xil bo‘lsa — qiymatlari qo‘shilsin. Yangi dict yarating.
# Natija:
# {'olma': 9, 'uzum': 3, 'nok': 7}

a = {"olma": 5, "uzum": 3}
b = {"olma": 4, "nok": 7}
c = {}
for key, value in a.items():
    c[key] = value
for key, value in b.items():
    if key in c:
        c[key] += value
    else:
        c[key] = value
print(c)

"""Task 4"""
# 4. Talabalar ro‘yxatidan faqat 18 yoshdan kattalarni chiqaring
# talabalar = {
#    "Ali": 17,
#    "Vali": 19,
#    "Sami": 21,
#    "Diyor": 16
# }
# Vazifa:
# 18 yoshdan katta bo‘lganlarni ekranga chiqaring.
# Natija:
# Vali - 19
# Sami - 21

talabalar = {
   "Ali": 17,
   "Vali": 19,
   "Sami": 21,
   "Diyor": 16
}

for key, value in talabalar.items():
    if value > 18:
        print(key, "-", value)

"""Task 5"""
# 5. Matndagi har bir harf uchrash sonini sanang
# matn = "assaalom"
# Vazifa:
# Har bir harf nechta marta qatnashganini dict ko‘rinishida hisoblang.
# Natija:
# {'a': 3, 's': 2, 'l': 1, 'o': 1, 'm': 1}

matn = "assaalom"

c = {}

for item in matn:
    if item in c:
        c[item] += 1
    else:
        c[item] = 1

print(c)
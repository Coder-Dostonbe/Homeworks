"""Task 1"""
# 1.Siz foydalanuvchidan uning ismi, familiyasi, yoshini qabul qilasiz.
# Ularni tegishli o'zgaruvchilarga saqlang. Olingan qiymatlarni ro'yxatga saqlang.

infos = []

name = infos.append(input("Ismingizni kiriting: "))
last_name = infos.append(input("Familyangizni kiriting: "))
age = infos.append(input("Yoshingizni kiriting: "))
print(infos)

"""Task 2"""
# 2.Foydalanuvchidan vergul va bo'sh joy bilan ajratilgan raqamlar ketma-ketligini
# qabul qiluvchi dastur tuzing. Keyin har bir raqamni ro'yxat va kortejga yozing.

numbers1 = input("Istalgancha raqamlarni vergul yoki bo'sh joy bilan kiriting: ").split()
numbers2 = tuple(numbers1)
print(numbers1)
print(numbers2)

"""Task 3"""
# Bitta input() funksiya chaqiruvida foydalanuvchidan kirish sifatida uchta nom oladigan dastur yozing.
# Foydalanuvchidan bo'sh joy bilan ajratilgan uchta nomni kiritishini so'rang
# Uchta alohida nom olish uchun split() funksiyasidan foydalanib kirish qatorini bo'sh joyga ajrating.

any_info = input("Istalgan 3 ta so'zni bir biridan ajratib kiriting: ").split(" ")
print(any_info)

"""Task 4"""
# 4.*Foydalanuvchidan harf bahosini (A+, A, A- va hokazo) qabul qiladigan va ro‘yxatingizda shunday
# baho borligini tekshiradigan dastur yozing [A+,..., F]. Agar mavjud bo'lsa, dastur True, aks holda
# False chiqishi kerak.

grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
grade =  input("Bahoyingizni harfda kiriting misol(A+...): ")
if grade in grades:
    print("True")
else:
    print("False")

"""Task 5"""
# **Foydalanuvchidan so'zlar ketma-ketligini qabul qiladigan dastur yozing. Satrni ro'yxatga aylantiring.
# Python so'zining so'zlar ro'yxatida mavjudligini tekshiring, agar mavjud bo'lsa, uni ro'yxatdan olib
# tashlang va ro'yxatni chiqaring. Agar u mavjud bo'lmasa, uni nol holatidagi ro'yxatga qo'shing va ro'yxatni
# chiqaring.

words = input("Istalan so'zlarni bir biridan ajratib kiriting: ").lower().split(" ")
for_python = []
if "python" in words:
    words.remove("python")
    print(words)
else:
    for_python.append("python")
    print(for_python)
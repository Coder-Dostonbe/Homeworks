"""Homework 2"""
"""Task 1"""
# 1. Dastur foydalanuvchidan yoshini so’rashi kerak:
#
#     a. Agar yoshi 18 dan kam yoki unga teng bo'lsa, u holda chiqish: "Siz o'qishingiz kerak."
#     b. Agar yoshi 18 dan katta bo'lsa, lekin 50 dan kam yoki unga teng bo'lsa - "Siz ishlashingiz kerak"
#     c. Agar yoshi 50 dan katta bo'lsa, lekin 59 dan kam yoki unga teng bo'lsa - "Siz yaqinda nafaqaga chiqasiz"
#     d. Agar yoshdan katta bo'lsa. 59, lekin 110 dan kam - "Siz pensionersiz".
#     e.Agar foydalanuvchi haqiqiy bo'lmagan yoshga kirsa, nima ko'rsatilishi kerakligini ham o'ylab ko'ring. Masalan, 1200.

age = int(input("Yoshingizni kiriting: "))
if 0 < age <= 18:
    print("Hozir siz bilim olishingiz kerak")
elif 18 < age <= 50:
    print("Siz ishlashingiz kerak")
elif 50 < age <= 110:
    print("Yashab bersayz bo'ldi")
elif age < 0:
    print("Hazillashmang bunaqa yosh yo'g'u")
elif age > 110:
    print("Dinazavr ekansizu😁")

"""Task 2"""
# 2. Foydalanuvchidan butun sonni qabul
# qiladigan 1 dan 12 gacha shu oyga mos oy nomi  va kunlar sonini qaytaradigan dastur yozing.

month_num = int(input("1 dan 12 gacha bo'lgan raqam kiriting: "))
if month_num == 1:
    print(f"{month_num}-oy Yanvar")
elif month_num == 2:
    print(f"{month_num}-oy Fevral")
elif month_num == 3:
    print(f"{month_num}-oy Mart")
elif month_num == 4:
    print(f"{month_num}-oy Aprel")
elif month_num == 5:
    print(f"{month_num}-oy May")
elif month_num == 6:
    print(f"{month_num}-oy Iyun")
elif month_num == 7:
    print(f"{month_num}-oy Iyul")
elif month_num == 8:
    print(f"{month_num}-oy Avgust")
elif month_num == 9:
    print(f"{month_num}-oy Sentabr")
elif month_num == 10:
    print(f"{month_num}-oy Oktabr")
elif month_num == 11:
    print(f"{month_num}-oy Noyabr")
elif month_num == 12:
    print(f"{month_num}-oy Dekabr")
else:
    print(f"Bir yilda 12 oy bor holos")

"""Task 3"""
# 3. Foydalanuvchidan uchta sonni so’raydigan va mos keluvchi sonlar sonini chiqaruvchi dasturni yozing.

num1 = int(input("1-raqamni kiriting: "))
num2 = int(input("2-raqamni kiriting: "))
num3 = int(input("3-raqamni kiriting: "))

if num1 == num2:
    print(f"Siz kritgan birinchi {num1} va ikkinchi {num2} bir biriga teng")
elif num1 == num3:
    print(f"Siz kritgan birinchi {num1} va uchinchi {num3} bir biriga teng")
elif num2 == num3:
    print(f"Siz kritgan birinchi ikkinchi {num2} va uchinchi {num3} bir biriga teng")
elif num1 == num2 == num3:
    print("Siz kiritgan barcha raqamlar bir biriga teng")
else:
    print(f"Siz kiritgan sonlardan hech biri bir biriga teng emas")

"""Task 4"""
# 4 *. Foydalanuvchidan ikkita son so’raydigan agar
# ulani ko’paytmasi 1000 dan katta bo’lmasa ko’paytmani aks holda ularni yig’indisini qaytaradigan dasturni yozing.

Num1 = int(input("Birinchi raqamni Kiriting: "))
Num2 = int(input("Ikkinchi raqamni Kiriting: "))
kopaytma = Num1 * Num2

if kopaytma < 1000:
    print(f"Siz ktirtgan raqamlar ko'paytmasi {kopaytma} ga teng")
else:
    print(f"Siz kiritgan sonlar yig'indisi {Num1+Num2} ga teng")

"""Task 5"""
# 5 *. Agar foydalanuvchi tergan son 5 ga
# qoldiqsiz bo’linsa “Hello” yozuvini konsolga chiqaradigan aks holda “Bye” yozuvini chiqaradigan dastur yozing.

son = int(input("Istalgan bitta sonni kiriting: "))

if son % 5 == 0:
    print("Hello")
else:
    print("Bye")

"""Task 6"""
# 6 **. Foydalanuvchidan yil terilishini so’raydigan yil kabisa ekanligini aniqlaydigan dasturni yozing.

year = int(input("Yilni kiriting: "))
if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
    print(f"{year} yil kabisa yili")
else:
    print(f"{year} yil kabisa yili emas")
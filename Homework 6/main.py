"""Task 1"""
#  1. Mahsulotlar ro'yxatini aniqlang, qidirish, tozalash, to'xtatish buyruqlarini qo'shing.

products = ["olma", "non", "cola", "o'rik sharbati", "tuxum", "go'sht"]

while True:
    user_input = input("Buyruqni hamda mahsulotni kiriting: ").lower()
    if user_input == "stop":
        print("Dastur to'xtadi!")
        break
    if len(user_input.split(" ")) == 2:
        command, product = user_input.split(" ")
        if command == "search":
            if product in products:
                print(f"{product} {products} ning ichida bor")
            else:
                print(f"{product} {products} ning ichida mavjut emas")

        if command == "clean":
            if product in products:
                print(f"Ro'yhat tozalab tashlandi")
                products.clear()
            else:
                print("Bunday ro'yhat mavjut emas!")

"""Task 2"""
#  2.“Narvon” muammosi. N ≤ 9 natural son berilgan bo‘lsa, n ta pog‘onadan narvon chiqaring,
#  i-chiqadam 1 dan i gacha bo'sh joysiz raqamlardan iborat.
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

num = int(input("Bitta raqam kiriting: "))
if num > 9:
    print("9 dan kichik raqam kiriting")
else:
    for i in range(1, num):
        for j in range(i):
            print(i, end=" ")
        print()

"""Task 3"""
# 3.Ikki musbat sonning eng katta umumiy boʻluvchisi ikkala sonni ham
# qoldiqsiz ajratuvchi eng katta sondir. Ikki sonning eng katta umumiy
# bo'luvchisini aniqlash uchun bir nechta algoritmlar mavjud, jumladan,
# quyidagilar. d o'zgaruvchini n va m dan kichiklari bilan boshlang
# n yoki m qoldiqsiz d ga bo'linmaguncha, bajaring
# d ni birga kamaytiring
# Chop etish d, bu n va m ning eng katta umumiy bo'luvchisidir
#
# Foydalanuvchidan ikkita musbat sonni so‘raydigan va ular uchun eng
# katta umumiy bo‘luvchini chop etadigan dastur tuzing.


n = int(input("Birinchi sonni kiriting: "))
m = int(input("Ikkinchi sonni kiriting: "))

d = min(m, n)

while True:
    if n % d == 0 and m % d == 0:
        break
    d -= 1
print(f"Siz kiritgan {n} va {m} ning EKUBi {d} ga teng")

"""Task 4"""
# 4. Bank dasturini yozing. Omonat miqdori va yillar sonini kiriting.
# Depozit muddati tugagunga qadar foydalanuvchi hisobiga qancha pul tushishini hisoblang.
# “Murakkab foizlar” tizimi yordamida muammoni hal qiling (foiz yangi summadan hisoblanadi)
# 10% ga teng yillik foizni ko'rib chiqing.

omonat_summasi = float(input("Omonatga qo'ymoqchi bo'lgan summangizni kiriting: "))
yil = int(input("Necha yilga omonat qo'ymoqchisiz: "))

foyda = omonat_summasi * (1 + 10 / 100) ** yil

print(f"Agar siz yiliga 10% lik depazit bilan omonat qo'ysangiz yiliga {round(foyda)} so'm foyda ko'rasiz")

"""Task 5"""
# 5. Ro‘yxatdagi faqat quyidagi shartlarga javob beradigan raqamlarni ko‘rsatish dasturini tuzing
# Raqam beshga bo'linishi kerak
# Agar raqam 150 dan katta bo'lsa, uni o'tkazib yuboring va keyingi raqamga o'ting.
# Agar raqam 500 dan katta bo'lsa, tsiklni to'xtating
# Umid qilamanki:
# raqamlar = [12, 75, 150, 180, 145, 525, 50]
# Kutilayotgan natija:
# 75
# 150
# 145

raqamlar = [12, 75, 150, 180, 145, 525, 50]
mos_raqamlar = []

for i in raqamlar:
    if i % 5 == 0:
        if i > 500:
            break
        elif i <= 150:
            mos_raqamlar.append(i)
        elif i > 150:
            pass
print(mos_raqamlar)

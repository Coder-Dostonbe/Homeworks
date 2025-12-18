"""Task 1"""
#  1. Bizda sonlardan iborat ro‘yxat bo‘ladi.
# Masalan: [10, 3, 55, 7, 88, 1, 42]
# Biz shularning eng kattasidan boshlab 3 tasini topmoqchimiz:
# 👉 88
# 👉 55
# 👉 42

def three_max_nums(nums):
    top = sorted(nums, reverse=True)[:3]
    print(top)

three_max_nums(nums = [10, 3, 55, 7, 88, 1, 42])

"""Task 2"""
# 2. Bizda sonlar bor:
# 8, 2, 3, 0, 7
# Shularni hammasini qo‘shib, bitta natija chiqarmoqchimiz.
# Buning uchun:
# 1.Avval jami = 0 deb olamiz.
# 2. Keyin ro‘yxatdagi har bir sonni olamiz.
# 3. Olingan sonni jamiga qo‘shamiz.
# Xuddi pul sanagandek: har birini qo‘shib boramiz.

def counter(num_collection):
    jami = 0
    for num in num_collection:
        jami += num
    print(jami)

counter(num_collection = [8, 2, 3, 0, 7])

"""Task 3"""
# 3. Biz ro‘yxatdagi sonlarni bir-biriga ko‘paytirib boramiz.
# Masalan:
# 8 × 2 × 3 × (−1) × 7 = −336
# Ko‘paytirishda boshlanish qiymati 1 bo‘ladi, chunki 0 dan boshlasak, hammasi 0 chiqib ketadi.

def kopaytir(num_list):
    result = 1
    for num in num_list:
        if num == 0:
            pass
        else:
            result *= num
    print(result)

kopaytir(num_list = [8, 2, 3, -1, 7])

"""Task 4"""
# 4. Satrni teskari aylantirish uchun Python dasturini yozing.
# Qator misoli: "1234abcd"
# Kutilayotgan natija: "dcba4321"

def reverser(text):
    result = text[::-1].lower()
    print(result)

reverser("1234abcd")

"""Task 5"""
# 5. Palindrom — oldindan ham, teskari o‘qiganda ham bir xil bo‘ladigan so‘z.
# So‘zni qabul qiladigan va uning palindrom ekanligini aniqlaydigan funksiya yozing. To'g'ri - Anna, kazak, kulba

def check_palindrome(word):
    if word == word[::-1]:
        print(f"Siz kiritgan so'z {word} palindrom!")
    else:
        print(f"{word} so'zi palindrom emas!")

recuest = input("So'z kiriting: ")
check_palindrome(recuest)

"""Task 6"""   """Task 7"""
# 6,7.  Foydalanuvchi yiliga 10% miqdorida "y" yil muddatga "x" rubl miqdorida depozit qo'yadi.
# Pul va yillar miqdorini oladigan va "y" yil ichida foydalanuvchi hisobiga tushadigan summani
# qaytaradigan bank funktsiyasini yozing.

def profit_counter(amount, years):
    profit = amount * (1+10/100) ** years
    print(f"{years} yillik tushum: {round(profit)}")

summa = int(input("Qancha summa omonat qo'ymoqchisiz: "))
yil = int(input("Qancha yilga omonat qo'ymoqchisiz: "))
profit_counter(summa, yil)

"""Task 8"""
# 8. Raqamning faktorialini hisoblash uchun Python funksiyasini yozing (manfiy bo'lmagan butun son).
# Funktsiya argument sifatida raqamni oladi.
# 5! = 1*2*3*4*5


def faktorial(number):
    x = 1
    for i in range(1, number +1 ):
        x *= i
    print(x)

f = int(input("Raqam kiriting: "))
faktorial(f)

"""Task 9"""
# 9. Satrni oladigan va katta va kichik harflar sonini hisoblaydigan Python funksiyasini yozing. isupper() islower()
# Misol qatori: "Tezkor tulki"
# Kutilayotgan natija:
# Katta harfdagi belgilar soni: 3
# Kichik harflar soni: 12

def checker(sentence):
    uppercase = 0
    lowercase = 0
    for piece in sentence:
        if piece.isupper():
            uppercase += 1
        elif piece.islower():
            lowercase += 1
    print(f"Katta harfdagi belgilar soni: {uppercase}")
    print(f"Kichik harfdagi belgilar soni: {lowercase}")


gap = input("Katta va kichik harflardan iborat gap kiriting: ")
checker(gap)

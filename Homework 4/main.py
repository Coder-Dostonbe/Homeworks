"""Task 1"""
# 1. a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] roʻyxati mavjud.
# Alohida ro'yxatda 5 dan kichik yoki unga teng va 5 dan katta raqamlarni chop eting.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

little = []
big = []

for i in a:
    if i <= 5:
        little.append(i)
    else:
        big.append(i)
print(little)
print(big)

"""Task 2"""
# Foydalanuvchidan ADD misolini qabul qiladigan dasturni yozing va natijani chop eting.

num = input("Istalgan raqamlarni bir biriga qo'shish misolini yozing: ").split(" ")
int_pack = []
trash = []

for i in num:
    if i == "+":
        trash.append(i)
    elif type(i) == str:
        int_pack.append(int(i))
print(sum(int_pack))

"""Task 3"""
# 3. Nikolay ro‘yxat asosida “foydasiz” raqam topish haqida o‘yladi. Buning mohiyati quyidagicha:
# u raqamlarning ixtiyoriy ro'yxatini oladi, ularning eng kattasini topadi va keyin uni ro'yxat
# uzunligiga bo'linadi. Talaba bunday qiymat qayerda foydali bo'lishi mumkinligini hali aniqlamadi,
# lekin bunday funktsiyani amalga oshirishda sizning yordamingizni kutmoqda

unimportant_numbers = input("Istalgancha raqam kiriting: ").split(" ")
for_int = []
for i in unimportant_numbers:
    i = int(i)
    for_int.append(i)
a = max(for_int)//len(for_int)

print(a)

"""Task 4"""
# 4. Oxirgi darsdagi muammoda biz to'g'ridan-to'g'ri va sonli hisob-kitoblar o'rtasidagi yozishmalar
# jadvalini yaratdik. Endi siz bo'sh joy bilan ajratilgan foydalanuvchi tomonidan kiritilgan harflar
# baholarining ixtiyoriy soni uchun o'rtacha bahoni hisoblashingiz kerak bo'ladi.
# Misol uchun, agar foydalanuvchi ketma-ket A, keyin C+ va keyin B, keyin bo'sh qatorni kiritsa, o'rtacha
# natija 3,1 bo'lishi kerak.
# Hech qanday xato tekshiruvi talab qilinmaydi. Keling, shunday da'vo qilaylik
# foydalanuvchi faqat haqiqiy baholarni yoki nolni kiritishi mumkin.

grades = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "D-": 0.7,
    "F": 0
}
for_count = []

grade = input("Harfdagi baholaringizni kiriting: ").title().split(" ")

for i in grade:
    if i in grades:
        for_count.append(grades[i])
    else:
        print(f"Siz kiritgan {i} baho mavjud emas!")

print(sum(for_count)/len(for_count))


"""Task 5"""
#  5. Raqamlar ro'yxati berilgan. ro‘yxatning har bir elementini kvadratiga aylantiruvchi dastur yozing.

nums = input("Istalgancha raqam kiriting: ").split(" ")
nums1 = []

for num in nums:
    if type(num) == str:
        num = int(num)
        nums1.append(num**2)
print(nums)

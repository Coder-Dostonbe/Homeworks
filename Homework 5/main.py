"""Task 1"""
# 1. Sevimli ovqatlaringiz ro‘yxatini tuzing.
# Ro‘yxatingizni nusxalab, do‘stingizning sevimli taomlari ro‘yxatini yarating.
# Har ikkala ro‘yxat bir-biridan farq qilishini ta’minlash uchun ularning har biriga
# bittadan qo‘shimcha taom qo‘shing.
# So‘ngra ikkala ro‘yxatni ekranga chiqaring.


my_favourite_foods = ["osh", "manti", "shashlik", "somsa", "chuchvara", "tandir"]
my_friend_favourite_foods = my_favourite_foods[:]
my_favourite_foods.append("norin")
my_friend_favourite_foods.append("non kabob")
print(my_favourite_foods)
print(my_friend_favourite_foods)

"""Task 2"""
# 2. Foydalanuvchidan raqam qabul qiladigan user_num o‘zgaruvchisini yarating.
# 1 dan user_num qiymatigacha (shu qiymatni ham qo‘shgan holda) bo‘lgan sonlardan iborat ro‘yxat yarating.
# Ro‘yxatning o‘zini va ro‘yxatdagi barcha sonlar yig‘indisini ekranga chiqaring.

num = int(input("Istalgan bitta raqam kiriting: "))
num_list = []
for i in range(1,num+1):
    num_list.append(i)
print(f"1 dan {num} gacha bo'lgan raqamlar ro'yhati: {num_list}")
print(f"1 da siz kiritgan {num} gacha bo'lgan raqamlar yig'indisi {sum(num_list)} ga teng")

"""Task 3"""
# 3.  1 dan 100 gacha bo‘lgan sonlardan ikkita alohida ro‘yxat yarating:
# - birinchi ro‘yxatda faqat juft sonlar bo‘lsin,
# - ikkinchi ro‘yxatda esa faqat toq sonlar bo‘lsin.
# Har bir ro‘yxatni va uning ichidagi sonlar yig‘indisini ekranga chiqaring.

even_numbers = []
odd_numbers = []

for i in range(0, 100, 2):
    even_numbers.append(i)
for w in range(1, 100, 2):
    odd_numbers.append(w)
print(f"Juft sonlar ro'yhati:\n {even_numbers}\n va ularning yig'indisi {sum(even_numbers)} ga teng")
print(f"Toq sonlar ro'yhati:\n {odd_numbers}\n va ularning yig'indisi {sum(odd_numbers)} ga teng")

"""Task 4"""
# 4. Vazifa:
# Berilgan sonlar ro‘yxati.
# Shu ro‘yxatdan faqat juft sonlarni tartibini buzmasdan chiqarishing kerak.
# Lekin ro‘yxatda 815 soni chiqsa — shu joyda to‘xtaysan, undan keyin son chiqarmaysan.
# raqamlar = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978,
#     328, 615, 953, 345, 399, 162, 758, 61, 215, 826, 248, 866,
#     950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892,
#     894, 767, 553, 81, 379, 81, 379, 8, 8, 958, 743, 527
# ]

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978,
    328, 615, 953, 345, 399, 162, 758, 61, 215, 826, 248, 866,
    950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892,
    894, 767, 553, 81, 379, 81, 379, 8, 8, 958, 743, 527
]

numbers1 = []

for i in numbers:
    if i % 2 == 0:
        numbers1.append(i)
    elif i == 815:
        print("Dastur 815 ga yetib kelgani sababli to'xtadi")
print(f"Juft sonlar ro'yhati: {numbers1}")



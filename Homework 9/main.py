"""Task 1"""
# 1. Vazifa:
# Berilgan roʻyxatdagi ismlarni bosh harfi katta bo‘lgan ko‘rinishga o‘tkazing.
# Buning uchun avval def yordamida oddiy funksiya yarating va uni map() bilan qo‘llang.
# Keyin aynan shu natijani lambda funksiyasi orqali ham bajaring.
# Berilgan roʻyxat:
# ismlar = ['alfred', 'tabita', 'uilyam', 'arla']

def word_capitalizer(word):
    capitalized = list(map(lambda x: x.capitalize(), word))
    return capitalized

ismlar = word_capitalizer(['alfred', 'tabita', 'uilyam', 'arla'])
print(ismlar)

ismlar1 = ['alfred', 'tabita', 'uilyam', 'arla']
word_capitalize1 = list(map(lambda word: word.capitalize(), ismlar1))
print(word_capitalize1)

"""Task 2"""
# 2. Vazifa:
#  Berilgan ballar roʻyxatidan 75 dan katta bo‘lgan baholarni ajratib oling.
# Buning uchun avval def yordamida funksiya yarating va uni filter() bilan ishlating.
# Keyin shu ishni lambda funksiyasi yordamida takrorlang.
# Berilgan roʻyxat:
# ballar = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def finder(nums):
    bigger = list(filter(lambda x: x>=75, nums))
    return bigger

ballar = finder([66, 90, 68, 59, 76, 60, 88, 74, 81, 65])
print(ballar)

ballar1 = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

result = list(filter(lambda p:  p> 75, ballar1))
print(result)

"""Task 3"""
# 3. Vazifa:
# Berilgan soʻzlar roʻyxatidan palindrom (teskari oʻqilganda ham bir xil boʻladigan) so‘zlarni tanlab oling.
# Buning uchun filter() va lambda funksiyasidan foydalaning.
# Berilgan roʻyxat:
# so'zlar = ['Anna', 'Aleksey', 'Hammasi', 'Qozoq', 'Dom', 'Alla']

def sorter(names):
    sorted_names = list(filter(lambda name: name.lower() == name.lower()[::-1], names))
    return sorted_names


sorting_list = sorter(['Anna', 'Aleksey', 'Hammasi', 'Qozoq', 'Dom', 'Alla'])
print(sorting_list)


"""Task 4"""
# 4. Vazifa:
# Berilgan so‘zlar ro‘yxatidagi har bir so‘zning uzunligini toping.
# Buning uchun map() va lambda funksiyalaridan foydalanib, so‘zlar uzunliklaridan iborat yangi ro‘yxat hosil qiling.
# Berilgan ro‘yxat: so'zlar = ("olma", "banan", "gilos")

def length_counter(list1):
    words_length = list(map(lambda x: len(x), list1))
    return words_length

words_list = length_counter(["olma", "banan", "gilos"])
print(words_list)

"""Task 5"""
# 5. Vazifa:
# Ikki xil matn ro‘yxati berilgan. Ushbu ro‘yxatlardagi elementlarni indeks bo‘yicha
# birlashtirib, bitta yangi ro‘yxat hosil qiling.
# Kirish ma’lumotlari: ['olma', 'banan', 'gilos'], ['apelsin', 'limon', 'ananas']

a = ['olma', 'banan', 'gilos']
b = ['apelsin', 'limon', 'ananas']

united = list(map(lambda x,y: f"{x} {y}", a, b))
print(united)
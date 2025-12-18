"""Task 1"""
#  1. mbox-short.txt faylini oching, ushbu fayldagi har bir satrni "o'qing" va unga mos keladigan qatorlarni toping:
#  "From Stephen.marquard@uct.ac.za Sat 5 Jan 09:14:16 2008" . Keyin barcha kiruvchi
#  elektron pochta manzillarini va jamidan chop eting.
#  Ushbu muammoni hal qilish uchun string usullaridan foydalaning.

with open("mbox-short.txt", mode="r", encoding="utf-8") as fil:
    for line in fil:
        if line.startswith("From "):
            lst = line.split(" ")
            print(lst[1])

"""Task 2"""
# 2. Muayyan fayl faylini ochadigan va oxirgi satrlarni satrlar sonidagi oxirgi satrlarni
# chop etadigan read_last(liniyalar, fayl) funksiyasini yozing (har holda, musbat butun
# son berilganligini tekshiring).

def read_last(main_line, main_file):
    with open(main_file, mode='r') as f1:
        lines = f1.readlines()

    last = lines[-main_line:]
    for l in last:
        print(l.strip())

read_last(50, "article.txt")

"""Task 3"""
# 3. romeo.txt faylini oching. Undagi har bir satrni "o'qing". Har bir satrdan alohida so'zlarni oling,
# so'ngra so'zlar ro'yxatini tuzing. Ro'yxatdagi so'zlar takrorlanmasligi kerak. Keyin barcha so'zlar alifbo
# tartibida tartiblangan ro'yxatni chop eting.

words = []
with open("romeo.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        for word in line.split(" "):
            words.append(word.strip())

words = list(set(words))
print(sorted(words), end=" ")

"""Task 4"""
# 4. Hujjat «article.txt" quyidagi matnni o'z ichiga oladi:
# Kechki ovqat
# Pashshalar guvillashdi
# Chiroq yoqdi
# Choynakdagi qaynoq suv
# Venera osmonda porladi
# Daraxtlar shitirlashardi
# Bulutlar tarqaldi
# Barglar yashil rangga aylandi
# Maksimal uzunlikka ega bo'lgan so'zni (yoki bir nechta bo'lsa, so'zlar ro'yxatini)
# chiqaradigan eng uzun_so'zlar(fayl) funksiyasini amalga oshirish talab etiladi.

main_list = []
max_len = []
with open("article.txt", mode="r", encoding="utf-8") as fl:
    for line in fl:
        for word in line.split():
            main_list.append(word)
    max_word = ""
    for word1 in main_list:
        if len(word1) > len(max_word):
            max_word = word1
            max_len.append(max_word)

print(max_len)




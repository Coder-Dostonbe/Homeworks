"""Task 1"""
# 1. Foydalanuvchi ismini so'raydigan va keyin unga salom beradigan dastur yozing.

name = input("Ismingizni kiriting: ").capitalize()
print(f"Assalomu aleykum {name}")

"""Task 2"""
# 2. Foydalanuvchidan 3 raqamni so'raydigan va ularning miqdorini ko'rsatadigan dastur yozing.

num1 = int(input("1-sonni kiriting: "))
num2 = int(input("2-sonni kiriting: "))
num3 = int(input("3-sonni kiriting: "))
print(f"Siz kiritgan 3ta raqam yig'indisi {num1 + num2 + num3} ga teng")

"""Task 3"""
# 3. Foydalanuvchidan xonaning uzunligi va kengligini so'raydigan dasturni yozing.
# Qiymatlarni kiritgandan so'ng, dastur xonaning maydonini hisoblashi va ekranda ko'rsatish kerak.
# Xonaning uzunligi va kengligi vergulli son formatida kiritilishi kerak.
# Qatorni kasr soniga aylantirish uchun float()-dan foydalaning.

xona_eni = float(input("Xonaning enini kiriting: "))
xona_boyi = float(input("Xonaning boyi kiriting: "))
print(f"Xonaning yuzi {xona_eni*xona_boyi} m kv ga teng")

"""Task 4"""
# 4. Foydalanuvchidan ikkita a va b tamsayılarini so'raydigan dastur yarating, so'ngra quyidagi matematik operatsiyalar natijalarini ko'rsatadi:
# a va b yig'indisi;
# a dan b ni ayirish;
# a ni b ga ko'paytirish;
# a ning b ga bo'lganda natija;
# a ning b ga bo'lganda qoldiq;
# a sonini b darahasiga o'tkazish natijasi

a = int(input("Birinchi sonni kiriting: "))
b = int(input("ikkinchi sonni kiriting: "))
print(f"Siz kiritgan sonlarning yig'indisi: {a+b} ga teng")
print(f"Siz kiritgan sonlarning ayirmasi {a-b} ga teng")
print(f"Siz kiritgan sonlarning ko'paytmasi {a*b} ga teng")
print(f"Siz kiritgan sonlarning bo'linmasi {a/b} ga teng")
print(f"{a} ni {b} ga bo'ganda {a%b} qoldiq qoladi")
print(f"{a} ning {b} darajasi {a**b} ga teng")

"""Task 5"""
# 5. Foydalanuvchidan raqamni so'raydigan va keyingi va oldingisini ko'rsatadigan dastur yozing:

num = int(input("Istalgan sonni kiriting: "))
print(f"{num} dan oldingi son {num-1}")
print(f"{num} dan keyingi son {num+1}")
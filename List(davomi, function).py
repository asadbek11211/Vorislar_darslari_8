"""
    27.10.2025
    Ro'yhatlarning davomi methods, functions
    methods(append(), insert(), remove(), pop(), sort(), reverse())
    functions(len(), sorted() min(), max(), sum(), range(), list(), tuple())
"""

# davlatlar = ["O'zbekiston", "Qozog'iston", "Turkmaniston", "Tojikiston", "Afg'oniston", "Rossiya", "Xitoy", "Koreya", "Yaponiya", "Malayziya"]
# uylar = list(("uy1", "uy2", "uy3", "uy4", "uy5", "uy6", "uy7", "uy8", "uy9", "uy10"))

# print(davlatlar)
# print(uylar)

# davlatlar.sort()
# print(davlatlar)

# print(sorted(davlatlar))
# print(davlatlar)

# isimlar = ["Zafarbek", "Xursandbek", "Muhammadjon", "Alijon", "Valijon", "Sardor", "Jasur", "Doston", "Bobur", "Anvar", "Kamol", "Sarvar"]
# print(isimlar)
# isimlar.sort()
# print(isimlar)

# sonlar = list(range(1,21))
# print(sonlar)
# juft_son = list(range(2,30,2)) 
# print(juft_son)

# toq_son = list(range(1,567,2))
# print(len(toq_son))

# print(len(isimlar))

# sonlar = [-9,0,96,2002,897,45,-34,23,1,-567,34,78,-6895]
# print(f" Asl royhat : {sonlar}")
# print(f" Eng kichik son : {min(sonlar)}")
# print(f" Eng katta son : {max(sonlar)}")
# print(f" Sonlar yig'indisi : {sum(sonlar)}")

# son = list(range(-365, 1003, 13))
# print(len(son))

isimlar = ["Zafarbek", "Xursandbek", "Muhammadjon", "Alijon", "Valijon", "Sardor", "Jasur", "Doston", "Bobur", "Anvar", "Kamol", "Sarvar"]


# tuple() O'zgarmas ro'yhat

moshinalar = ["bmw","mercedes","audi","ferrari","lamborgini","tesla","volvo","toyota","hyundai","kia"]
print(moshinalar)
moshinalar.remove("tesla")
print(moshinalar)
moshinalar.insert(0,"Chevralet")
print(moshinalar)

ranglar = ("qizil", "yashil", "sariq", "ko'k", "oq", "qora", "pushti", "binafsha")
print(ranglar)

# ranglar.remove("pushti")
# print(ranglar)

# ranglar.append("jigarrang")
# print(ranglar)

ranglar1 = list(ranglar)
print(ranglar1)

ranglar1.remove("qizil")
print(ranglar1)

ranglar = tuple(ranglar1)
print(ranglar)
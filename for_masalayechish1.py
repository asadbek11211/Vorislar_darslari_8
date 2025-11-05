# 7-masala

# print("a < b")
# a = int(input("A soniga butun qiymat kiriting : "))
# b = int(input("B soniga butun qiymat kiriting : "))


# # print(f"A ning malumot tipi = {type(a)}")
# # print(f"B ning malumot tipi = {type(b)}")

# sonlar = list(range(a,b+1))
#  #[1,2,3,4,5,6]
# for son in sonlar:
#     print(f"{son} - sikl : {son}")
# print(f"Royhatning yigindisi : {sum(sonlar)}")

#8 - masala
# print("a < b")
# a = int(input("A soniga butun qiymat kiriting : "))
# b = int(input("B soniga butun qiymat kiriting : "))

# sonlar = list(range(a,b+1))
# print(f"Royhat : {sonlar}")
# kopaytma = 1
# for son in sonlar:
#     kopaytma *= son
# print(f"Royhat elementlari kopaytmasi : {kopaytma}")

#9-masala
# print("a < b")
# a = int(input("A soniga butun qiymat kiriting : "))
# b = int(input("B soniga butun qiymat kiriting : "))

# sonlar = list(range(a,b+1))
# print(f"Royhat : {sonlar}")
# kvadrat = []
# yigindi = 0
# for son in sonlar:
#     kvadrat.append(son**2)
#     yigindi += son**2
# print(f"Darajaga oshgan royhat : {kvadrat}")
# print(f"Darajaga oshgan royhat elementlari yigindisi :{yigindi}")

#10-masala

n = int(input("n soniga butun qiymat kiriting : "))

sonlar = list(range(1,n+1))
yigindi = 0
korinish = []
for son in sonlar:
    i += f"1/{son}"
    korinish.append(i)
    i = 0
    yigindi += 1/son
print(korinish)
print(f"Yigindi : {yigindi}")


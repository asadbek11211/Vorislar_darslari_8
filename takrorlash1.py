print("Eng yaxshi beshta meva qaysi:")
meva = input("Ismingizni kiriting:")
mevalar = 1
savol = f"{meva.title()} {mevalar} - eng yaxshi meva qaysi:"
while mevalar <= 5:
    savol = f"{meva.title()} {mevalar} - eng yaxshi meva qaysi:"
    meva1 = input(savol)
    print(meva1)
    mevalar+=1
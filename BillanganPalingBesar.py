bilangan1 = float(input("Masukkan bilangan pertama : "))
bilangan2 = float(input("Masukkan bilangan kedua : "))

if bilangan1 > bilangan2:
    print("Bilangan pertama ({}) lebih besar dari bilangan kedua ({})".format(bilangan1, bilangan2))
elif bilangan2 > bilangan1:
    print("Bilangan kedua ({}) lebih besar dari bilangan pertama ({})".format(bilangan2, bilangan1))
else:
    print("Bilangan pertama dan kedua sama besar yaitu", bilangan1)
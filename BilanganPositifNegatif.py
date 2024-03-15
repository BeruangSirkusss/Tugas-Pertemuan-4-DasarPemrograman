bilangan = int(input("Masukkan sebuah bilangan : "))

if bilangan % 2 == 0:
    print("Bilangan {} adalah bilangan genap.".format(bilangan))
else:
    print("Bilangan {} adalah bilangan ganjil.".format(bilangan))

if bilangan > 0:
    print("Bilangan {} adalah bilangan positif.".format(bilangan))
elif bilangan < 0:
    print("Bilangan {} adalah bilangan negatif.".format(bilangan))
else:
    print("Bilangan adalah nol.")
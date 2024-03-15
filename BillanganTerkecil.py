bilangan1 = float(input("Masukkan bilangan pertama : "))
bilangan2 = float(input("Masukkan bilangan kedua : "))
bilangan3 = float(input("Masukkan bilangan ketiga : "))

bilangan_terkecil = bilangan1 

if bilangan2 < bilangan_terkecil:
    bilangan_terkecil = bilangan2

if bilangan3 < bilangan_terkecil:
    bilangan_terkecil = bilangan3

print("Bilangan terkecil adalah:", bilangan_terkecil)
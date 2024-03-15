def hitung_luas_dan_keliling_segitiga(a, b, c):
    s = (a + b + c) / 2

    luas = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    keliling = a + b + c

    return luas, keliling

a = float(input("Masukkan panjang sisi pertama segitiga: "))
b = float(input("Masukkan panjang sisi kedua segitiga: "))
c = float(input("Masukkan panjang sisi ketiga segitiga: "))

luas, keliling = hitung_luas_dan_keliling_segitiga(a, b, c)

print("Luas segitiga adalah:", luas)
print("Keliling segitiga adalah:", keliling)
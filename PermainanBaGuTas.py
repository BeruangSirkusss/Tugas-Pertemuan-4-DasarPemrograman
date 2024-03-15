pemain1 = input("Pemain 1, Masukkan pilihan (Batu/Gunting/Kertas): ")
pemain2 = input("Pemain 2, Masukkan pilihan (Batu/Gunting/Kertas): ")

pilihan_valid = ['Batu', 'Gunting', 'Kertas']
if pemain1 in pilihan_valid and pemain2 in pilihan_valid:
    if pemain1 == pemain2:
        print("Pertandingan seri!")
    elif (pemain1 == 'batu' and pemain2 == 'gunting') or (pemain1 == 'gunting' and pemain2 == 'kertas') or (pemain1 == 'kertas' and pemain2 == 'batu'):
        print("Pemain 1 menang!")
    else:
        print("Pemain 2 menang!")
else:
    print("Masukkan tidak valid! Silakan masukkan pilihan yang benar (batu/gunting/kertas).")
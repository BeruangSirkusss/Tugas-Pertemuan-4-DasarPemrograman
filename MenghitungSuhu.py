print("Program konversi suhu dari Celsius ke Fahrenheit atau sebaliknya.")

pilihan = input("Masukkan pilihan (C untuk Celsius ke Fahrenheit, F untuk Fahrenheit ke Celsius): ").upper()

if pilihan == 'C':
    celsius = float(input("Masukkan suhu dalam Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} derajat Celsius sama dengan {fahrenheit} derajat Fahrenheit.")
elif pilihan == 'F':
    fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} derajat Fahrenheit sama dengan {celsius} derajat Celsius.")
else:
    print("Masukkan tidak valid! Silakan masukkan C atau F.")
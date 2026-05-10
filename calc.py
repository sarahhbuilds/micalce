# Fungsi untuk operasi aritmatika
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error! Pembagian dengan nol."
    return x / y

# Menu operasi
print("Pilih Operasi:")
print("1. Jumlah (+)")
print("2. Kurang (-)")
print("3. Kali (*)")
print("4. Bagi (/)")

# Input pengguna
pilihan = input("Masukkan pilihan (1/2/3/4): ")

num1 = float(input("Masukkan angka pertama: "))
num2 = float(input("Masukkan angka kedua: "))

# Logika percabangan
if pilihan == '1':
    print(f"Hasil: {tambah(num1, num2)}")
elif pilihan == '2':
    print(f"Hasil: {kurang(num1, num2)}")
elif pilihan == '3':
    print(f"Hasil: {kali(num1, num2)}")
elif pilihan == '4':
    print(f"Hasil: {bagi(num1, num2)}")
else:
    print("Input tidak valid")

# 1. bikin fungsi dan operasi nya dulu
# 2. bikin menu operasi
# 3. suruh pilih menu operasi
# 4. masukan angka 1 dan 2 
# 5. bikin kondisi logika 

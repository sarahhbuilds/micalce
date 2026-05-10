# Python Calculator

Project Python pertama saya: kalkulator sederhana.

## Operasi yang Didukung
- Tambah
- Kurang
- Kali
- Bagi

## Alur Program
1. Python membaca semua function dan menyimpannya.
2. User memilih operasi.
3. User memasukkan dua angka.
4. Program mencocokkan pilihan dengan kondisi.
5. Function dipanggil.
6. `return` mengembalikan hasil ke yang memanggil (bisa print(tambah) atau yg lain)
7. `print()` menampilkan hasil.

## Contoh Output
pilih tambah, kurang, kali atau bagi: tambah
angka ke1: 10
angka ke2: 5
15.0

# Struktur
1. python lihat fungsi def tapi di simpan dulu
2. python lanjut menyuruh user input operasi yang ingin dilakukan
3. python menyuruh user memasukkan angka
4. python mencocokkan pilihan input user dengan kondisi logika

## Yang Saya Pelajari
- Functions
- Parameters
- Return
- Input
- Variables
- If / Elif / Else
- Debugging

- def tambah(x, y): >> define fungsi (tambah) dengan parameter (x, y) dan operasi (return x + y)
    return x + y

- def kurang(x, y):
    return x - y

- def kali(x, y):
    return x * y

- def bagi(x, y):
    return x / y


- pilih = (input('pilih tambah, kurang, kali atau bagi: ')) (user menginput operasi yang akan dilakukan)

# Pemilihan angka
x = float(input('angka ke1: ')) 
y = float(input('angka ke2: '))

# Kondisi Logika
if pilih == 'tambah':
    print(tambah(x, y))
elif pilih == 'kurang':
    print(kurang(x, y))
elif pilih == 'kali':
    print(kali(x, y))
elif pilih == 'bagi':
    print(bagi(x, y))
else:
    print('invalid bestieh')

# Penjelasan fungsi return
karna yg call itu print(tambah(x, y) sesuai kondisi pilih yg di input oleh user
dimana tambah x y itu x + y 
jadi dia tuh kayak muter gitu ga sih? 
python liat define dan operasi di dalamnya
lalu x dan y masuk, lalu print tambah call dan def jalan
lalu return nya dimasukin ke print(tambah) dan di print
so it's def return (simpen) > input pilihan operasi > cocokkan logika > print (tambah) di call > hasil return tambah dimasukkan ke print (tambah)

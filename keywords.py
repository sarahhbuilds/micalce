# BELAJAR KEYWORDS

# KONDISI IF, ELSE, ELIF
nilai = 7
if nilai >= 7:
    print('selamat kamu lulus!')
else:
    print('ayo remedial')

# Jika memenuhi if, akan true
# jika if tidak terpenuhi, akan ke else lalu false
# elif, lanjutan dari if, jika if tidak terpenuhi

hari_ini = "Minggu"

if(hari_ini == "Senin"):
    print("Saya akan kuliah")
elif(hari_ini == "Selasa"):
    print("Saya akan kuliah")
elif(hari_ini == "Rabu"):
    print("Saya akan kuliah")
elif(hari_ini == "Kamis"):
    print("Saya akan kuliah")
elif(hari_ini == "Jumat"):
    print("Saya akan kuliah")
elif(hari_ini == "Sabtu"):
    print("Saya akan kuliah")
elif(hari_ini == "Minggu"):
    print("Saya akan libur")


# WHILE LOOP, FOR LOOP, NESTED LOOP

# - WHILE LOOP
# eksekusi code selama kondisi sesuai
# fokus utama = kondisi logika
# contoh objek = bool true/false
count = 0
while (count < 9):
  print ("The count is: ", count)
  count = count + 1

print ("Good bye!")
# LOGIKANYA: variable count yg isinya 0,
# while(selama) count kurang dari 9, print 'the count is: ', count
# bawahnya ada var/konsidi baru, count = count + 1 disebut increment
# increment, ngubah isi var count setiap pengulangan terjadi
# kalo increment ga ditulis, code akan terus berjalan dan jadi infinite loop
# infinite loop bisa pakai 'break' biar berhentiin paksa
# kalo udah 8 (alias kurang dari 9) print good bye


# FOR LOOP
# mengulang item dari urutan apapun 
# fokus utama = urutan item
# contoh objek = list, string, array
angka = [1,2,3,4,5]
for x in angka:
  print(x)
# python itu punya variable otomatis yaitu di iterator variable
# setiap for ... in var: print(...) itu namanya bebas
# dan variable itu untuk nyimpen data dari variabel yg ada
# kalo sesuai code diatas, for x (var otomatis) 
# selama ngambil dari 1 - 5, itu bakal disimpen di x, baru di print

#Contoh pengulangan for
buah = ["nanas", "apel", "jeruk"]
for makanan in buah:
  print ("Saya suka makan", makanan)
# LOGIKANYA, selama ngambil data dari var buah dan disimpen 
# di var sementara 'makanan' baru di print dan tambahin var sementaranya
# kalo langsung print('saya suka', buah) nanti bakal jadi
# saya suka [nanas, apel, jeruk], alias ga looping dan ada kurungnya


# - NESTED LOOP
# menggunakan satu loop didalam loop lain (bersarang)
# fokus utama = complexity
# contoh objek = loop dalam loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
# kalo i lagi 1, j nya 123
# kalo i lagi 2, j nya 123
# kalo i lagi 3, j nya 123 lagi 
# jadi loop i kondisi, dan dari i kondisi itu dalemnya loop lagi


# LOGIKA OPERASI AND OR
# AND

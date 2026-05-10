# BELAJAR VARIABLE
nama = "Hartono"
alamat = 'Mataram'
umur = 19
tinggi = 170.5
menikah = 0
# mencetak isi variabel
print("Nama : ", nama)
print("Alamat : ", alamat)
print("Umur : ", umur)
print("Tinggi : ", tinggi)
if(menikah):
    print("Status: menikah")
else:
    print("Status: belum menikah")


# dari contoh diatas, ada beberapa variable dengan isi sesuai 
# var nama dan alamat = string karna ada kutip
# var umur itu tipe int
# var tinggi itu tipe float
# var menikah itu bool bisa 0/false atau 1/True
# logikanya: akan dimulai dari print nama dengan menambahkan 'nama: ' lalu var nya 
# lalu if (menikah) artinya if akan ambil data dari isi var menikah entah 0/1 
# jika isi var menikah true berarti print nya menikah dan sebaliknya
# gicu deh


# var bersifat mutable (nilai bisa berubah ubah)
# NO = 2var, 2-var, var-vars
# YES = var2, var-2, var_var 
# del(var) = untuk hapus variable
# string - pakai ""
# int dan bool ga perlu pakai ""
# type(var) = untuk periksa tipe 

# TIPE DATA VARIABLE
# str = teks, bisa pake ""/''/''''''/""""""
# int = angka tanpa .
# float = angka dengan .
# bool = true false (0 false, >=1 true)

# CASTING
# spesifikasi data dalam variable 
a = str(3) #akan jadi 3
x = int(3) #akan jadi 3
y = float(3) #akan jadi 3.0
z = bool(3) #akan jadi true
c = complex(3,2) #akan jadi 3+2j
print(a, x, y, z, c)


# BELAJAR TIPE DATA COLLECTION

# LIST 
# DIBAWAH INI LIST OF STRING (list yg isinya teks)
var = ['agus', 'asep', 'ujang']
var2 = var
var.append('koko')
var.remove('ujang')
var[0] = "meimei"

print(var)
# diatas ini logikanya list var isi nya teks, var2 = var
"""pertama tambahin koko, lalu hapus ujang
dan ubah index 0 jadi meimei"""

# list adalah salah satu tipe data koleksi di python, dia pake [] begini
# lisst itu bukan nama variable nya tapi value yg ada   i variable nya
# jadi kalo ada 2 variable yaitu a dan b tapi yg a ada isinya sedangkan yg b itu isinya variable a
# berarti ke2 tersebut tetap list yang sama 
# list pake index, dimulai dari 0
# append buat nambah data, remove buat hapus data
# untuk append dan remove, pake kurung biasa, isinya itu data yang mau ditambahin dan bukan indexnya

# KENAPA KETIKA APPEND DI LIST PAKE () DAN BUKAN [] PADAHAL LIST KAN PAKE [] DI PYTHON?
# () untuk metode/fungsi, [] untuk data, dan append adalah metode/fungsi dan bukan data
# append fungsinya untuk nambahin data ke list

# SET
var = {1, 2, 3, 4}
var.add(5)
var.remove(1)
print(var, type(var))

var = {'apel', 'jeruk', 'pir', 'melon'}
var.add('mangga')
var.remove('jeruk')
print(var)
# hasilnya unordered, karna tidak ada index

# set itu mutable alias valuenya bisa diubah
# pake {}, GA PAKE INDEX JADI GABISA UBAH SUATU VALUE
# gabisa elemen ganda, untuk saring duplikat


# TUPLE
var = (1, 2, 3, 4)
print(type(var))
# gabisa ubah isi
# pake index juga
# untuk data konsisten

# DICTIONARY
vardict = {
    "nama": "sarah",
    "kelas": 12,
    "domisili" : "bogor",
}
print(vardict["nama"])

vardict["alamat"] = "citoh" # nambahin data
del vardict['kelas']
print(vardict)
# ngambil data tertentu dari key(yg awal)
# pake [] karna untuk manggil fungsi yaitu del fungsi hapus
# dan vardict[] untuk nambah data
# bisa juga pake var.update({})
# untuk nambahin banyak item sekaligus atau gabungin 2 dict

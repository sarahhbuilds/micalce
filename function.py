# BELAJAR FUNCTION PYTHON
# function untuk menjalankan sebuah blok kode
# bukannya python itu berbaris ya? 
# kenapa sapa user bisa ada diatas pas define tapi isinya ada di bawah?
"""gini: 
1. python baca fungsi def, tapi ga dijalanin, cuma simpen di memori
2. print dibawahnya dilewati dulu(kalo ada)
3. print diluar def dijalanin pertama
4. panggil fungsi(python liat, dan lompat lagi ke def paling atas)
5. baru dijalanin semua"""

# DEFINE 
def sapa_user(nama): #simpen memori
    print("Halo, " + nama + "! Selamat belajar Python.") #skip dulu
print('mulai belajar') # dijalanin pertama

# Panggil fungsi
sapa_user("Budi") #liat ini, balik lagi keatas, baru dijalanin
sapa_user("Andi") #same lah

# def = keyword untuk bikin fungsi
# sapa_user = nama fungsi, bebas
# (nama) = parameter (input)
# : = titik 2 wajib ada
# print ... = isi fungsi wajib indent




# RETURN
# nama dalam () itu cuma label/parameter, bukan manggil variable
def pabrik_roti(tepung, air): #(a, b) itu cuma parameter
    adonan = tepung + air
    return adonan # proses dari parameter    

hasil = pabrik_roti(5, 5) # Manggil pabrik, tepung=10, air=5. 
# Hasilnya (15) DISIMPAN ke variabel 'roti_jadi'
print(hasil)

# Di layar nggak muncul apa-apa (karena nggak ada print).
# TAPI, sekarang variabel 'hasil' isinya angka 10.


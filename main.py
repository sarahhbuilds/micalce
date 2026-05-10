# uangsaya = 200000
# gameps = 10000
# gamexbox = 12000
# gasing = 2000

# if uangsaya > (gamexbox + gameps + gasing):
#     print("beli semua")
# elif uangsaya >= gamexbox:
#     print("beli xbox")
# elif uangsaya >= gameps:
#     print('beli ps')
# elif uangsaya >= gasing:
#     print("beli gasing")
# else:
#     print("tidak beli apapun")


# function = memanggil blok kode secara reusable?
# def greet(name):
#     text = "namanya adalah " + name
#     print(text)

# greet("sarah")
# greet("irisa")
# greet("chiaki")
# greet("katzewie")

# case
# def hitung_ongkir(kota, berat):
#     tarif_per_kg = {
#         "Jakarta": 10000,
#         "Bandung": 12000,
#         "Surabaya": 15000
#     }

#     if kota in tarif_per_kg:
#         ongkir = berat * tarif_per_kg[kota]
#         print(f"ongkir ke {kota} untuk {berat}kg adalah rp{ongkir}")
#     else:
#         print("kota belum didukung.")

# hitung_ongkir("Bandung", 3)

# GREETING GENERATOR
# name = input("siapa namamu byotch")
# city = input("tinggal dimana byotch")
# age = input("umur berapa byotch")

# print(f"hi {name} dari {city}")
# print(f"tua juga ya umurmu udah {age}")

# import random

# affirmations = [
#     "Kamu lebih kuat dari yang kamu kira",
#     "Hari ini akan baik-baik saja",
#     "Kamu layak untuk sukses",
#     "Istirahat itu produktif",
#     "Kamu tidak sendirian"
# ]

# print(random.choice(affirmations), type(affirmations))

# list_a = ["Seoul", "Taipei"]
# list_b = list_a
# list_b.append("Tokyo")
# print(list_a)

# mood = "lelah"
# output = "Scroll TikTok" if mood == "tired" else "Belajar Python"
# print(output)

# inventory = [
#     {"item": "Manga", "harga": 15},
#     {"item": "Skincare", "harga": 50},
#     {"item": "Laptop", "harga": 1200}
# ]

# total_biaya = 0
# budget = 1000

# for barang in inventory:
#     total_biaya = total_biaya + barang["harga"]
# if total_biaya > (budget):
#         print('gagal pindah ke taiwan')
# else:
#         print('berhasil kabur')

# print(f"Total yang harus dibayar: ${total_biaya}")

# The "Why" of Memory - This is what makes Python click for an INTP
a = [1, 2, 3]
b = a
c = b
c.append(4)

print(f"a is: {a}")
print(f"b is: {b}")
print(f"c is: {c}")
print(f"Are they the same object in memory? {a is b or c}")

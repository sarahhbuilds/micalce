# 1. Siapkan wadah (list) untuk menampung harga-harga barang
keranjang = []

print("--- SELAMAT DATANG DI TOKO PYTHON ---")
print("Ketik '0' untuk selesai dan hitung total.")

# 2. Mulai pengulangan (While Loop)
while True:
    harga = int(input("Masukkan harga barang: "))
    
    # 3. Kondisi untuk berhenti (If-Else)
    if harga == 0:
        break # Keluar dari loop jika inputnya 0
    else:
        keranjang.append(harga) # Masukkan harga ke dalam list

# 4. Hitung total (Operasi Matematika)
total_belanja = sum(keranjang)

print("\n---------------------------")
print("Total belanjaan Anda: Rp", total_belanja)

# 5. Tambahan logika diskon (If-Else)
if total_belanja > 50000:
    diskon = total_belanja * 0.1 # Diskon 10%
    total_akhir = total_belanja - diskon
    print("Selamat! Anda dapat diskon 10%: Rp", int(diskon))
    print("Total yang harus dibayar: Rp", int(total_akhir))
else:
    print("Total yang harus dibayar: Rp", total_belanja)

print("--- TERIMA KASIH ---")

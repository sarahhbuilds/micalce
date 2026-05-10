def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y


pilih = (input('pilih tambah, kurang, kali atau bagi: '))

x = float(input('angka ke1: '))
y = float(input('angka ke2: '))


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

# oh i get it, karna yg call itu print(tambah(x, y) 
# dimana tambah x y itu x + y 
# jadi dia tuh kayak muter gitu ga sih? 
# python liat define dan operasi di dalamnya
# lalu x dan y masuk, lalu print tambah call dan def jalan
# lalu return nya dimasukin ke print(tambah)  
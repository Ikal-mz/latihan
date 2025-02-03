# global dan local scope

nama_global = "budi"    # <- ini variabel global

# akses variabel global dalam fungsi
def fungsi() :
    print(f"fungsi menampilkan {nama_global}")

fungsi()

# akses variabel global dalam loop
for i in range(0,5) :
    print(f"loop {i} - {nama_global}")

# akses variabel global dalam percabangan
if True :
    print(f"if menampilkan {nama_global}")

# variabel local scope
def fungsi() :
    nama_local = "bambang"  # <- variabel local scope

fungsi()
# print(nama_local)   <- akan error karena mengakses variabel local scope

# contoh 1 penggunaan : akses variabel
def say_budi() :
    print(f"hallo {nama}")

nama = "budi"
say_budi()

# contoh 2 penggunaan : merubah variabel global
angka = 0
name = "ringgo"

def ubah(nilai_baru, nama_baru) :
    global angka    # <- fungsi ini mendapat akses merubah variabel global
    global name
    angka = nilai_baru
    name = nama_baru

print(f"sebelum{angka,name}")
ubah(11,"budi")
print(f"sesudah{angka,name}")

# contoh 3
angka = 0

for i in range(0,5) :
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True :
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)
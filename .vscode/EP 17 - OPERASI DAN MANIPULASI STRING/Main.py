#operator dalam bentuk methods

##merubah case dari string

#merubah semua ke upper case (huruf besar)
salam = "bro!"
print("normal =",salam)
salam = salam.upper()
print("upper =",salam)

#merubah semua ke lower case (huruf kecil)
alay = "aKu Gaul AbiseeeZzzzZ"
print("normal =", alay)
alay = alay.lower()
print("lower =", alay)

##pengecekan dengan isX method

#pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()  #hasilnya boolean
print(salam, "is lower =", apakah_lower)
apakah_upper = salam.isupper()  #hasilnya boolean
print(salam, "is upper =", apakah_upper)

# isalpha() <-- untuk mengecek semua huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline (\n)
# istitle() <-- semua kata dimulai dengan huruf besar

print("=======CEK SEMUA HURUF========")
huruf = "Markona"
cek_huruf = huruf.isalpha()
print(huruf, "is alpha? =", cek_huruf)
huruf = "wiro 212"
cek_huruf = huruf.isalpha()
print(huruf, "is alpha? =", cek_huruf)


print("=======CEK HURUF DAN ANGKA========")
huruf_dan_angka = "wiro212"
cek = huruf_dan_angka.isalnum()
print(huruf_dan_angka, "merupakan huruf dan angka =", cek)
huruf_dan_angka = "ada spasi"
cek = huruf_dan_angka.isalnum()
print(huruf_dan_angka, "merupakan huruf dan angka =", cek)


print("=======CEK ANGKA SAJA========")
huruf = "Markona"
cek_huruf = huruf.isdecimal()
print(huruf, "merupakan semua angka =", cek_huruf)
huruf = "1997"
cek_huruf = huruf.isdecimal()
print(huruf, "merupakan semua angka =", cek_huruf)

print("=======SPASI ATAU TAB========")
spasi = " "
cek = spasi.isspace()
print(spasi, "berisi spasi saja =",cek)
spasi = "Budi"
cek = spasi.isspace()
print(spasi, "berisi spasi saja =",cek)

print("=======HURUF AWAL SELALU BESAR========")
besar = "Aku sayang"
cek = besar.istitle()
print(besar, "huruf awal selalu besar = ", cek)
besar = "Aku Sayang"
cek = besar.istitle()
print(besar, "huruf awal selalu besar = ", cek)

##mengecek komponen startswith(), endswith()
cek_start = "Bambang Pamungkas".startswith("Bambang")
print("start =", cek_start)

cek_end = "Bambang Pamungkas".endswith("Pamungkas")
print("end =", cek_end)

## penggabungan komponen join(), split()
pisah = ['aku', 'sayang', 'kamu']
gabungan = '.'.join(pisah)
print(pisah)
print(gabungan)
gabungan = ' '.join(pisah)
print(gabungan)
gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# akolasi karakter rjust(), ljust(), center()
print('='*5,'+'*3,'='*5)

kanan = "bambang".rjust(11)
print("'",kanan,"'")

kiri = "bambang".ljust(11)
print("'",kiri,"'")

tengah = "bambang".center(11)
print("'",tengah,"'")

tengah = "bambang".center(20,'-')
print("'",tengah,"'")

# kebalikannya -> strip()
tengah = tengah.strip("-")
print("'",tengah,"'")

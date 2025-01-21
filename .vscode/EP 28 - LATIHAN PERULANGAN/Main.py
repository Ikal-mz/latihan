# latihan perulangan membuat segitiga

sisi = 11

# 1. menggunakan for

#dummy variabel

print("Awal dari for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("Akhir dari for")

# 2. menggunakan while

print("\nAwal dari while")
count = 1
while True :
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("Akhir dari while")

# 3. hanya ganjil saja

print("\nAwal ganjil")
count = 1
while True :
    if count % 2:
        #print jika ganjil
        print("*"*count)
        count += 1
    else:
        #kembali ke atas jika genap
        count += 1
        continue
    
    #akan break jika melebihi sisi
    if count > sisi:
        break

print("Akhir ganjil")

# 4. hanya ganjil saja

print("\nAwal ganjil")
count = 1
spasi = int(sisi//2)

while True :
    if count % 2:
        #print jika ganjil
        print(" "*spasi,"*"*count)
        spasi -= 1
        count += 1
    else:
        #kembali ke atas jika genap
        count += 1
        continue
    
    #akan break jika melebihi sisi
    if count > sisi:
        break

print("Akhir ganjil")
#modolus genap = 0
#modolus ganjil = 1






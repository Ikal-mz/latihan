#continue, pass break

#pass -> berfungsi sebagai dummy, tidak akan di eksekusi

angka = 0

while angka < 5 :
    angka += 1

    if angka == 3 :
        pass    #ini tidak akan di eksekusi

    print(angka)

print(f"akhir program \n")

#continue

angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5 :
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3 :
        print("mantap !")
        continue    #akan membuat loop meloncat ke step selanjutnya

    print("done")

print("akhir program !")
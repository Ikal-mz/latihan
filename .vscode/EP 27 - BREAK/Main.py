#break

angka = 0

while angka < 5 :
    angka += 1
    print(f"angka sekarang = {angka}")

    if angka == 3 :
        print("mantap")
        break

    print("wadaw")

print("akhir program \n")

data_int = int(input("hitung angka sampai = "))

angka = 0

while True :
    angka += 1
    print(f"count = {angka}")

    if angka == data_int :
        print("mantap")
        break
    print("wadaw")

print("akhir program")
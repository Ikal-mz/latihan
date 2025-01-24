# latihan fungsi

import os

# membuat header program
os.system("cls")

print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
print(f"{'-'*30:^40}")

# mengambil input user
PANJANG = int(input("Masukan nilai panjang : "))
LEBAR = int(input("Masukan nilai lebar : "))

# program menghitung luas dan keliling
LUAS = PANJANG*LEBAR
KELILING = 2*(PANJANG+LEBAR)

# tampilkan hasilnya
print(f"Hasil perhitungan luas : {LUAS}")
print(f"Hasil perhitungan keliling : {KELILING}")


## LANJUTKAN 
# https://www.youtube.com/watch?v=AcyUE59S53U&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=51&ab_channel=KelasTerbuka
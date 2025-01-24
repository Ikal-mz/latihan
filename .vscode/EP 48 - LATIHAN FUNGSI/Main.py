# latihan fungsi

import os

# membuat header program
"""os.system("cls")

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
print(f"Hasil perhitungan keliling : {KELILING}")"""


def header() :
    """FUNGSI HEADER"""
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*30:^40}")

def input_user() : 
    """FUNGSI INPUT USER"""
    panjang = int(input("Masukan nilai panjang : "))
    lebar = int(input("Masukan nilai lebar : "))
    return panjang,lebar

def hitung_luas(panjang,lebar) :
    """FUNGSI LUAS"""
    return panjang*lebar

def hitung_keliling(panjang,lebar) :
    """FUNGSI KELILING"""
    return 2*(panjang+lebar)

def display(message,value) :
    """FUNGSI DISPLAY"""
    print(f"Hasil perhitungan {message} = {value}")

# Program utama
while True :
    header()
    PANJANG,LEBAR = input_user()
    LUAS = hitung_luas(PANJANG,LEBAR)
    KELILING = hitung_keliling(PANJANG,LEBAR)
    display("luas", LUAS)
    display("keliling", KELILING)
    
    isContinue = input("Apakah lanjut (y/n)?")
    if isContinue == "n" :
        break

print("Program selesai, terima kasih")
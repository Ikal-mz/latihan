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
    luas =  panjang*lebar
    return display("luas", luas)

def hitung_keliling(panjang,lebar) :
    """FUNGSI KELILING"""
    keliling =  2*(panjang+lebar)
    return display("keliling", keliling)

def display(message,value) :
    """FUNGSI DISPLAY"""
    print(f"Hasil perhitungan {message} = {value}")

def opsi () :
    pilih = input("1 untuk hitung keliling, 2 untuk hitung luas, 3 untuk hitung keduanya : ")
    if pilih == "1" :
        PANJANG,LEBAR = input_user()
        keliling = hitung_keliling(PANJANG,LEBAR)
    elif pilih == "2" : 
        PANJANG,LEBAR = input_user()
        luas = hitung_luas(PANJANG,LEBAR)
    elif pilih == "3" :
        PANJANG,LEBAR = input_user()
        keliling = hitung_keliling(PANJANG,LEBAR)
        luas = hitung_luas(PANJANG,LEBAR)
    else :
        print("Masukan Opsi Yang Benar!!!")

# Program utama
while True :
    header()
    opsi()
    
    isContinue = input("Apakah lanjut (y/n)?")
    if isContinue == "n" :
        break

print("Program selesai, terima kasih")


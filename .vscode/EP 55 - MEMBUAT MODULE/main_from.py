# membuat matematika dengan module

from matematika import tambah,kali,pangkat
# from matematika import *      <- mengambil semua komponen dalam file matematika

hasil_tambah = tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kali(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat3 = pangkat(3)
print(f"hasil pangkat3 = {pangkat3(4)}")
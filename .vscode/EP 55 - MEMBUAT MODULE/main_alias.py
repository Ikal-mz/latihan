# membuat matematika dengan module

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as pngkt
# from matematika import *      <- mengambil semua komponen dalam file matematika

import matematika as match

hasil_tambah = match.tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = k(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat3 = pngkt(3)
print(f"hasil pangkat3 = {pangkat3(4)}")
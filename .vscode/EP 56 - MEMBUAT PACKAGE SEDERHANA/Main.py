import sains.matematika
from sains import fisika
from sains.fisika import gaya as gy

hasil_tambah = sains.matematika.tambah(1,2,3,4,5,6)
print(f"hasil tambah : {hasil_tambah}")

gaya = fisika.gaya(50,2)
print(f'gaya adalah {gaya}')

gaya = gy(50,2)
print(f"gaya adalah {gaya}")


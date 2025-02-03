# import 

# fungsinya untuk mengambil program dari file external .py

# 1. menyambungkan program dari external
import program_print
import ucup

# 2. import dengan data
import variabel
import var

# data ada di namespace variabel
print(variabel.data)
print(var.data)

# 3. import dengan fungsi
import matematika

hasil = matematika.tambah(9,6)
print(hasil)
#operasi dan manipulasi string

#1. menyambung string (concatenate)
nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Luffi"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

#2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari ", nama_lengkap , "=", str(panjang))

#3. operator untung string

#mengecek apakah ada komponen char atau string di dalam sebuah sting

d = "d"
status = d in nama_lengkap
print(d, "ada di", nama_lengkap, "=", str(status))

D = "D"
status = D in nama_lengkap
print(D, "ada di", nama_lengkap, "=", str(status))

d = "d"
status = d not in nama_lengkap
print(d, "tidak ada di", nama_lengkap, "=", str(status))

#mengulang string
print("wk"*10)
print(11*"wk")

#indexing
print("nama lengkap : ", nama_lengkap)
print("index ke-0 : ", nama_lengkap[0])
print("index ke-7 : ", nama_lengkap[7])
print("index ke-(-1) : ", nama_lengkap[-1])
print("index ke-(-4) : ", nama_lengkap[-4])
print("index ke-(-5) : ", nama_lengkap[-5])
print("index ke-[0:3] : ", nama_lengkap[0:4])
print("index ke-[3:8] : ", nama_lengkap[3:9])
print("index ke-[0,2,4,6,8,10,12] : ", nama_lengkap[0:13:2])

#item paling kecil
print("paling kecil : ", min(nama_lengkap))
#item paling besar
print("paling besar : ", max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi : ", str(ascii_code))
data = 117
print("char untuk ASCII 117 : ", chr(data))

#4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count('o')
print("jumlah data o pada ", data, '=', str(jumlah))
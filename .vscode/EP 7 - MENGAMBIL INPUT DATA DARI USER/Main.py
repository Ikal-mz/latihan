#INPUT USER
#data yang di masukan pasti string

data = input("Masukan data : ")
print("data =", data, "type = ", type(data))

#jika kita ingin mengambil data integer/float
#maka di casting dulu data str ke int/float
angka = int(input("Masukan Angka : "))
print("data =", angka, "type = ", type(angka))

#untuk boolean kita perlu casting data ke int dulu baru casting ke boolean
biner = bool(int(input("Masukan Nilai Boolean : ")))
print("data =", biner, "type = ", type(biner))

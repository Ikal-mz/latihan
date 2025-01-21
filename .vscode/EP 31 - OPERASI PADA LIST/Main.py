data_angka = [1,3,4,5,6,2,3,2,5,7,8,2,0,8,6,1]

print(f"data angka = \n{data_angka}")

# count data
jumlah_data_1 = data_angka.count(1)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah data 1 = {jumlah_data_1}")
print(f"jumlah data 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["budi", "bambang", "markona", "halima"]
print(f"data = {data}")

index_budi = data.index("budi")
index_markona = data.index("markona")
print(f"index si budi = {index_budi}")
print(f"index si markona = {index_markona}")

# mengurutkan list
print(f"data angka sebelum di sort \n{data_angka}")
data_angka.sort()
print(f"data angka setelah di sort \n{data_angka}")

print(f"data sebelum di sort \n{data}")
data.sort()
print(f"data setelah di sort \n{data}")

# balik listnya (reverse)
data.reverse()
data_angka.reverse()
print(f"data di reverse \n{data} \n {data_angka}")

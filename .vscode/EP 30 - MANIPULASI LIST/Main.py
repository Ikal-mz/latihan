# Operasi

# Index     0(-4)   1(-3)   2(-2)   3(-1)
data = ["bambang", "budi", "riko", "rambo"]

# mengambil data dari list
data_0 = data[-4]
print(f"data pertama (index ke-0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# manipulasi data
# menambah item pada list sesuai posisi
print(f"data sebelum ditamabah \n{data}")

data.insert(2,"mamen")
print(f"data sesudah ditambah \n{data}")

# menambah item pada posisi terakhir
data.append("ringgo")
print(f"data ditambah lagi di posisi akhir = \n{data}")

# menambahkan list dengan list
data_baru = {"ujang", "yujing", "puyeng"}
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# ubah data index ke 2
data[2] = "bastian"
print(f"data rubah = \n{data}")

# menghapus data (remove)
data.remove("rambo")
print(f"data remove = \n{data}")

# remove data paling akhir
data_akhir = data.pop()
print(f"data remove paling akhir = \n{data}")

print(f"data remove paling akhir = \n{data_akhir}")







data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4]
print(f"data list biasa {data_list_biasa}")

list_2D = [data_0,data_1,data_list_biasa,6,7]
print(f"data 2D {list_2D}")

# contoh penggunaan
peserta_0 = ["riko","25","laki-laki"]
peserta_1 = ["budi","15","laki-laki"]
peserta_2 = ["hapsa","27","perempuan"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"list peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama \t: {peserta[0]}")
    print(f"umur \t: {peserta[1]}")
    print(f"gender \t: {peserta[2]}\n")

# dengan reference
list_copy = list_peserta.copy()
print(f"list peserta = {list_copy}")

peserta_0[0] = "bambang"
print(f"list peserta = {list_copy}")
print(f"list peserta = {list_peserta}")


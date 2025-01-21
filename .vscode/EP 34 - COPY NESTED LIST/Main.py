data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1,9]
data_2D_copy = data_2D.copy()

print(f"data \t\t= {data_2D}")
print(f"data copy \t= {data_2D_copy}")

# mengambil data dari nested list
data = data_2D[0][1]
print(f"data = {data}")

#address datanya
print(f"address data 2D \t= {hex(id(data_2D))}")
print(f"address data 2D copy \t= {hex(id(data_2D_copy))}")

print("address dari member ke-0")
print(f"address asli \t= {hex(id(data_2D[0]))}")
print(f"address copy \t= {hex(id(data_2D_copy[0]))}")

data_2D[0][1] = 5
data_2D[2] = 8
print(f"data \t\t= {data_2D}")
print(f"data copy \t= {data_2D_copy}")

# kita gunakan deepcopy
from copy import deepcopy
data_2D = [data_0,data_1,9]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address data 2D \t= {hex(id(data_2D))}")
print(f"address data 2D copy \t= {hex(id(data_2D_deepcopy))}")

print("address dari member ke-0")
print(f"address asli \t= {hex(id(data_2D[0]))}")
print(f"address copy \t= {hex(id(data_2D_deepcopy[0]))}")

data_2D[0][1] = 97
print(f"data \t\t= {data_2D}")
print(f"data copy \t= {data_2D_copy}")
print(f"data deep \t= {data_2D_deepcopy}")

# kesimpulan -> penggunaan deepcopy di sarankan untuk nested list
#CASTING ADALAH MERUBAH DATA DARI SATU TIPE KE TIPE LAIN
#tipe data = int, float, str, bool
print("====integer===")
data_int = 11
print("data =",data_int,", type = ", type(data_int))


data_float = float(data_int)
print("data =",data_float,", type = ", type(data_float))

data_str = str(data_int)
print("data =",data_str,", type = ", type(data_str))

data_bool = bool(data_int) #akan false jika nilai int adalah 0
print("data =",data_bool,", type = ", type(data_bool))

print("====float===")
data_float = 11.8
print("data =",data_float,", type = ", type(data_float))

data_int = int(data_float) #dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data =",data_int,", type = ", type(data_int))
print("data =",data_str,", type = ", type(data_str))
print("data =",data_bool,", type = ", type(data_bool))

print("====bolean===")
data_bool = False
print("data =",data_bool,", type = ", type(data_bool))

data_int = int(data_bool) 
data_str = str(data_bool)
data_float = float(data_bool)
print("data =",data_int,", type = ", type(data_int))
print("data =",data_str,", type = ", type(data_str))
print("data =",data_float,", type = ", type(data_float))


print("====string===")
data_str = "22"
print("data =",data_str,", type = ", type(data_str))

data_int = int(data_str) #string harus angka
data_bool = bool(data_str) #falsa jika string kosong
data_float = float(data_str) #string harus angka
print("data =",data_int,", type = ", type(data_int))
print("data =",data_bool,", type = ", type(data_bool))
print("data =",data_float,", type = ", type(data_float))
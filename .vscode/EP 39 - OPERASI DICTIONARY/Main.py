# operator dictionary

data_dict = {
    "rg" : "ringo",
    "zl" : "zulaiha",
    "il" : "ilon"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary = {LENDICT}")

# mengecek key exist atau tidak
KEY = "il"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict = {CHECKKEY}")

# mengakses velue (read) dengan get
print(data_dict["zl"])      # akan error jika key dalam data_dict tidak ada
print(data_dict.get("zl"))
print(data_dict.get("zzz"))
print(data_dict.get("zzz","key yang di cari tidak ditemuka"))   #cek key dengan message

# mengupdate data
data_dict["il"] = "ilmus"   # key yg sudah ada di update valuenya
print(data_dict)

data_dict["uus"] = "usman" # jika key blm ada maka di tambahkan key dan value baru
print(data_dict)

data_dict.update({"il" : "ilon"})   #jika key sudah ada di update value
print(data_dict)

data_dict.update({"jc" : "jheky chan"}) #jika key blm ada di tambahkan key dan value baru
print(data_dict)

# mendelete data dict
del data_dict["uus"]
print(data_dict)

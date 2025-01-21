#width and multiline

# data

data_nama = "Budi"
data_umur = 17
data_tinggi = 165.5
data_nomor_sepatu = 41

#string standar
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, ukuran sepatu = {data_nomor_sepatu}"
print(5*"=","Data String",5*"=")
print(data_string)

#string multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nukuran sepatu = {data_nomor_sepatu}"
print("\n",5*"=","Data String",5*"=")
print(data_string)

#string multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
ukuran sepatu = {data_nomor_sepatu}
"""
print("\n",5*"=","Data String",5*"=")
print(data_string)

#string multiline (mengatur lebar)
data_string = f"""
nama          = {data_nama:>6}
umur          = {data_umur:>6}
tinggi        = {data_tinggi:>6}
ukuran sepatu = {data_nomor_sepatu:>6}
"""
print("\n",5*"=","Data String",5*"=")
print(data_string)
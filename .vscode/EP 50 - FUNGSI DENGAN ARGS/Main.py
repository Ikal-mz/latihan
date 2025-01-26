"""*args"""

# memasukan data/argument

def fungsi(nama,tinggi,berat) :
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("bambang", 155, 55)

def fungsi(data_list) :
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["budi", 166, 65])

# penggunaan *args

def fungsi(*args) :
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("riko", 160, 60)

# studi kasus

def tambah(*data) :
    # data tipenya adalah tuple, dia bisa diiterasi
    output = 0
    for angka in data :
        output += angka
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9,10)
print(f"hasil = {hasil}")

hasil = tambah(11,43,22,5)
print(f"hasil = {hasil}")
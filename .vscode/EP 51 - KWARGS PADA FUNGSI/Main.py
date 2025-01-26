"""**kwargs"""

def fungsi(nama,tinggi,berat) :
    """fungsi biasa"""
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("budi", 155, 59)

def fungsi (**kwargs) :
    """fungsi kwargs"""
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="ringgo", tinggi=170, berat=60)

# studi kasus

def match(*args, **kwargs) :
    output = 0
    if kwargs["option"] == "tambah" :
        for angka in args :
            output += angka
    elif kwargs["option"] == "kali" :
        output = 1
        for angka in args :
            output *= angka
    else :
        print("tidak ada operasi")

    return output

hasil = match(1,2,3,4,5,option="tambah")
print(f"hasil jumlah = {hasil}")

hasil = match(1,2,3,4,5,option="kali")
print(f"hasil kali = {hasil}")
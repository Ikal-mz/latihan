from . import Operasi

def create_console():
    print("\n\n","="*100)
    print("Silakan Tambah Data Buku\n")
    judul = input("Judul\t: ")
    penulis = input("Penulis\t: ")
    while (True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun Salah, Silakan Masukan Tahun Lagi (yyyy)")
        except:
            print("Tahun Harus Angka, Silakan Masukan Tahun Lagi (yyyy)")
    
    Operasi.create(tahun,judul,penulis)
    print("\nBerikut Adalah Data Baru Anda")
    read_console()

def read_console():
    data_file = Operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "penulis"
    tahun = "Tahun"

    # header
    print("\n","="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    print("data")

    # data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")


    #fotter
    print("="*100,"\n")

from . import Operasi

def delete_console():
    read_console()
    while(True):
        print("Silakan masukan nomor buku yang akan di delete")
        no_buku = int(input("Nomor Buku : "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            data_add = data_break[1]
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4][:-1]

            # data yang ingin diupdate
            print("\n\n","="*100)
            print("Data yang inigin dihapus\n")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")

            is_done = input("Yakin akan dihapus (y/n)? ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
        else:
            print("Nomor tidak valid")
    print("Data berhasil dihapus")

def update_console():
    read_console()
    while(True):
        print("Silakan masukan nomor buku yang akan di update")
        no_buku = int(input("Nomor Buku : "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("Nomor tidak valid")
    
    data_break = data_buku.split(",")
    pk = data_break[0]
    data_add = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4][:-1]

    while(True):
        # data yang ingin diupdate
        print("\n\n","="*100)
        print("Silakan pilih data yang akan di ubah\n")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # memilih mode untuk update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n\n","="*100)
        match user_option:
            case "1": judul = input("judul\t: ")
            case "2": penulis = input("penulis\t: ")
            case "3":
                while (True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun Salah, Silakan Masukan Tahun Lagi (yyyy)")
                    except:
                        print("Tahun Harus Angka, Silakan Masukan Tahun Lagi (yyyy)")
            case _: print("Index tidak cocok")

        print("Data Baru Anda\n")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        
        is_done = input("Apakah data sudah sesuai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

    Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)

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

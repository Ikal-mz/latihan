from time import time
from . import Database
from .Util import random_sting
import time

def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'

    panjang_data = len(data_str)

    try:
        with(open(Database.DB_NAME,'r+', encoding="utf-8")) as file :
            file.seek((panjang_data+1)*(no_buku-1))
            file.write(data_str)
    except:
        print("Error saat update data")

def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_sting(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data tidak bisa di tambahkan")


def create_first_data():
    penulis = input("Penulis : ")
    judul = input("Judul : ")
    while (True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun Salah, Silakan Masukan Tahun Lagi (yyyy)")
        except:
            print("Tahun Harus Angka, Silakan Masukan Tahun Lagi (yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_sting(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("aaaaaaa")

def read(**kwargs):

    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("Error Membaca Database")
        return False
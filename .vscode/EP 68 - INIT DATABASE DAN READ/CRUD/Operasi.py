from . import Database
from .Util import random_sting
import time

def create_first_data():
    penulis = input("Penulis : ")
    judul = input("Judul : ")
    tahun = input("Tahun : ")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_sting(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("aaaaaaa")

def read():
    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines()
            return content
    except:
        print("Error Membaca Database")
        return False
from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}


def init_consule():
    try:
        with open(DB_NAME,"r") as file:
            print("database tersedia")
    except:
        print("database tidak ditemukan, membuat database baru")
        with open(DB_NAME,"w",encoding="utf-8") as file:
            Operasi.create_first_data()
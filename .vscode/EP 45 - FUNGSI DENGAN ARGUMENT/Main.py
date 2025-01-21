"""FUNGSI DENGAN ARGUMENT (INPUT/PARAMETER)"""

"""
def nama_fungsi(argument):
    badan fungsi
"""


def hello_world(nama) :
    """fungsi hello_world menerima input dengan variabel"""
    print(f"Selamat datang wahai {nama}")

hello_world("Budi")
hello_world("Bambang")

# program tambah
def tambah(angka_1,angka_2) :
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(4,3)
tambah(42553,233)

def say_hi(list_peseta) :
    data_peserta = list_peseta.copy()
    for peserta in data_peserta :
        print(f"yang terhormat {peserta}")

anggota_boyband = ["bambang","budi","dudung"]

say_hi(anggota_boyband)
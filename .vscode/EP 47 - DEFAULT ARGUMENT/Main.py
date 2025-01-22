"""DEFAULT ARGUMENT"""

# def fungsi(argument) :

# def fungsi(argument = "nilai default") :

# contoh 1
def say_hello(nama="cantik") :
    """fungsi dengan default argument"""
    print(f"hallo {nama}")

say_hello("markona")
say_hello()

# contoh 2
def sapa_dia(nama,pesan="Apa Kabar?") :
    """fungsi dengan 1 argument biasa dan 1 default argument"""
    print(f"hai {nama}, {pesan}")

sapa_dia("budi", "mantap")
sapa_dia("bambang")

# contoh 3
def hitung_pangkat(angka, pangkat=2) :
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(4,2))

hasil = hitung_pangkat(pangkat=4,angka=3)
print(hasil)

# contoh 4
def fungsi(method1=1, method2=2, method3=3, method4=4) :
    hasil = method1+method2+method3+method4
    return hasil

print(fungsi())
print(fungsi(method3=9))


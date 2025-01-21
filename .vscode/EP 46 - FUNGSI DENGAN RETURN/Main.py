# Template fungsi dengan return

"""
def nama_fungsi (argument) :
    badan fungsi
    return/output
"""

# fungsi kuadrat

def kuadrat(input_angka) :
    output_angka = input_angka**2
    return output_angka

y = kuadrat(8)
print(y)

print(kuadrat(4))

z = 11 + kuadrat(8)
print(z)

# fungsi tambah

def tambah(angka_1,angka_2) :
    return angka_1 + angka_2

a = tambah(8,11)
print(a)

def a():
    print("oke")

# fungsi dengan return banyak

def operasi_math(angka_1,angka_2) :
    penjumlahan = angka_1 + angka_2
    pengurangan = angka_1 - angka_2
    perkalian = angka_1 * angka_2
    pembagian = angka_1 / angka_2

    return penjumlahan,pengurangan,perkalian,pembagian

o,p,q,r = operasi_math(8,3)
print(f"hasil dari penjumlahan = {o}")
print(f"hasil dari pengurangan = {p}")
print(f"hasil dari perkalian = {q}")
print(f"hasil dari pembagian = {r}")
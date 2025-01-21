# looping dari list

# for loop
print("For Loop")
kumpulan_angka = [1,2,3,5,3,8]

for angka in kumpulan_angka :
    print(f"angka = {angka}")

peserta = ["ringgo", "agus", "budi", "bambang", "asep"]

for nama in peserta :
    print(f"Nama = {nama}")

# for loop dan range
print("\nFor Loop dan Range")
kumpulan_angka = [11,22,43,65,73,80]
panjang = len(kumpulan_angka)

for i in range(panjang) :
    print(f"Angka = {kumpulan_angka[i]}")

# while loop
print("\nWhile Loop")

kumpulan_angka = [11,22,43,65,73,80]
panjang = len(kumpulan_angka)
i = 0

while i < panjang :
    print(f"Angka = {kumpulan_angka[i]}")
    i += 1

# list comrehension
print("\nList Comprehension")
data = ["Bambang", 1,4,6,"Budi"]

[print(f"Data = {i}") for i in data]

angka = [11,22,43,65,73,80]
angka_kuadrat = [i**2 for i in angka]
print(angka)
print(angka_kuadrat)

# enumerate
print("\nEnumerate")
data_list = ["Bambang", 1,4,6,"Budi"]

for index,data in enumerate(data_list) :
    print(f"Index = {index}, Data = {data}")



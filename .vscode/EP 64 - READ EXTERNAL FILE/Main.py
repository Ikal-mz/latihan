## membaca file external

print(3*"=", "Membaca file txt", 3*"=")
file = open("data.txt",mode="r")

# cek status bisa di baca
print(f"status read : {file.readable()}")
# cek status bisa di tulis
print(f"status write : {file.writable()}")

# baca seluruh file
print(file.read())

# baca perbaris
# print(file.readline(),end="") # baca baris pertama
# print(file.readline(),end="") # baca baris kedua

# baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sudah di close : {file.closed}")
file.close()
print(f"apakah file sudah di close : {file.closed}")


# salah teknik membuka file di python
print("\n",3*"=", "Membaca file txt dengan with", 3*"=")

with open("data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah di close : {file.closed}")

print(f"apakah file sudah di close : {file.closed}")





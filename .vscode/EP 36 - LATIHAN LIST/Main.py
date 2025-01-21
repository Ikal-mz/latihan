# program list buku


list_buku = []

while True :
    print("\nMasukan data buku")
    judul = input("Masukan judul buku\t: ")
    penulis = input("Masukan penulis buku\t: ")
    
    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    print("\n\n","=="*7,"Data buku","=="*7)
    for index,buku in enumerate (list_buku) :
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n\n","="*20)
    isLanjut = input("Apakah di lanjutkan?(y/n)")

    if isLanjut == "n" :
        break
print("Program Selesai")


    
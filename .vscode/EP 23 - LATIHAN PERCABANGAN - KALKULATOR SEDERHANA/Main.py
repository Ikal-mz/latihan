#KALKULATOR SEDERHANA

print(10*"=", "Kalkulator Sederhana", 10*"=","\n")

angka_pertama = float(input("Masukan angka Pertama : "))
operator = input("Masukan Operatot (+, -, *, /) : ")
angka_kedua = float(input("Masukan Angka Kedua : "))

if operator == "+" :
    hasil = angka_pertama + angka_kedua
    print("Hasil dari :", angka_pertama, "+", angka_kedua , "=", hasil)
elif operator == "-" :
    hasil = angka_pertama - angka_kedua
    print("Hasil dari :", angka_pertama, "-", angka_kedua , "=", hasil)
elif operator == "*" or operator == "x" :
    hasil = angka_pertama * angka_kedua
    print("Hasil dari :", angka_pertama, "*", angka_kedua , "=", hasil)
elif operator == "/" :
    hasil = angka_pertama / angka_kedua
    print("Hasil dari :", angka_pertama, "/", angka_kedua , "=", hasil)
else :
    print("Operator yang anda masukan salah !")
    
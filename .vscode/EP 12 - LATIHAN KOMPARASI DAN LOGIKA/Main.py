#latihan logika dan komparasi

#membuat gabungan area rentang dari angka

# kurang dari 3 atau lebih dari 10
inputUser = float(input("Masukan angka \nkurang dari 3 \natau \nlebih dari 10 \n: "))

#periksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3 = ", isKurangDari)

#periksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("lebih dari 10 = ", isLebihDari)

#logika pengecekan menggunakan or
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan: ", isCorrect)

# lebih dari 3 dan kurang dari 10
print("\n", 10*"=", "\n")
inputUser = float(input("Masukan angka \n lebih dari 3 \n dan \nkurang dari 10 \n: "))

#lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ", isLebihDari)

#kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 = ", isKurangDari)

#logika pengecekan menggunakan and
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukan = ", isCorrect)

#ada tugas di akhir

#masukan angka yg lebih dari 0 kurang dari 5 atau lebih dari 8 kurang dari 11
print("\n", 10*"=", "\n")
inputUser = float(input("Masukan angka \n lebih dari 0 dan kurang dari 5 \n atau \n lebih dari 8 kurang dari 11 \n: "))

#lebih dari 0 dan kurang dari 5
isLebihDari = inputUser > 0 and inputUser < 5
print("Lebih dari 0 dan kurang dari 5 = ", isLebihDari)

#lebih dari 8 dan kurang dari 11
isKurangDari = inputUser > 8 and inputUser < 11
print("Lebih dari 8 dan kurang dari 11 = ", isKurangDari)

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukan = ", isCorrect)

#masukan angka kurang dari 0 dan lebih dari 5 kurang dari 8 dan lebih dari 11
print("\n", 10*"=", "\n")
inputUser = float(input("Masukan angka \n kurang dari 0 \n atau \n lebih dari 5 kurang dari 8 \n atau \n lebih dari 11 \n : "))

#kurang dari 0
isKurangDari = inputUser < 0
print("Kurang dari 0 = ", isKurangDari)

#lebih dari 5 kurang dari 8
isRentang = inputUser > 5 and inputUser < 8
print("Lebih dari 5 dan kurang dari 8 = ", isRentang)

#lebih dari 11
isLebihDari = inputUser > 11
print("Lebih dari 11 = ", isLebihDari)


isCorrect = isKurangDari or isLebihDari or isRentang
print("Angka yang anda masukan = ", isCorrect)



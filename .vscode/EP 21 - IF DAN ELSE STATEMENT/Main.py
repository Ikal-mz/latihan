# if dan else statement

#1. if nya
#2. kondisinya
#3. aksinya

nama = input('Siapa nama anda? ')

"""program sebelumnya
if kondisi : aksi
program selanjutnya"""

# 1. program if inline
print("="*5,"If Inline",5*"=")
if nama=="budi" : print(f"Kamu terbaik {nama}")
print(f"Terima kasih {nama}")

#2. program if Indentation
print("\n","="*5,"If Indentation",5*"=")
if nama=='budi' :
    print(f'Kamu terbaik {nama}')
    print(f'Kamu keren {nama}')
print(f"Terima kasih {nama}")

#3. else statement
print("\n","="*5,"Else Statement",5*"=")
if nama=="riko" :
    print("Hai riko, kamu paling kece")
else:
    print(f"kamu tidak keren {nama}")
print("akhir dari program")

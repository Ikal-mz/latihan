data = "Ini adalah string"
print(data)
print(type(data))

#1. cara membuat string

'''
    1. dengan menggunakan single quote '.....'
    2. dengan menggunakan double quote "....."

'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan single quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("Ini adalah hari Jum'at")

#2. munggunakan tanda \

#membuat tanda ' menjadi string
print('Mari shalat jum\'at')
print('g\'day, isn\'t it?')

#backlash
print("C:\\user\\Ucup")
print("C:\\\\user\\\\Ucup")

#tab
print("Ucup Otong")
print("Ucup\tOtong, jadi jauh")

#backspace
print("ucup otong")
print("ucup \botong, jadi deketan")

#newline
print("Baris pertama.\nBaris kedua.") #LF -> line feed -> unix, macos, linux
print("Baris pertama.\rBaris kedua.") #CR -> carriage return -> commodore, acorn, lisp
print("Baris pertama.\r\nBaris kedua.") #CRLF -> line feed carriage return -> dipakai oleh windows

# 3. String literal atau raw

#hati-hati
print('C:\new folder') #akan salah patchnya

#menggunakan raw string
print(r'C:\new folder')

#multiline literal string
print("""
Nama    : ucup
Kelas   : 3 SD
""")

#multiline literal string dan raw
print(r"""
Nama    : ucup
Kelas   : 3 SD
Folder  : C:\new folder
""")




#format string

# contoh generic
# string
nama = "bambang"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f'boolean = {boolean}'
print(format_str)

# angka
angka = 11.11
format_str = f'angka = {angka}'
print(format_str)

#bilangan bulat
angka = 15
format_str = f'bilangan bulat = {angka:d}'
print(format_str)

#bilangan ribuan
angka = 20000
format_str = f'bilangan ribuan = {angka:,}'
print(format_str)

#bilangan desimal
angka = 11.1543
format_str = f"desimal = {angka:.3f}"
print(format_str)

#menampilkan leading zero
angka = 11.1543
format_str = f'desimal = {angka:7.3f}'
print(format_str)

angka = 11.1543
format_str = f'desimal = {angka:07.3f}'
print(format_str)

angka = 11.1543
format_str = f'desimal = {angka:09.3f}'
print(format_str)

#menampilkan tanda + dan -
angka_minus = -11
angka_plus = +11.1234
format_minus = f'minus = {angka_minus:+d}'
format_plus = f'plus = {angka_plus:+.3f}'

print(format_minus)
print(format_plus)

#menformat persen
persentase = 0.075
format_persen = f'persen = {persentase:.2%}'
print(format_persen)

#melakukan perasi aritmatika di dalam placeholder
harga = 11000
jumlah = 3

format_string = f'harga total = {harga*jumlah:,}'
print(format_string)

#format angka lain (binary, octal, hecadecimal)
angka = 255
format_binary = f'binary = {bin(angka)}'
format_octal = f'octal = {oct(angka)}'
format_hex = f'hex = {hex(angka)}'

print(format_binary)
print(format_octal)
print(format_hex)
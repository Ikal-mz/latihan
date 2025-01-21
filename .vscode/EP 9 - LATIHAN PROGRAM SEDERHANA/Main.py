#LATIHAN KONVERSI SATUAN TEMPERATURE

#program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR")

celcius = float(input('Masukan suhu dalam celcius : '))
print('suhu adalah', celcius, 'celcius')

#reamur
reamur = (4/5) * celcius
print('suhu dalam reamur adalah', reamur, 'reamur')

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print('suhu dalam fahrenheit adalah', fahrenheit, 'fahrenheit')

#kelvin
kelvin = celcius + 273
print('suhu kelvin adalah', kelvin, 'kelvin')

'''
RUMUS KONVERSI TEPERATUR

celcius -> reamur = (4/5) * celcius
        -> fahrenheit = ((9/5) * c) + 32
        -> kelvin = c + 273

reamur  -> celcius = (5/4) * reamur
        -> fahrenheit = ((9/4) * reamur) + 32
        -> kelvin = ((5/4) * reamur) + 273

fahrenheit  -> celcius = (5/9) * (fahrenheit - 32)
            -> reamur (4/9) * (fahrenheit -32)
            -> kelvin (tugas)???

kelvin  -> celcius = kelvin - 273
        -> reamur = (4/5) * (kelvin - 273)
        -> fahrenheit = (tugas)???
'''

#tugas konversi dari fahrenheit ke kelvin
#ubah dulu fahrenheit ke reamur -> reamur ke kelvin
#atau ubah fahrenheit ke celcius -> celcius ke kelvin

fahrenheit = float(input('Masukan suhu dalam fahrenheit : '))
print('suhu adalah ', fahrenheit, 'fahrenheit')

#ubah fahrenheit ke celciu -> celcius ke kelvin
celcius = (5/9) * (fahrenheit - 32)
kelvin = celcius + 273
print('suhu dalam kelvin adalah ', kelvin, 'kelvin')


#tugas konversi dari kelvin ke fahrenheit
#ubah dulu kelvin ke reamur -> reamur ke fahrenheit
#atau ubah kelvin ke celcius -> celcius ke fahrenheit
kelvin = float(input('Masukan suhu dalam kelvin : '))
print('suhu adalah ', kelvin, 'kelvin')

#ubah kelvin ke celcius -> celcius ke fahrenheit
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print('suhu dalam fahrenheit adalah ', fahrenheit, 'fahrenheit')


#operasi aritmatika

a = 11
b = 3

#operasi tambah
hasil = a+b
print(a, "+", b, "=", hasil)

#operasi kurang
hasil = a-b
print(a, "-", b, "=", hasil)

#operasi kali
hasil = a*b
print(a, "*", b, "=", hasil)

#operasi bagi
hasil = a/b
print(a, "/", b, "=", hasil)

#operasi eksponen (pangkat) **
hasil = a**b
print(a, "**", b, "=", hasil)

#operasi modulus (sisa pembagian) %
hasil = a%b
print(a, "%", b, "=", hasil)

#operasi floor division //
hasil = a//b
print(a, "//", b, "=", hasil)

#prioritas operasi, operational precedence
'''
    1. ()
    2. exponen **
    3. perkalian dan teman-temannya * / ** % //
    4. penjumlahan dan pengurangan + -
'''

x = 2
y = 3
z = 4

hasil = x ** y * z + x / y - y % z // x
print (x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x,"= ", hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=', hasil)

hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=', hasil)

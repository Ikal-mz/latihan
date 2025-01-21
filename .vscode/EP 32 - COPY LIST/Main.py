# teknik menduplikat list

a = ["riko", "hasim", "malik"]
print(f"data a = {a}")

b = a   # pass by reference
print(f"data b = {b}")

# kita akan merubah member dari a
# ini akan merubah kedua list
a[1] = "sepja"
b.sort()
print(f"data a = {a}")
print(f"data b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikasi list dengan copy
print(f"\nmembuat list c dengan a.copy()")
c = a.copy()    # full duplikat

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"kita ubah data c index ke 0")
c[0] = "mifta"

print(f"data a = {a}")
print(f"data b = {b}")
print(f"data c = {c}")

print(f"kita ubah data a index ke 2")
a[2] = "jeju"

print(f"data a = {a}")
print(f"data b = {b}")
print(f"data c = {c}")
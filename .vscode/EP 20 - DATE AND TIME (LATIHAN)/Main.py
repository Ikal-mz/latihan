#date and time (latihan)

import datetime as dt

print("Silakan masukan tanggal, \nbulan dan tahun lahir anda")

tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan   : "))
tahun = int(input("tahun   : "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Harinya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
umur_tanggal = (umur_hari.days % 365) % 30

print(f"umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan, {umur_tanggal} hari")
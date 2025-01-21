
import datetime

mahasiswa1 = {
    'nama' : 'budi muhem',
    'nim' : '1245618090',
    'sks' : 130,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2000,8,10)
}

mahasiswa2 = {
    'nama' : 'bambang sentosa',
    'nim' : '1245618091',
    'sks' : 135,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2001,2,12)
}

mahasiswa3 = {
    'nama' : 'yosep hamidun',
    'nim' : '1245618092',
    'sks' : 140,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2001,2,10)
}

data_mahasiswa = {
    "key1" :  mahasiswa1,
    "key2" :  mahasiswa2,
    "key3" :  mahasiswa3,
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*45)

for mahasiswa in data_mahasiswa :
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
    



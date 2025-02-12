# 1. mode write 
# dia akan membuat file baru jika tidak ada, 
# lalu menimpa atau overwrite isinya

with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("Budi Sutoso Sijuntak")

with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("timpah")

# 2. mode append
with open("data_2.txt","w",encoding="utf-8") as file:
    file.write("Budi Sutoso Sijuntakn\n")

with open("data_2.txt","a",encoding="utf-8") as file:
    file.write("append")

# 3. mode r+
with open("data_3.txt","w",encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data_3.txt","r+",encoding="utf-8") as file:
    file.write("baris-1\n")
    file.write("baris-2\n")
    file.write("baris-3\n")

with open("data_3.txt","r+",encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt","r+",encoding="utf-8") as file:
    file.write("Budi Susanto") # menimpah isi text sesuai dengan panjan data




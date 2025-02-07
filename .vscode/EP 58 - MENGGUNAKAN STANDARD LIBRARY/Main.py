import datetime


data_waktu = datetime.datetime.now()
print(f"datetime now {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"hari dengan format : {data_waktu.strftime('%A')}")

from collections import Counter
data = ["a","b","c","d","d","c","c","d","b","c"]

data_count = Counter(data)
print(data_count)

print(f"data a : {data_count['a']}")
print(f"data b : {data_count['b']}")
print(f"data c : {data_count['c']}")
print(f"data d : {data_count['d']}")

import io

file = io.open("file.txt","r")
print(file.read())



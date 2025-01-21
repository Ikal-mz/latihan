# looping dictonary

teman_teman = {
    "bud" : "budi laksono",
    "met" : "mamat emet",
    "bam" : "bambang sukijo",
    "ris" : "risal sahbandar"
}

# looping firs try (yang keluar keynya)
for teman in teman_teman :
    print(teman)

# operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys() :
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for val in teman_teman.values() : 
    print(val)

items = teman_teman.items()
print(items)

for item in teman_teman.items() :
    print(item)

for key,val in teman_teman.items() :
    print(f"key : {key}, value : {val}")

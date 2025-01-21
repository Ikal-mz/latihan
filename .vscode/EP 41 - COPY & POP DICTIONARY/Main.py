# copy dictonary

teman_teman = {
    "man" : "maman suratman",
    "min" : "mimin suritmin",
    "mon" : "temon suritmon",
    "sem" : "semonceli",
    "sur" : "mansur widodo"
}

friends = teman_teman.copy()

print(f"teman-teman : {teman_teman}\n")
print(f"freinds : {friends}\n")

teman_teman["min"] = "mimin muhaimin"
print(f"teman-teman : {teman_teman}\n")
print(f"freinds : {friends}\n")

# pop dictonary (berkasarkan key)
dataMansur = friends.pop("sur")
print(f"data mansur : {dataMansur}\n")
print(f"freinds : {friends}\n")

# popitem dictonary (data terakhir)
dataTerakhir = friends.popitem()
print(f"data terakhir : {dataTerakhir}\n")
print(f"freinds : {friends}\n")



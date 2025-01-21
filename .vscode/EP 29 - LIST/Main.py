#--LIST

#kumpulan data numbers
data_angka = [1,4,2,3]
print(data_angka)

#kumpulan data sting
data_string = ["bambang", "budi", "ringo"]
print(data_string)

#kumpulan data boolean
data_boolean = [True, False, False, False, True]
print(data_boolean)

#kumpulan data campuran
data_campuran = [1, "jhonshon", 2, True, "Zilong", False]
print(data_campuran)

#cara alternatif membuat list
data_range = range(0,11,2) #range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

#membuat list dengan for loop, list comprehension
list_pake_for = [i**3 for i in range(0,10)]
print(list_pake_for)

#membuat list pake for dan if
list_for_if = [i for i in range(0,11) if i != 7]
print(list_for_if)

#membuat list pake for dan if (nilai genap)
list_for_if = [i for i in range(0,11) if i%2 == 0]
print(list_for_if)
               
#membuat list pake for dan if (nilai ganjil)
list_for_if = [i for i in range(0,11) if i%2 == 1]
print(list_for_if)
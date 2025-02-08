import numpy as np

list_a = [1,2,3,4,]
vektor_a = np.array([1,2,3,4])

print(f"ini adalah list a : {list_a}")
# print(list_a**2)    <- ini akan gagal
print(f"ini adalah vektor a : {vektor_a}")
print(f"vektor a di pangkatkan 2 : {vektor_a**2}")
print(f"vektor a di kalikan 6 : {vektor_a*6}")

matrix_b = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(f"matrix_b : \n{matrix_b}")
print(f"matrix_b di pangkatkan 2 : \n{matrix_b**2}")

zeros_c = np.zeros((3,3))
print(f"zeros c : \n{zeros_c}")

ones_d = np.ones((3,3))
print(f"ones d : \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah : \n{jumlah}")

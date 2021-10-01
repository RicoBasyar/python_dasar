from random import choice

# Tiga tipe angka 

i = 20
j = 20.5
k = 20j

print(type(i))
print(type(j))
print(type(k))
print("\n")

# Konversi

float_to_int = int(j)
int_to_float = float(i)


print(float_to_int, type(float_to_int))
print(int_to_float, type(int_to_float))


# Fungsi nomor acak

list_buah = ["Apel", "Mangga", "Anggur", "Jambu"]
tuple_angka = (1,3,5,6,8,3,2)

print(choice(list_buah))
print(choice(tuple_angka))

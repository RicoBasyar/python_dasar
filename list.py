# List

list1 = ["Ozzi","Kawe","Rico"]
list2 = [1,2,3,4,5,6]
list3 = [1,2,"ozzi","kawe",4,5,6,"Rico"]

print(list1[2])
print(list3[:3])
print(list2[4])

# Update nilai list
list2[2] = 9
print(list2)

# Tambah nilai list
list2.append(3)
print(list2)

list2.insert(3, 12)
print(list2,"\n")

# Operasi dasar list
print(len(list2))
print(list2 + list1)
print(list1 * 4)
print("Ilham" in list1)

for x in list1:
    if (x == "ilham"):
        print("ada ilham\n")
    else:
        print("Tidak ada ilham\n")

# Indexing, Slicing, Matrix Pada list

list4 = ['Java', 'Python', 'C++']
print(list4[1])
print(list4[-1])
print(list4[1:],"\n")

# Fungsi Build-in List
print(len(list4))
print(max(list4))
print(min(list4))

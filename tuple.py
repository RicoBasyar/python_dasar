# Tuple
tuple1 = ("Apel","Anggur","Mangga","Semangka","Melon")
tuple2 = ()

print(tuple1[1:3])

# Update Tuple
tuple3 = tuple1 + ("Jeruk", "Lemon")
print(tuple3)
#------------------ATAU--------------------#
list1 = list(tuple1)
list1.append("Jeruk")
tuple1 = tuple(list1)
print(tuple1)


# Delete Tuple
del tuple3
print(tuple3)





number = 9

# KONDISI IF
if(number == 9):
    print("Angka 9")

if(10>5):
    print("Sepuluh lebih besar dari 5 \n")

# Kondisi IF ELSE
if(number<10):
    print("Lebih kecil dari 10\n")
else:
    print("lebih besar dari 10\n")


# Kondisi ELIF

hari = "Minggu"

if(hari == "Senin"):
    print("Kerja")
elif(hari == "Selasa"):
    print("Kerja")
elif(hari == "Rabu"):
    print("Kerja")
elif(hari == "Kamis"):
    print("Kerja")
elif(hari == "Jumat"):
    print("Kerja")
elif(hari == "Sabtu"):
    print("Libur")
elif(hari == "Minggu"):
    print("Libur")

# While Loop

count = 0

while(count<10):
    print("count = ", count)
    count += 1

print("Selesai", count)


# FOR LOOP
# Contoh sederhana
angka = [1,2,3,4,5,6,7,8]
for j in angka:
    print(j)

# Contoh lagi
makanan = ["Apel", "Anggur", "Mangga", "Jeruk"]
for x in makanan[:3]:
    print(x)

# NESTED LOOP
i = 2
while(i<100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j += 1
    if(j > i/j): print(i, "Bilangan prima")
    i += 1




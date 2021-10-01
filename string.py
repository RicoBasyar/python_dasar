# String Sederhana
print("Hello World!"[3:10])

nama = "Rico Basyar"
message = "Hello World"
print("Nama Depan \t:", nama[:4], "\nPesan \t\t:", message[1:5])

# Mengupdate String
print(message[:5] + "Python")

# String dengan operator logic
if("a" not in message.lower()):
    print("Tidak ada huruf a")
else:
    print("ada huruf a")

# Format
x = 30
print("Hello %s" % (nama[:4]))
print("Tiga puluh : %d" % (x))

# Triple Quote
kutipantiga = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (kutipantiga)

# String Unicode
kata = "halo"
print(kata.capitalize())
print(kata.isalnum())
print(kata.isalpha())
print(kata.isdigit())
print(kata.islower())
print(kata.isnumeric())
print(kata.isspace())

print("\nPenggunaan Continue pada Looping")
print("--------------------\n")
a = 0
b = float(input("masukan angka anda : "))
while a < b: # a < b adalah syarat
    a += 1 # Increment
    if a == 5: # seleksi kondisi
        continue # Continue point
    print(a)
print("\nPenggunaan if else dalam looping")
print("--------------------\n")
a = 0
b = float(input("Masukan angka anda : "))
while a < b:
    if a == (b - 1):
        print("Perulangan berenti")
        break;
    else:
        print("Perulangan ke - ", a)
        a +=1
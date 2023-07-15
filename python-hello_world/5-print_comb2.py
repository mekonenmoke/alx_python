# To print number 00 to 99 in two digit
for num in range(15):
    print(f"{num:02d}", end=", " if num != 14 else "\n")

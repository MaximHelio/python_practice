for ㅣ in range(1, 9):
    print("***********", end="\t")
print(" ")

for m in range(2, 10):
    print("    %d단    " %(m), end="\t")
print(" ")

for n in range(1, 9):
    print("***********", end="\t")

print(" ")

for b in range(1, 10):
    for a in range(2, 10):
        print("%d * %d = %d" %(a, b, a*b), end="\t")
    print(" ")

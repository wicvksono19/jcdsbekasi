n = int(input('masukan angka '))

for i in range(1, n+1):
    for j in range(1,n-i+1):
        print("_", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("#", end="_")
        else:
            print("_", end="")
    print()
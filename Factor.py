x=int(input("enter any num \n"))

print("the factor of", x, "are:")

for i in range(1, x+1):
    if x % i == 0:
        print(i,"even number")
    else:
        print(i, "odd number")
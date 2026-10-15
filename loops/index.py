n =5
factorial=1

for i in range(n, 0, -1):
    factorial *= i

print("The factorial of", n, "is:", factorial)

a,b=48,18
while b!=0:
    a,b = b, a%b

print("The GCD is:", a)


for i in range (1,2) : 
        for j in range (1,11):
             print(i, "x", j, "=", i*j)



for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row * col:4d}", end="")
    print() 
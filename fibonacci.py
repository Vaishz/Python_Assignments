f0=0
f1=1
n=int(input("Enter number of terms: "))
for i in range (1,n):
    f=f0+f1
    print(f, end=",")
    f0=f1
    f1=f

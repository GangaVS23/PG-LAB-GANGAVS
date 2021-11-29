s=int(input("Enter start year:"))
e=int(input("Enter end year:"))
if(s<e):
    print("Leap years are:",end=" ")
for i in range(s,e):
    if (i%4==0) or (i % 100 !=0) and (i%4==0):
        print(i,end=" ")
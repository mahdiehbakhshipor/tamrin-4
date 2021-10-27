m = int (input("m : "))
n = int (input("n : "))
for i in range(m):
    if(i%2==0):
        ch1="#"
        ch2="*"
    else:
        ch1="*"
        ch2="#"
    for j in range(int(n/2)):
        print(ch1,ch2,end=" ")
    print()
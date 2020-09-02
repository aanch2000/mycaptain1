num = int(input("Enter a number..."))
count = 0
print("Fibonacci series upto ",num,": \n")
p1=0
p2=1
if num==0:
    print(p1)
elif num==1:
    print(p1,"\n",p2)
else:
    while count<num:
        print(p1)
        p=p1+p2
        p1=p2
        p2=p
        count+=1

def sum(a,b):
    return a+b



def avg(a,b):
    return (a,b)/2



def ams(a):
    n=int(input("Enter the number\n"))
    sum=0
    order=len(str(n))
    t=n
    while(n>0):
        sum+=(n%10) **order
        n=n/10

    if(sum==n):
        print("yes")
        return true
    else :
        print("No")
        return false    






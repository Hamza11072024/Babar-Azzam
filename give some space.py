def sum(N):
    return N*(N+1)/2

def array_sum(a):
    sum=0
    for i in a:
        sum=sum+i
    return(sum)

a=[1,11,22,23]

array_sum(a)

def sum1(n):
    if(n<=0):
        return
    return n+sum1(n-1)

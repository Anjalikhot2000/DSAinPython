#using recursion
def gcd(m,n):
    if m<n:
        (m,n)=(n,m) #kind of swapping
    if m%n==0:
        return n
    else:
        return(gcd(n,m-n))
print(gcd(14,63))
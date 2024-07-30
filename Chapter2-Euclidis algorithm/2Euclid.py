#another way 
def gcd(m,n):
    if m<n:
        (m,n)=(n,m) #kind of swapping
    if m%n==0:
        return n
    else:
        diff=m-n
        return(gcd(max(n,diff),min(n,diff)))
print(gcd(14,63))
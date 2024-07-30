#done using while loop
def gcd(m,n):
    if (m<n):
        (m,n)=(n,m)
    while (m%n)!=0:
        diff=m-n
        (m,n)=(max(diff,n),min(diff,n))
    return (n)
print(gcd(14,63))
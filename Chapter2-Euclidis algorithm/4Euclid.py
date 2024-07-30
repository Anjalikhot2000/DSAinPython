#As the m=ad, n=bd(where d is the common divisor of m and n), if this happens the remainder, r=m%n can be also r=cd
def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if m%n==0:
        return n
    else:
        return(gcd(n,m%n))
print(gcd(12,8))
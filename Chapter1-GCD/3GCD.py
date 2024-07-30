#As seen in above example we can reduce the time complexity by using min() in for loop instead of max()
a=12
b=8
cf=[]
for i in range(1,min(a,b)+1):
    if (a%i==0) and (b%i==0):
        cf.append(i)
print(cf)
print(max(cf))
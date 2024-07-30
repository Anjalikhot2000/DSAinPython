#to shorten the line of code done in 1GCD.py
a=12
b=8
cf=[]
for i in range(1,max(a,b)+1):
    if (a%i==0) and (b%i==0):
        cf.append(i)
print(cf)
print(max(cf))
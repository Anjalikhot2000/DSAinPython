#to find GCD
a=8
b=12
fa=[]
for i in range(1,a+1):
    if (a%i==0):
        fa.append(i)
fb=[]
for i in range(1,b+1):
    if (b%i==0):
        fb.append(i)
cf=[]
for i in fa:
    if i in fb:
        cf.append(i)
print(max(cf))
#Bool- True and False
#We generate boolean values during comparisons
x=5
y=2
print(x==y) #False
print(x>y) #True
print(x<y) # False
print(x!=y) #True


#Combining logical operators
print(x>0 and x%y!=0) #True
#lets take an example
def divides(m,n):  #used function- function def
    if m%n==0:
        return (True)
    else:
        return(False)
print(divides(2,3)) #False  #calling function
print(divides(4,2)) #True
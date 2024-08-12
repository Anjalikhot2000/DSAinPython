#Type string,str, a sequence of characters
#Encloses in single,double and triple quotes

#single quotes
city="Chennai"
print(city)

#double quotes
title="Anjali's mob is one plus"
print(title)

#triple quotes
dialogue='''He said his fav book is "Sita the warrior"'''
print(dialogue)

#reverse in string
for i in range(-1,-(len(city)+1),-1):
    print(city[i])

#concatination
s="hello"
t="there"
print(s+t)
t=" there"
print(s+t)

#Extract substring using slicing
s="hello"
print(s[1:4]) #Output: ell
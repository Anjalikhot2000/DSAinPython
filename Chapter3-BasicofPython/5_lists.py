#sequence of values but type not need to be uniform
#containing elements which are of heterogenous data types
#ordered- mutable
#can contain duplicate values
#can be created using list() or []
#can be created using dict.keys() or dict.values() or dict.items()

li=[1,2,"hi",2.5]
print(li)

#lists can contain list within list
#lists can be nested within each other  

nested=[[2,37],4,["hello"]]
print(nested[0]) #output:[2,37]
print(nested[1]) #output:4
print(nested[2]) #output:["hello"]
print(nested[2][0][3]) #output:l
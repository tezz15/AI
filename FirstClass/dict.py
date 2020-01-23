#Graph is represented in dictionary.
a = {1:'January',2:"February",3:"March",4:"April",5:"May"}
for key,values in a.items(): #creates set
    print(key,values)

b = {value:key for key,value in a.items()}
print(b)
print(b['January'])
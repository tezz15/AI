'''
a = []
a.append("hello")
a.append(1)
a.append(2.3)
print(a)
'''
a = ['Ram', 'Shyam',2,3,5.1]
for i in a:
    print(i)
x = a.pop(2)
print(a)
print("Deleted item:", x)

print(a)
del a[0]
print("New list:",a)
a=(1,3,4,6,7,1,1,3,3,3,4,5,2,1,1)
print(a.count(1))
print(a.index(3))
#How to update Tuple
#To update a tuple first we change it into a list then 
# we update it and again change it into a Tuple
x=("cherry","Banana","Papaya")
print(x)
y= list(x)
y[1] = "Kiwi"
x = tuple(y)
print(x)
# Join two tuple
tuple1 = ("a","b","c")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)
#Multiply Tuple
fruits = ("Apple","Banana","Cherry")
# fruits = (2,4,6)
# fruits = ("A","b")
mytuple = fruits * 3
print(mytuple)

t= [0,1,2,3]
t[2:]
t[2:].append(t[0])
print(t)
a = ["pn",123,True,20.5,"Gwalior",123]
b=a[2:]
print(b)
b = b + (8,9,"h")
print(b)
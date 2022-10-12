#implicit type conversion
x = 10
  
print("x is of type:",type(x))
  
y = 10.6
print("y is of type:",type(y))
  
z = x + y
  
print(z)
print("z is of type:",type(z))

#Explicit type conversion
# using  tuple(), set(), list()
s = 'geeks'
  
# printing string converting to tuple
c = tuple(s)
print ("After converting string to tuple : ",end="")
print (c)
  
# printing string converting to set
c = set(s)
print ("After converting string to set : ",end="")
print (c)
  
# printing string converting to list
c = list(s)
print ("After converting string to list : ",end="")
print (c) 
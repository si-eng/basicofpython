#if else statment 
i = 10
  
if (i > 15):
    print("10 is less than 15")
else:    
    print("I am Not in if")

#Nested if 
i = 10
if (i == 10):
    
    #  First if statement
    if (i < 15):
        print("i is smaller than 15")
          
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
          
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

#elif ladder
i = 20
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")

#for loop
s = "apple"
for i in s:
    print(i)

#continue statment
for words in "sakshi sharma":
    if words=="a" or words=="s":
        continue
    print("current word",words)

#break
for words in "sakshi sharma":
    if words=="a" or words=="s":
        break
    print("current word",words)


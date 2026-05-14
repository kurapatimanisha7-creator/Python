#if statement=a block of code that will execute if its condition is true

age=int(input("how old are you?: "))
if age>18:
    print("you are an adult")
elif age<0:
    print("you have not even born yet!")
else:
    print("you are a child")
# return statement =function send python values/oobjects back to the caller
#                   these values/objects are known as the functions return value

def sum(num1,num2):
    sum=num1+num2
    return sum  # return statement will end the function and send the result back to the caller
    
#sum(5,6) # we are not storing the return value in a variable so it will not be printed
result=sum(5,6) # we are storing the return value in a variable so it will be printed
print(result)
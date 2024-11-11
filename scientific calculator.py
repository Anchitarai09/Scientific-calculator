import math

print( "------perform calculation--------- ")
# here we create function
def scientific_calculator(operation , *args):
  # addition  
    if operation == '+' or operation == 'add':
        return sum(args)
 # subtraction
    elif operation == '-' or operation == 'subtract':
        return args[0] - args[1]
 # multiplication
    elif operation == '*' or operation == 'multiply':
        mul = 1
        for i in args:
            mul *= i
        return mul  
 # division
    elif operation == '/' or operation == 'division':
        if args[1] == 0:
            return "ZeroDivisionError: division by zero"  # Handle division by zero
        return args[0] / args[1]
 # power
    elif operation == '**' or operation == 'power':
        return args[0]**args[1]  ## if args[0]/args[1] i.e 2(base)**3(exponent) o/p is 8else
    else:
        return "you enter something wrong please check it"
    
def scientific_cal(operation , num):
    if operation == 'square':
        return num**2
    elif operation == 'square root':
        return math.sqrt(num)
    elif operation == 'percentage':
        return num/100
    elif operation == 'logarithm':
        return math.log10(num)
    elif operation == 'sin':
        return math.sin(math.radians(num))
    elif operation == 'cos':
        return math.cos(math.radians(num))
    elif operation == 'tan':
        return math.tan(math.radians(num))
    elif operation == 'factorial':
        return math.factorial(int(num))
    elif operation == 'exponential':
        return math.exp(num)
    else:
        return "you enter something wrong please check it"

def valid_operation(operation):
    valid_operations = ['+', 'add', '-', 'subtract', '*', 'multiply', '/', 'division', '**', 'power',
                        'square', 'square root', 'percentage', 'logarithm', 
                        'sin', 'cos', 'tan', 'factorial', 'exponential']
    return operation in valid_operations        
    
# now we call our function for Two or Three Input   
a=int(input("Enter number 1st : "))
b=int(input("Enter number 2nd : "))    
operation = input("enter operation: ")
# if else condition
if not valid_operation(operation):
    print("error:Invalid operation.Please check your input")
else :
    result=scientific_calculator(operation , a,b)
    print(f"The result of {a} {operation} {b} is: {result}")

# here we call our function for Single Input
num1=int(input("enter number : "))
opera= input("Enter operation : ")
# if-else condition
if not valid_operation(operation):
    print("error:Invalid operation.Please check your input")
else:    
    result_1=scientific_cal(opera,num1) # 4 is angle
    print(f"The result of the operation '{opera}' on {num1} is : {result_1}")

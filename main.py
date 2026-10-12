
num1 = float(input("Give first number: "))

num2 = float(input("Give second number: "))

print("Choose an operation")
print ("1 - Addition")
print ("2 - Subtraction")
print ("3 - Multiplication")
print ("4 - Division")

operation = int(input("Choose your operation: "))

def add1 (num1, num2):
    return num1 + num2

def subtract2 (num1, num2):
    return num1 - num2
    
def multiplication3 (num1, num2):
    return num1*num2
    
def division4 (num1, num2):
    return num1/num2

if operation == 1:
    result = add1(num1, num2)
    print("Addition = ", result)

elif operation == 2:
    result = subtract2(num1, num2)
    print("Subtraction =", result)
    
elif operation == 3:
    result = multiplication3(num1, num2)
    print("Multiplication =", result)
    
elif operation == 4:
    result = division4(num1, num2)
    print("Division =", result)
    
    
    
    
    
    
    
    
    
    
    
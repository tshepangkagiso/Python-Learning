# Create a simple calculator that takes two numbers and an operation (+, -, *, /) as input from the user, performs the operation, and prints the result
    
def IsNumber(value1, value2):
    return isinstance(value1, int) and isinstance(value2, int)

def Switch(operand, value1, value2):
    if IsNumber(value1, value2):
        if operand == "+" :
            return value1 + value2
        
        elif operand == "-":
            return value1 - value2
        
        elif operand == "/":
            if value2 == 0:
                return None
            return value1 / value2
        
        elif operand == "*":
            return value1 * value2
        
        elif operand == "%":
            return value1 % value2
        else:
            return None

def Calculate():
    num1 = int(input("Enter 1st num: ") )
    operator = input("Enter operator(+, -, /, *, %): ")
    num2 = int(input("Enter second num: ") )
    result = Switch(operator, num1, num2)

    if result is not None:
        return f"{num1} {operator} {num2} = {result}"
    else:
        return False
    
output = Calculate()

if output == False:
    print("something is wrong, check if its numbers or real operands")
else:
    print(output)
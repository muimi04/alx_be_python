def perform_operations(num1,num2,operations):
    if operations == 'add':
        return num1 + num2 
    elif operations == 'subtract':
        return num1 - num2
    elif operations == 'multiply':
        return num1 * num2
    elif operations == 'division':
        if 2 == 0 :
            return "error can not divide by zero."
        return num1 / num2
    else:
        return "error. invalid operations."

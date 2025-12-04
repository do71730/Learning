'''Takes two numbers and return the sum'''
def additon(num1,num2):
    result = 0
    try: 
        result = num1 + num2
    except:
        result = "Error"
    return result

'''Takes two numbers and return the difference'''
def subtraction(num1,num2):
    result = 0
    try: 
        result = num1 - num2
    except:
        result = "Error"
    return result

'''Takes two numbers and return the quotient'''
def division(num1,num2):
    result = 0
    try: 
        result = num1 / num2
    except:
        result = "Error"
    return result

'''Takes two numbers and return the product'''
def multiply(num1,num2):
    result = 0
    try: 
        result = num1 * num2
    except:
        result = "Error"
    return result

'''Takes two numbers and return the power'''
def power(num1,num2):
    result = 0
    try: 
        result = num1 ** num2
    except:
        result = "Error"
    return result

'''Takes two numbers and return the reminder'''
def mod(num1, num2):
    result = 0
    try: 
        result = num1 % num2
    except:
        result = "Error"
    return result

'''Start the calculator and runs until the user inputs x'''
def main():
    n= 'o'
    while n != 'x':
        num1 = 0
        num2 = 0
        opp = '+'
        print('enter x at any time to stop: ')
        num1 = input("What is the first number: ")
        if num1 != 'x':
            num1 = int(num1)
            opp = input("chose and operation: /,+,-,*,**(power),%(modulus): ")
            if opp != 'x':
                num2 = input("what is the second number: ")
                if num2 != 'x':
                    num2 = int(num2)
                else: 
                    n= 'x'
            else:
                n ='x'
        else: 
            n = 'x'
        
        if n != 'x':
            if(opp == '/'): 
                print(division(num1,num2))
            elif(opp == '*'):
                print(multiply(num1,num2))
            elif(opp == '**'):
                print(power(num1,num2))
            elif(opp == '-'):
                print(subtraction(num1,num2))
            elif(opp == '%'):
                print(mod(num1,num2))
            elif(opp == '+'):
                print(additon(num1,num2))
            else:
                print('Wrong operation')
        else:
            print('Goodbye!')

'''Program begins by calling main'''
if __name__ == '__main__':
    main()
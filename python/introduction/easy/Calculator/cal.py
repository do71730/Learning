def additon(num1,num2):
    result = 0
    try: 
        result = num1 + num2
    except:
        result = "Error"
    return result

def subtraction(num1,num2):
    result = 0
    try: 
        result = num1 - num2
    except:
        result = "Error"
    return result

def division(num1,num2):
    result = 0
    try: 
        result = num1 / num2
    except:
        result = "Error"
    return result

def multiply(num1,num2):
    result = 0
    try: 
        result = num1 * num2
    except:
        result = "Error"
    return result

def power(num1,num2):
    result = 0
    try: 
        result = num1 ** num2
    except:
        result = "Error"
    return result

def mod(num1, num2):
    result = 0
    try: 
        result = num1 % num2
    except:
        result = "Error"
    return result

def main():
    num1 = int(input("What is the first number: "))
    opp = input("chose and operation: /,+,-,*,**(power),%(modulus): ")
    num2 = int(input("what is the second number: "))

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

if __name__ == '__main__':
    main()
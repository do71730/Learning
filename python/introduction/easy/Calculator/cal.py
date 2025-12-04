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

if __name__ == '__main__':
    main()
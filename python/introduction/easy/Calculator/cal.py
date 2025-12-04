def additon(num1,num2):
    return num1 + num2

def subtraction(num1,num2):
    return num1 - num2

def division(num1,num2):
    return num1 / num2

def multiply(num1,num2):
    return num1 * num2

def power(num1,num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2

def main():
    num1 = input("What is the first number: ")
    opp = input("chose and operation: /,+,-,*,**(power),%(modulus): ")
    num2 = input("what is the second number: ")

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
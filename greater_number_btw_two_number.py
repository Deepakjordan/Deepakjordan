def main():
    num1=int(input("enter the number:"))
    num2=int(input("enter the another number:"))
    greater_num= greater(num1,num2)

def greater(num1,num2):
    if num1>num2:
        print(f'{num1} is greater than {num2}')
    elif num2>num1:
        print(f'{num2} is greater than {num1}')
    else:
        print(f'both are same')

main()                    
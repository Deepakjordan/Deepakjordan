#num=int(input("enter a number:"))
#fac=1
#while (num>0):
#    fac=fac*num
#    num=num-1
#print("factorial=",fac)    


def main():
    num=int(input("enter a number:"))
    res=factorial(num)
    display(res,num)

def factorial(num):
    factorial=1
    while (num>0):
        factorial=factorial*num
        num=num-1
    return factorial

def display(res,num):
    print(f'{num}! = {res}')   

main()         
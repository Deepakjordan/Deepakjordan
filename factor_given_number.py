num=int(input('enter a number:'))
for i in range (1,num+1):
    if num%i==0:
        print(i)


def main():
    num=int(input("enter a number:"))
    factor= factor_of(num)
    display(num,factor)

def factor_of(num):
    for i in range (1,num+1):
        if num%i==0:
            return i

def display(num,factor):
    print(f'the {num} factors are {factor}')                        
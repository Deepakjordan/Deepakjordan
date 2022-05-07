def main():
    num = int(input("enter a number:"))
    res= reminder(num)
    display(num,res)

def reminder(num):
    return num%2

def display(num,res):
    if res==0:
        print(f'it is even number')      
    else:
        print(f'it is not even')     

main()        
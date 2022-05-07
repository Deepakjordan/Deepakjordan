def main():
    l=int(input("enter the len:"))
    b=int(input("enter the ber:"))
    area_of= area(l,b)
    perimeter_of= perimeter(l,b)
    display(area_of,perimeter_of,l,b)

def area(l,b):
    return l*b 

def perimeter(l,b):
    return 2*(l+b)

def display(area_of,perimeter_of,l,b):
    print(f'the {l} and {b} of rectangle is {area_of=},{perimeter_of=}')   

main()         


  
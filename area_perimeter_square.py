def main():
    n = int(input("enter a side value:"))
    area_of= area(n)
    perimeter_of= perimeter(n)
    display(area_of,perimeter_of,n)

def area(n):
    return n*n 

def perimeter(n):
    return 4*n

def display(area_of,perimeter_of,n):
    print(f'the side of square {n} than the area is {area_of}  ')
    print(f'the side of square {n} than the perimeter is {perimeter_of} ')     

main()          
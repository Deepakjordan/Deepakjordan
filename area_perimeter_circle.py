def main():
    radius=int(input("enter the radius:"))
    display(area(radius),perimeter(radius),radius)

def area(radius):
    return 22/7 * radius * radius

def perimeter(radius):
    return 2 * 22/7 * radius       

def display(area,perimeter,radius):
    print(f'the area of circle of {radius=} is {area}')
    print(f'the perimeter of circle of {radius=} is {perimeter}')  

main()    
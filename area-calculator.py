print('Area Calculator')



print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
print("4. Square")
print('5. Exit')

imput = int(input('What shape would you like to calculate the area for? '))

if imput == 5:
    print('Exiting the program.')

elif imput == 1:
    radius = float(input('Enter the radius of the circle: '))
    area = 3.14159 * radius * radius
    print(f'The area of the circle is {area}')
elif imput == 2:
    length = float(input('Enter the length of the rectangle: '))
    width = float(input('Enter the width of the rectangle: '))
    area = length * width
    print(f'The area of the rectangle is {area}')
elif imput == 3:
    base = float(input('Enter the base of the triangle: '))
    height = float(input('Enter the height of the triangle: '))
    area = 0.5 * base * height
    print(f'The area of the triangle is {area}')
elif imput == 4:
    side = float(input('Enter the side length of the square: '))
    area = side * side
    print(f'The area of the square is {area}')

          
a = float(input("Enter the first side of a triangle: "))
b = float(input("Enter the second side of a triangle: "))
c = float(input("Enter the third side of a triangle: "))
c1 = c**2
a1 = a**2
b1 = b**2

if c1 == a1 + b1:
    print("Triangle is rectangular")
else:
    print("Triangle is not rectangular")
a, b, c = input('Ведите 3 стороны треугольника: ').split(' ')

p = (float(a) + float(b) + float(c)) / 2

S = (p * (p - float(a)) * (p - float(b)) * (p - float(c))) ** 0.5

print(S)




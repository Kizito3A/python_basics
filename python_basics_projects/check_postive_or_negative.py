a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

S = (a + b + c)/2

area  = (S(S-a)*(S-b)*(S-c)) ** 0.5

print("The area of the triangle is %0.2f" %area)

print("Welcome :)")
a = input("Please write. Are you trying to identify a triangle or a quadrilateral?:")
if a == "triangle":
    print("please write the three sides lengths of the triangle: ")
    b = int(input("First side length:"))
    c = int(input("Second side length:"))
    d = int(input("Third side length:"))
    if (abs(d - b) >= c >= d + b) and (abs(c - d) >= b >= d + c) and (abs(b - c) >= d >= b + c):
        if b == c == d:
            print("This an equilateral  triangle.")
        elif d == b != c:
            print("This is an isosceles triangle.")
        elif d == b != c:
            print("This is an isosceles triangle.")
        elif d == c != b:
            print("This is an isosceles triangle.")
        elif b == c != d:
            print("This is an isosceles triangle.")
        elif d != b and b != c and d != c:
            print("This is an scalene triangle.")
    else:
        print("The side lengths you provided can not belong to a triangle.")
if a == "quadrilateral":
    print("please write the four sides lengths af the quadrilateral")
    f = int(input("First side length:"))
    v = int(input("Second side length:"))
    z = int(input("Third side length:"))
    y = int(input("Fourth side length:"))
    if f == v == z == y:
        print("This is a square.")
    elif (f == z == y != v) or (f == z == v != y) or (f == v == y != z) or (z == v == y != f):
        print("ERROR")
    elif (f == v and z == y) or (f == z and v == y) or (f == y and z == v) or (v == z and z == f) or (v == y and f != z) or (z == y and f == v):
        print("This a rectangle")
    elif f != v != z != y:
        print("This is a quadrilateral.")

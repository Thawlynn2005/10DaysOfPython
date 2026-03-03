#Exercises Day 3
#No1
age = 20

#No2
height = 5.7

#No3
complex_number = 3 + 4j

#No4
base = int(input("Enter base: "))
height = int(input("Enter height: "))
print("Area of triangle:", 0.5 * base * height)

#No5
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
print("The perimeter of the triangle is:", a + b + c)

#No6
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)

#No7
pi = 3.14
radius = float(input("Enter radius: "))
area = pi * radius * radius
circumference = 2 * pi * radius
print("Area:", area)
print("Circumference:", circumference)

#No8
slope8 = 2
y_intercept = -2
x_intercept = 1
print("Slope:", slope8)
print("x-intercept:", x_intercept)
print("y-intercept:", y_intercept)

#No9
x1, y1 = 2, 2
x2, y2 = 6, 10
slope9 = (y2 - y1) / (x2 - x1)
print("Slope:", slope9)

#No10
print("Both slopes are equal:", slope8 == slope9)

#No11
for x in range(-5, 1):
    y = x**2 + 6*x + 9
    print("x =", x, "y =", y)

#No12
print(len("python") != len("jargon"))

#No13
print("on" in "python" and "on" in "jargon")

#No14
sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

#No15
print("on" in "dragon" and "on" in "python")

#No16
length = len("python")
print(str(float(length)))

#No17
num = int(input("Enter a number: "))
print(num % 2 == 0)

#No18
print(7 // 3 == int(2.7))

#No19
print(type("10") == type(10))

#No20
print(int(float("9.8")) == 10)

#No21
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print("Your weekly earning is", pay)

#No22
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

#No23
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
def print_something(name = "Someone", age = "Unknown"):
    print("my name is", name, "and my age is", age)

print_something( age = 27 , name = "Nick")

def print_people (*people):
    for person in people:
        print("This person is", person )

print_people("Nick", "samuel","simon","joseph", "Mathew", "George")

def do_math(num1, num2):
    return num1 + num2

math1= do_math(5,7)
math2= do_math(11,34)

print("The first sum is ",math1,"The second sum is ",math2)


check = "Hamburgers"

if check == False:
    print("It is false")
elif check == "Hamburgers":
    print("Yummy,humburger")
elif check == "Yo":
    print("Hello")
else:
    print("It is actually equal to True")

numbers =  [1,2,3,4,5]

for item in numbers:
    print( item )

names = ["Nick","Joseph"," Mathew","latin"]

for item in names:
    print("This person name is :", item)

run = True
current = 1

while run:
    if current == 100:
        run = False

    else:
        print(current)
        current += 1
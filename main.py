import time
# First classwork
my_name = input("What is your name?\n")
my_age = input("What's your age?\n")
print(f"Hi, My name is {my_name} And I am {my_age} years old")

# Second Classwork

    # Solution #1

first_number = int(input("insert the first number \n"))
second_number = int(input("insert the second number \n"))

operation = input("type the operator (+ , - , * , /) \n")

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    print(first_number / second_number)
else:
    print("Wrong operator")

    # Solution #2

print("Use the calculator as follows (with spaces): \nx + y \nx - y \nx * y \nx / y")
time.sleep(2)
operation = input("Enter your operation: \n")

first_number = int(operation[0])
operator = operation[2]
second_number = int(operation[4])

if first_number | second_number == None:
    print("wrong operation form!")
else: 
    if operator == "+":
        print(first_number + second_number)
    elif operator == "-":
        print(first_number - second_number)
    elif operator == "*":
        print(first_number * second_number)
    elif operator == "/":
        print(first_number / second_number)
    else:
        print("Wrong Operator")

#Third Classwork

number = input("Choose a number between 1 & 12: \n")
plural = input("Enter a plural noun: \n")
name = input("Enter your name: \n")
sentence = input("Enter any sentence: \n")
verb = input("Enter any verb: \n")

print(f"""
The story goes...
It was {number} o'clock when I heard a knock at the door.
I opened the door and there was a box full of {plural} with a note saying From {name}.
Just as I closed the door I heard a scream {sentence}
I froze in place and all I could do was {verb}.
""")


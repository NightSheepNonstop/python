price = 0
while True:
    age = input("Please enter your age.\n")
    age = int(age)
    if 0 <= age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    elif 12 <= age:
        price = 15
    print(f"The price of your ticket is {price}")
    out = input("Enter 'quit' to quit.\n")
    if out == 'quit':
        break

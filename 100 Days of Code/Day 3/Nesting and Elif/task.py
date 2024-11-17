print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Whats your age? "))

    if age >= 18:
        print("The ticket cost is $12")
    elif age < 18 and age >= 12:
        print("The ticket cost is $10")
    else:
        print("The ticket cost is $5")
else:
    print("Sorry you have to grow taller before you can ride.")

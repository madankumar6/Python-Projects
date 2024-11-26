import random
import my_module

random_number = random.random()
print(random_number)

zero_one = random.randint(0, 1)
print(zero_one)

print(f"My favorite number is {my_module.my_favorite_number}")

random_float = random.uniform(1, 10)

heads_tails = random.randint(0, 1)

if(heads_tails == 0) :
    print("Heads")
else :
    print("Tails")

bmi = 84 / 1.65 ** 2
weight = 74
height = 1.75
bmi = weight / (height ** 2)
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))

#f-strings
score = 99
score += 1
print(f"Your score is {score}")
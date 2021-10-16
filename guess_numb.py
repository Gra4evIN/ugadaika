import random


guesses_made = 0

name = input("Как тебя зовут? ")

number = random.randint(1, 20)

print('{0} Угадай число от 1 до 20, сможешь? У тебя 6 попыток'.format(name))

while guesses_made < 6:
    guess = input("Введи число: ")

    guesses_made += 1

    if guess != number:
        print("Попробуй ещё")

    if guess == number:
        break

if guess == number:
    print("Ты угадал!!! ")
else:
    print("Ты не угадал")



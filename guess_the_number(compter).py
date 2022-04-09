import random

def guess(x):

    random_number=random.randint(1,x)

    guess=0

    while(random_number != guess):
        guess=int(input(f"guess number between 1 to {x}"))
        if guess < random_number:
            print("opps!! the number is too low")
        elif guess > random_number:
            print("opps!! the number is too high")


    print(f"the number{guess} is exactly what you are looking for!")


guess(10)

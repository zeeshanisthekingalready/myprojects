import random as rand
print("Hello and welcome to my game.\n")
print("Set boundaeries.\n")
i = int(input())
print("Guess the number.\n")
def func(x):
    random_number = rand.randint(1,x)
    guess = input()
    while guess != random_number:
        print("Wrong number try again\n")
        guess = input()
        if guess == random_number:
            break
        break
    
    print("Yep you guessed it right")
func(i)

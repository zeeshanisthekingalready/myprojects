import random as rand
charecters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","o","p","q","r","s","t","u","v","w","x","y","z"]
def application():
    password = charecters[rand.randint(0,27)]
    print(password)
print("Welcome to my password genrator.\n")
print("How many charecters do you want your password to become.\n")
c = int(input())
for c in range(0,c,1):
    application()

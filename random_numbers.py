import random as rand
print("RANDOM NUMBER GENERATOR.\n")
def app(m,n):
    print(rand.randint(m,n))
    print("You want to quit\n")
    
while True:
    print("Enter the boundary :: MINIMUM\n")
    x = int(input())
    print("Enter the last boundary :: MAXIMUM\n")
    y = int(input())
    app(x,y)
    s = input()
    if s.lower() == "yes"or s.lower() == "Y":
        break
    elif s.lower() == "no"or s.lower() == "n":
        pass
    else:
        print("Invalid option\n")

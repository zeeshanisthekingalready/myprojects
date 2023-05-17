

print("Enter your name.\n")
n = input()
print("Enter your age.\n")
try:
  a = int(input())
except:
  print("Invalid input or some other error.\n")
print("Where do you live.\n")
l = input()
print("Do you work or own any buisness if so please write it's name.\n");
j = input()
print("What is your faviourute color.\n")
c = input()
print("Enter your gender.\n")
g = input()
print("\n")
print("\n")
if g == "Male" or g == "male":
    print("There was a ",g,"\n")
    print("His name was ",n,"\n")
    print("He was ",a," years old.\n")
    print("He lived in",l,"\n")
    if j == "work" or j == "Work":
        print("He worked a boring life poor guy.\n")
    elif j == "Own" or j == "own":
        print("He owned a small buisness.\n")
    else:
        print("He was a lazy person.\n")
    print("His faviourute color was ",c,"\n")
elif g == "female"or g == "Female":
    print("There was a ",g,"\n")
    print("her name was ",n,"\n")
    print("she was ",a," years old.\n")
    print("she lived in",l,"\n")
    print("she worked or owned ",j,"\n")
    print("her faviourute color was ",c,"\n")
else:
    print("There is no gender like this.")

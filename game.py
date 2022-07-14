import random

print("Who are you?")
name = input()
print("Hello, " + name + "!");

print("Tossing a coin...")
heads = 0
tails = 0

for i in range(3):
    print("Round " + str(i) + ": ", end="")
    if random.randint(0, 1) == 0:
        heads += 1
        print("Heads")
    else:
        tails += 1
        print("Tails")

print("Heads: " + str(heads) + ", Tails: " + str(tails))
if heads > tails:
    print("You won")
else:
    print("You lost")

print("Welcome! Please enter a name for your robot")
name = str(input())

print("Your robots name is",name, "\nHow many lives do they have?")
lives = int(input())

print("Enter their shield level")
shields = int(input())
print("Enter their energy level")
energy = int(input())

print(name, "Has",lives, "Lives\n",shields, "shield levels and",energy, "energy levels.")
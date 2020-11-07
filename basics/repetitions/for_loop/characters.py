print("What strange markings do you see?")
markings = input()

for positions in range(0 , len(markings), 1):
  print("Index", positions, ":", markings[positions])
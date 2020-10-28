print("What type of cover does the book have?")
cover = input()

if (cover.lower() == "soft"):
  print("Is the book perfect bound")
  bound = input()

  if(bound.lower() == "yes"):
    print("Soft bound, perfect bound books are very popular!")
  elif (bound.lower() == "no"):
    print("Soft covers with coils or stitches are great for short books")
  else: 
    print("Input not recognised!")

else:
  print("Books with hard covers can be more expensive!")
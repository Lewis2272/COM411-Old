print("Beep is lost!\nAhead of him are 2 winding paths\nOne dark and scary\nThe other light and colourful\nWhere would you like beep to go?")
pathway = input()

if (pathway == "scary") or (pathway == "dark"):
  print("Beep will go to the dark forest!\nNow he's here, Beep can sleep in the log cabin, or stay outside")
  beep_sleep = input()

  if (beep_sleep == "log cabin"):
    print("Beep gets a good nights rest inside the cabin")
  elif (beep_sleep == "stay outside"):
    print("Beep braves the forest, and eventually finds his way back to camp")

elif (pathway == "light") or (pathway == "colourful"):
  print("Beep comes across a stream!\nSuddenly he loses his footing and falls in!\nQuick! Beep needs to dry off!\nWhat should Beep make to keep warm?")
  beep_choice1 = input()

  print("Okay! What should Beep make next to keep safe?")
  beep_choice2 = input()

  if (beep_choice1 == "fire") and (beep_choice2 == "shelter"):
    print("Correct! Beep drys himself off and makes a bed for the night\nThe next morning he safely returns back to camp")

  else:
    print("Beep dies of hypothermia :/")

else:
  print("Did not recognise the input, please try again")
 

  
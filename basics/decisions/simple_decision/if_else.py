print("Please enter the activity to be performed")
activity = str(input())

if activity in ['calculate', 'Calculate', 'CALCULATE',]:
  print("Performing calculations...")
else:
  print("Performing activity...")

print("Activity completed!")
#Original if statement could've been 
  #if(activity.lower() == 'calculate')
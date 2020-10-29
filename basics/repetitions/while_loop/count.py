print("How many live cables must I avoid")
avoid = int(input())

live_cable = 0

while (live_cable < avoid):
  print("Avoiding...", end="")
  live_cable += 1
  print("...Done!",avoid, " live cables avoided")

print("All live cables have been avoided")

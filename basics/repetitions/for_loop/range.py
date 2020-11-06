print("What level of brightness is required?")
brightness = int(input())

print("\nAdjusting brightness...\n")

for bright in range (2, brightness+1, 2):
  print("Beep's brightness level:", "*" *bright)
  print("Bop's brightness level:", "*" *bright)


print("Adjustments complete!")
print("How many bars should be charged")
bars = int(input())

bars_charged = 0

while(bars_charged < bars):
  print("Charging:", "■" *bars_charged)
  bars_charged += 1

print("The battery is fully charged")
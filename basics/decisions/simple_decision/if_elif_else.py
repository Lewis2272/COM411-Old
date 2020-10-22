print("Towards which direction should I paint (up, down, left or right)?")
direction = str(input())

if direction in ['Up', 'up', 'UP']:
  print("I am painting in the upward direction!")
elif direction in ['Down', 'down', 'DOWN',]:
  print("I am painting in the downward direction!")
elif direction in ['Left', 'left', 'LEFT',]:
  print("I am painting to the left!")
elif direction in ['Right', 'right', 'RIGHT',]:
  print("I am painting to the right")
else:
  print("Please emter a valid direction")
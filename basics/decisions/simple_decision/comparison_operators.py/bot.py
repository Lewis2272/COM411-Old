print("Please enter your first number")
firstnum =int(input())

print("Please enter your second number")
secondnum = int(input())

if firstnum < secondnum:
  print("The first number is smaller than the second number")
elif secondnum < firstnum:
  print("The second number is smaller than the first number")
if firstnum == secondnum:
  print("Both of the number are equal")

#Alternative print could be
  #print("{} is smaller than {}".format (firstnum, secondnum))
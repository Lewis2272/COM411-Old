print("Plese enter the first whole number")
firstnum = int(input())

print("Please enter the second whole number")
secondnum = int(input())

print("Please enter the third whole number")
thirdnum = int(input())

num_even = 0
num_odd = 0

if firstnum % 2 ==0:
 num_even += 1
else:
  num_odd += 1

if secondnum % 2 ==0:
 num_even += 1
else:
  num_odd += 1

if thirdnum % 2 ==0:
 num_even += 1
else:
  num_odd += 1

print("There were {} even and {} odd number".format(num_even, num_odd))
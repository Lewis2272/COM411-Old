print("How many numbers should I sum up?")

sum_user = int(input())
sum_start = 0
answer = 0

while (sum_start < sum_user):
  print("Please enter number",sum_start+1, "of",sum_user,)
  actual_sum = int(input())
  sum_start += 1
  answer += actual_sum

print("The answer is",answer,)
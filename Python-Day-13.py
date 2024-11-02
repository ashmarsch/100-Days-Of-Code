print("Welcome to My Gradebook")
test_name = input("What is the name of the test?")
max_score = int(input("What is the maximum score you could receive?"))
actual_score = int(input("What is the score you received?"))
percentage = round(actual_score / max_score * 100, 2)

if percentage == 100:
  print("You got an A+!")
elif percentage >= 90:
  print("You got an A!")
elif percentage >= 80:
  print("You got a B!")
elif percentage >= 70:
  print("You got a C!")
elif percentage >= 60:
  print("You got a D!")
else:
  print("You got an F!")

print(f"You got {percentage}% on the {test_name} test.")
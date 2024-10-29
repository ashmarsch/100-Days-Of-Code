myYear = int(input("What year were you born? "))
if myYear >= 1925 and myYear <= 1946:
  print("You are a Traditionalist")
elif myYear >= 1947 and myYear <= 1964:
  print("You are a Baby Boomer")
elif myYear >= 1965 and myYear <= 1981:
  print("You are a Generation X")
elif myYear >= 1982 and myYear <= 1995:
  print("You are a Millenial")
elif myYear >= 1996 and myYear <= 2015:
  print("You are a Generation Z")
else:
  print("You are either too young or too old to be on this list.")
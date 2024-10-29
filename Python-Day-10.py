totalBill = float(input("What was the total bill? $"))
tipPercent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
numPeople = int(input("How many people to split the bill? "))
tip = totalBill * (tipPercent / 100)
totalBill += tip
split = totalBill / numPeople
print(f"Each person should pay: ${round(split, 2)}")
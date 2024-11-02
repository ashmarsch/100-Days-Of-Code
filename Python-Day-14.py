from getpass import getpass as input
print("E P I C    B A T T L E")
print()
print("Select your move (R, P ,or S)")
print()
player1 = input("Player 1 > ")
print()
player2 = input("Player 2 > ")
print()
if player1 == "R" and player2 == "R" :
  print("You both picked Rock, draw!")
elif player1 == "R" and player2 == "P" :
  print("P2's Paper smothered P1's Rock!")
elif player1 == "R" and player2 == "S" :
  print("P1's Rock smashed P2's Scissors!")
elif player1 == "P" and player2 == "R" :
  print("P1's Paper smothered P2's Rock!")
elif player1 == "P" and player2 == "P" :
  print("You both picked Paper, draw!")
elif player1 == "P" and player2 == "S" :
  print("P2's Scissors Cut P1's Paper!")
elif player1 == "S" and player2 == "R" :
  print("P2's Rock smashed P1's Scissors!")
elif player1 == "S" and player2 == "P" :
  print("P1's Scissors Cut P2's Paper!")
elif player1 == "S" and player2 == "S" :
  print("You both picked Scissors, draw!")
else:
  print("Invalid Move")

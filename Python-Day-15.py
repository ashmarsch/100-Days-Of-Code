exit = "no"

while exit == "no":
  animal_sound = input("What animal sound do you want to hear?")
  if animal_sound == "cow" or animal_sound == "Cow" :
    print("Moo")
  elif animal_sound == "pig" or animal_sound == "Pig" :
    print("Oink")
  elif animal_sound == "horse" or animal_sound == "Horse" :
    print("Neigh")
  elif animal_sound == "duck" or animal_sound == "Duck" :
    print("Quack")
  else:
    print("I don't know that animal sound. Try again.")

exit = input("Do you want to exit?: ")
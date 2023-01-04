print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print(f"okay,your height is {height} you can pass.")
  
  age = int(input("How old are you? "))
  if age < 12:
    print("please pay $5")
  elif age <= 18:
    print("please pay $7")
  else:
    print("please pay $12")
  
else:
  print("Your height is not enough to go on the toy.")
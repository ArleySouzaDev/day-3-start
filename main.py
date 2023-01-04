print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print(f"okay,your height is {height} you can pass.")
  bill = 0
  age = int(input("How old are you? "))
  if age < 12:
    bill = 5
    print("Child tickets is $5")
  elif age <= 18:
    bill = 7
    print("Young tickets is $7")
  else:
    bill = 12
    print("Adult tickets is $12")

  photo = input("do you want a photo taken? Y or N. ")
  
  if photo == "Y":
    bill += 3
    print(f"The new value will have an increase of $3, the final price is ${bill}, enjoy and have fun." )
  else:
    print(f"Final price is ${bill}")
  
else:
  print("Your height is not enough to go on the toy.")
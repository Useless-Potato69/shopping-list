#Welcomes to Store
print("------Dick Smiths Pen Battery Online Shop------")

#Defines Variables
shopping = "yes"
slist = []

#Asks the user for their name
name = input("What is your name? ")

#Shopping begins
while shopping == "yes":
  item = input("What would you like to buy? ")
  item = item.strip()
  item = item.capitalize()

  #Adds item to list
  slist.append(item)

  #Clears display
  import os
  def clear(): os.system('clear') 
  clear()

  #Prints header
  print("------Dick Smiths Pen Battery Online Shop------")
  print("Your Cart: {}".format(slist))

  #Asks user if they wish to keep shopping
  print("What would you like to buy? {}".format(item))
  shopping = input("Do you wish to keep shopping? ")
  shopping = shopping.strip()
  shopping = shopping.casefold()


  #Clears display
  import os
  def clear(): os.system('clear') 
  clear()

  #Prints header
  print("------Dick Smiths Pen Battery Online Shop------")
  print("Your Cart: {}".format(slist))

#Ends user interaction
print("Thank you for shopping with us {}!".format(name))
print("See you next time!")




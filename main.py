#Welcomes to Store
print("------Smiths Online Shop------")

#Defines Variables
shopping = "yes"
slist = []

#Asks the user for their name
name = input("What is your name?")

#Shopping begins
while shopping == "yes":
  item = input("What would you like to buy?")
  item = item.strip()
  item = item.capitalize()

  #Adds item to list
  slist.append(item)
  shopping = input("Do you wish to keep shopping?")
  shopping = shopping.strip()
  shopping = shopping.casefold()

  #Clears display
  import os
  def clear(): os.system('clear') 
  clear()

  #Prints header
  print("------Smiths Online Shop------")
  print("Your Cart: {}".format(slist))

#Ends user interaction
print("Thank you for shopping with us {}!".format(name))
print("See you next time!")




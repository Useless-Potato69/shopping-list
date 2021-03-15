#Welcomes to Store
print("------Smiths Online Shop------")

#Defines Variables
shopping = "yes"
slist = []

#Asks the user for their name
name = input("What is your name?")

#Adds items to cart
while shopping == "yes":
  item = input("What would you like to buy?")
  item = item.strip()
  item = item.capitalize()
  slist.append(item)
  shopping = input("Do you wish to keep shopping?")
  shopping = shopping.strip()
  shopping = shopping.casefold()
  import os
  def clear(): os.system('clear') 
  clear()
  print("------Smiths Online Shop------")
  print("Your Cart: {}".format(slist))
print("Thank you for shopping with us {}!".format(name))
print("See you next time!")





#if shopping == "yes":
#  item = input("What would you like to buy?")
#  item = item.strip()
#  item = item.capitalize()
#  slist.append(item)
  
#elif shopping == "no":
  #print("Thank you for shopping with us!")
  #print(list)
#else:
  #print("Please enter yes or no")
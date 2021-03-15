#Welcomes to Store
print("------Welcome to the online shop------")


shopping = "yes"
slist = []

#Adds items to cart
while shopping != "yes":
  item = input("What would you like to buy?")
  item = item.strip()
  item = item.capitalize()
  slist.append(item)
  shopping = input("Do you wish to keep shopping?")
  shopping = shopping.strip()
  shopping = shopping.casefold()
  print(slist)






if shopping == "yes":
  item = input("What would you like to buy?")
  item = item.strip()
  item = item.capitalize()
  slist.append(item)
  
elif shopping == "no":
  print("Thank you for shopping with us!")
  print(list)
else:
  print("Please enter yes or no")
#Welcomes to Store
print("------Dick Smiths Pen Battery Online Shop------")

#Defines Variables
still_shopping = True
slist = []

#Asks the user for their name
name = input("What is your name? ")

#Shopping begins
while still_shopping == True:
  

  #Clears display
  import os
  def clear(): os.system('clear') 
  clear()

  #Prints header
  print("------Dick Smiths Pen Battery Online Shop------")
  print("Your Cart: {}".format(slist))

  #Asks user what they want to buy
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
  moreitem = input("Do you wish to keep shopping? Y/N ")
  moreitem = moreitem.strip()
  moreitem = moreitem.casefold()

  if moreitem == "n":
    still_shopping = False
    import os
    def clear(): os.system('clear') 
    clear()
    print("------Dick Smiths Pen Battery Online Shop------")
    print("Your Cart: {}".format(slist))

    #Ends user interaction
    print("Thank you for shopping with us {}!".format(name))
    print("See you next time!")
    break

  #If users input is not acceptable then keep asking until it is
  elif moreitem != "y":
    still_shopping = False

    while moreitem != "y":
      import os
      def clear(): os.system('clear') 
      clear()
      print("------Dick Smiths Pen Battery Online Shop------")
      print("Your Cart: {}".format(slist))
      print("Please enter a valid response. (Y/N)")
      #Asks user again
      moreitem = input("Do you wish to keep shopping? Y/N ")
      moreitem = moreitem.strip()
      moreitem = moreitem.casefold()
      import os
      def clear(): os.system('clear') 
      clear()
      print("------Dick Smiths Pen Battery Online Shop------")
      print("Your Cart: {}".format(slist))

      #if users answers no, end user interaction
      if moreitem == "n":
        import os
        def clear(): os.system('clear') 
        clear()
        print("------Dick Smiths Pen Battery Online Shop------")
        print("Your Cart: {}".format(slist))
        print("Thank you for shopping with us {}!".format(name))
        print("See you next time!")
        break

      #If users answers yes, continue shopping
      elif moreitem == "y":
        still_shopping = True
  else:
    still_shopping = True

  







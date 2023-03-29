while True:
    # Loop until a valid input is entered (1.1)
    while True:
        eggCount = input("How many eggs do you want to order? ")
        if eggCount.isdigit():
            eggs = int(eggCount)
            break
        else:
            print("Invalid input. Please enter a positive integer.")
            
    # Calculate the number of dozens and loose eggs (1.2)
    dozens = eggs // 12
    looseEggs = eggs % 12
    
     # Calculate the total cost of eggs (1.3)
    dozenPrice = 3.25
    loosePrice = 0.45
    totalPrice = dozens * dozenPrice + looseEggs * loosePrice
    
    # Display the final amount owed (1.4)
    print("You ordered {} eggs. That’s {} dozen at R{} per dozen and {} loose eggs at {}c each for a total of R{:.2f}.".format(eggs, dozens, dozenPrice, looseEggs, loosePrice*100, totalPrice))
    
    #Allow user to order again
    while True:
        orderAgain = input("Would you like to place another order? \n(Y): Yes\n(N): No\n(Y/N): ")
        if orderAgain.upper() == "Y":
            break
        elif orderAgain.upper() == "N":
            print("Thank you for your order. Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter Y or N.")
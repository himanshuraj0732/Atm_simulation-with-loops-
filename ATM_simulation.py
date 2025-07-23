balance=90000
while True:
    print("\nWelcome to the ATM 💳")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")



    if choice == "1":
        print(f"Your balance is ${balance}")

    elif choice == "2":
        deposit= int(input("Enter the amount you want to deposit in your bank: "))
        balance +=deposit 
        print(f"you have deposit ${deposit:,.2f} in your bank , Now your balance is now ${balance:,.2f} ")   

    elif choice == "3":
        withdraw= int(input("Enter the amount you want to withdraw from your bank: "))
        if withdraw > balance:
           print("This is insuffisiant amount , please enter again")  

        else:
          balance -= withdraw
          print(f"you have withdraw ${withdraw:,.2f} from your bank now your bank has ${balance:,.2f}") 
        
    elif choice == "4":
        print("Thank you for using our ATM. Goodbye!")
        
        break

else:
    print("Oops, Something wrong please try again!!") 
# Atm_simulation-with-loops-
# 🏦 ATM Simulator – Python CLI Project

This is a beginner-friendly **ATM Simulator** built using **Python**. It uses loops, conditional statements, and user input to simulate basic banking operations like checking balance, depositing, and withdrawing money.

---

## 🚀 Features

- ✅ Check current account balance
- 💰 Deposit money to account
- 💸 Withdraw money with balance check
- 🔁 Continuous operation using loop until user exits
- 🛑 Error handling for insufficient balance
- 💳 User-friendly console interface

---

## 🧪 How It Works

1. Starts with a default balance (₹90,000)
2. Repeatedly shows options to the user:
   - Check Balance
   - Deposit
   - Withdraw
   - Exit
3. Updates balance as per user operations
4. Exits when user selects option `4`

---

## 📁 Code Preview

```python
balance = 90000

while True:
    print("\nWelcome to the ATM 💳")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your balance is ${balance:,.2f}")

    elif choice == "2":
        deposit = int(input("Enter the amount to deposit: "))
        balance += deposit
        print(f"You deposited ${deposit:,.2f}. New balance: ${balance:,.2f}")

    elif choice == "3":
        withdraw = int(input("Enter the amount to withdraw: "))
        if withdraw > balance:
            print("❌ Insufficient balance.")
        else:
            balance -= withdraw
            print(f"You withdrew ${withdraw:,.2f}. Remaining balance: ${balance:,.2f}")

    elif choice == "4":
        print("Thank you for using our ATM. Goodbye!")
        break

    else:
        print("❗ Invalid choice. Please select from 1 to 4.")

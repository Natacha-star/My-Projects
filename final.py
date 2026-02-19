# ===================================
#        MINI DIGITAL BANK
# ===================================

accounts = []


# -----------------------------------
# CREATE ACCOUNT
# -----------------------------------
def create_account():
    name = input("Enter account holder name: ").strip()

    # Check duplicate
    for acc in accounts:
        if acc["name"].lower() == name.lower():
            print("Account already exists!\n")
            return

    account = {
        "name": name,
        "balance": 0.0
    }

    accounts.append(account)
    print("Account created successfully!\n")


# -----------------------------------
# FIND ACCOUNT
# -----------------------------------
def find_account(name):
    for acc in accounts:
        if acc["name"].lower() == name.lower():
            return acc
    return None


# -----------------------------------
# DEPOSIT
# -----------------------------------
def deposit():
    name = input("Enter account name: ").strip()
    account = find_account(name)

    if account is None:
        print("Account not found.\n")
        return

    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Amount must be positive.\n")
            return

        account["balance"] += amount
        print("Deposit successful!\n")

    except ValueError:
        print("Invalid amount. Please enter a number.\n")


# -----------------------------------
# WITHDRAW
# -----------------------------------
def withdraw():
    name = input("Enter account name: ").strip()
    account = find_account(name)

    if account is None:
        print("Account not found.\n")
        return

    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Amount must be positive.\n")
            return

        if amount > account["balance"]:
            print("Insufficient balance.\n")
            return

        account["balance"] -= amount
        print("Withdrawal successful!\n")

    except ValueError:
        print("Invalid amount. Please enter a number.\n")


# -----------------------------------
# VIEW ACCOUNTS
# -----------------------------------
def view_accounts():
    if not accounts:
        print("No accounts available.\n")
        return

    print("\n====== ACCOUNT LIST ======")
    for acc in accounts:
        print(f"Name: {acc['name']}")
        print(f"Balance: {acc['balance']}")
        print("--------------------------")
    print()


# -----------------------------------
# SAVE TO FILE
# -----------------------------------
def save_to_file():
    try:
        with open("accounts.txt", "w") as file:
            for acc in accounts:
                file.write(f"{acc['name']},{acc['balance']}\n")

        print("Accounts saved successfully!\n")

    except Exception as e:
        print("Error saving file:", e)


# -----------------------------------
# LOAD FROM FILE
# -----------------------------------
def load_from_file():
    try:
        with open("accounts.txt", "r") as file:
            accounts.clear()
            for line in file:
                name, balance = line.strip().split(",")
                accounts.append({
                    "name": name,
                    "balance": float(balance)
                })

        print("Accounts loaded successfully!\n")

    except FileNotFoundError:
        print("File not found. No data loaded.\n")

    except Exception as e:
        print("Error loading file:", e)


# ===================================
# MAIN MENU LOOP
# ===================================

while True:
    print("====== MINI DIGITAL BANK ======")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Accounts")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        view_accounts()
    elif choice == "5":
        save_to_file()
    elif choice == "6":
        load_from_file()
    elif choice == "7":
        print("Goodbye ")
        break
    else:
        print("Invalid choice. Try again.\n")

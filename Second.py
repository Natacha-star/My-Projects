print("===================================")
print("      WELCOME TO SECRET VAULT")
print("===================================")

SECRET_PIN = 4321

while True:

    start = input("Do you want to try unlocking the vault? (yes/no): ").lower()

    if start == "no":
        print("Goodbye agent ")
        break

    elif start != "yes":
        print("Invalid input. Try again.")
        continue

    print("\n--- LEVEL 1: PIN VERIFICATION ---")

    attempts = 3
    unlocked = False

    for attempt in range(1, 4):
        pin = int(input("Enter the 4-digit secret PIN: "))

        if pin == SECRET_PIN:
            print("Correct PIN ")
            unlocked = True
            break
        else:
            attempts -= 1
            print(f"Wrong PIN  Attempts left: {attempts}")

    if not unlocked:
        print("Vault Locked. Too many failed attempts \n")
        continue

    print("\n--- LEVEL 2: NUMBER CHALLENGE ---")

    number_passed = False

    for _ in range(3):
        number = int(input("Enter a number between 1 and 10: "))

        if number < 1 or number > 10:
            print("Invalid number. Must be between 1 and 10.")
            continue

        if number % 2 == 0:
            print("Even number! Challenge passed ")
            number_passed = True
            break
        else:
            print("Odd number! Try again ")

    if not number_passed:
        print("Failed the number challenge \n")
        continue

    print("\n--- LEVEL 3: DISCIPLINE CHECK ---")

    study = input("Did you study today? (yes/no): ").lower()
    exercise = input("Did you exercise today? (yes/no): ").lower()
    sleep = input("Did you sleep at least 7 hours? (yes/no): ").lower()

    score = 0

    if study == "yes":
        score += 1
    if exercise == "yes":
        score += 1
    if sleep == "yes":
        score += 1

    if score >= 2:
        print("\n Vault Unlocked Successfully!")
    else:
        print("\n Access Denied. Discipline level too low.")

    print("\nSimulation complete.\n")

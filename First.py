print("Hello! Welcome to my simple life status calculator!")
print("_____________________________________________________")

Name = input("Enter your full name: ")
Age = int(input("Enter your age: "))
Height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kgs: "))
Hours = float(input("How many hours do you sleep in a day? "))
StudyHours = float(input("How many hours do you study in a day? "))
income = float(input("What is the monthly income you want to earn? "))

Age_to_months = Age * 12
Height_to_meters = Height / 100
BMI = weight / (Height_to_meters ** 2)

yearly_income = income * 12
weekly_working_hours = StudyHours * 7
yearly_working_hours = weekly_working_hours * 52
rem_hours = 24 - Hours - StudyHours

print("==================================")
print("LIFE SUMMARY")
print("==================================")

print(f"Your full name is: {Name}")
print(f"Your Age: {Age} years ({Age_to_months} months)")
print(f"Your BMI is: {round(BMI, 2)}")
print(f"You study {weekly_working_hours} hours per week. If consistent, that is {yearly_working_hours} hours per year.")
print(f"You sleep {Hours} hours per day, leaving {rem_hours} hours for other activities.")
print(f"Your desired monthly income is {income}, which equals {yearly_income} per year.")

print(f"Congratulations {Name}! Keep pushing toward your goals 🚀")

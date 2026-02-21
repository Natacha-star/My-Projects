#PART A: One-Dimensional Arrays
marks = [] # Create your empty array
total = 0

# 1. Accept 10 marks
for i in range(10):
    val = int(input("Enter mark: "))
    marks.append(val)
    total += val # Add to total as we go

# 2. Calculations
average = total / 10
highest = max(marks)
lowest = min(marks)

print(f"Total: {total}, Average: {average}")
print(f"High: {highest}, Low: {lowest}")
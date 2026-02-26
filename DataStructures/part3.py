# This file demonstrates the use of nested lists to represent a more complex data structure, such as a school's classes, students, and their marks in different subjects. The code calculates the average marks for each class and the overall average for the school.
# [Class][Student][Subject]
school_data = [
    [[80, 90], [70, 85], [60, 75]], # Class 1 (3 students, 2 marks each)
    [[95, 88], [82, 91], [77, 83]]  # Class 2 (3 students, 2 marks each)
]

grand_total = 0

total_marks_count = 12 # 2 classes * 3 students * 2 subjects

# Logic to calculate averages
for c in range(2): # Loop through Classes
    class_total = 0
    for s in range(3): # Loop through Students
        for sub in range(2): # Loop through Subjects
            val = school_data[c][s][sub]
            class_total += val
            grand_total += val
            print(f"Class {c+1}, Student {s+1}, Subject {sub+1}: {val}")
            
    print(f"Average for Class {c+1}: {class_total / 6}")
    

print(f"Overall School Average: {grand_total / total_marks_count}")

# 2 Rooms, 7 Days, 3 Times
temp_data = [
    # Room 1
    [[22, 24, 21], [23, 25, 22], [20, 22, 19], [21, 23, 20], [24, 26, 23], [25, 27, 24], [22, 24, 21]],
    # Room 2
    [[18, 20, 17], [19, 21, 18], [17, 19, 16], [18, 20, 17], [21, 23, 20], [22, 24, 21], [19, 21, 18]]
]

# Start by assuming the very first temperature is both highest and lowest
highest = temp_data[0][0][0]
lowest = temp_data[0][0][0]

# Triple loop to check every single value
for r in range(2):     # Rooms
    for d in range(7): # Days
        for t in range(3): # Times
            current_temp = temp_data[r][d][t]
            
            if current_temp > highest:
                highest = current_temp
            if current_temp < lowest:
                lowest = current_temp

print(f"Highest Temperature Recorded: {highest}°C")
print(f"Lowest Temperature Recorded: {lowest}°C")
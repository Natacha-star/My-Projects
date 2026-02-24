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
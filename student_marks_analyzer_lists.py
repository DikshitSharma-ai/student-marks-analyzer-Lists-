# Student Marks Analyzer
# Mini Python Project(Lists)
#Author: Dikshit Sharma


marks = [55, 72, 48, 90, 67, 39]

# ----------------------
# Variables define
# ----------------------

total = 0
count = 0
count_pass = 0
max_marks = marks[0]
min_marks = marks[0]

# -----------------------
# For Loop
# -----------------------

for n in marks:
    total = total + n
    count = count + 1

# -----------------------
# Pass Count
# -----------------------

    if n >= 50:
        count_pass = count_pass + 1

# -----------------------
# Highest Marks
# -----------------------

    if n > max_marks:
        min_marks = n

# -----------------------
# Lowest Marks
# -----------------------

    if n < min_marks:
        min_marks = n

# -----------------------
# Average
# -----------------------

avg = total/count

print("Total Marks = ", total)
print("Average Marks = ", avg)
print("Total Students = ", count)
print("Pass Students = ", count_pass) 
print("Highest Marks = ", max_marks)       
print("Lowest Marks = ", min_marks)

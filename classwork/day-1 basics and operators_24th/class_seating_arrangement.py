# Input
total_students = int(input("Enter total students: "))
students_per_row = int(input("Enter students per row: "))

# Calculate complete rows using arithmetic operator (//)
complete_rows = total_students // students_per_row

# Output
print("Number of Complete Rows:", complete_rows)
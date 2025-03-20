# Program to manage student grades using a dictionary
# Create a dictionary with student names as keys and their grades as values
grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92
}
# Display all student names and their grades
print("Student Grades:")
for student, grade in grades.items():
    print(f"{student}: {grade}")
# Add a new student and grade
grades["Eve"] = 88
print("\nAdded Eve's grade.")
# Update Bob's grade
grades["Bob"] = 95
print("\nUpdated Bob's grade.")
# Remove a student (e.g., Charlie)
del grades["Charlie"]
print("\nRemoved Charlie from the dictionary.")
# Display the updated dictionary
print("\nUpdated Student Grades:")
for student, grade in grades.items():
    print(f"{student}: {grade}")

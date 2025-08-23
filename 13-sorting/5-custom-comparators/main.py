# Custom Comparator - Python Example

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 85}
]

# Sort by grade descending, then name ascending
sorted_students = sorted(students, key=lambda x: (-x["grade"], x["name"]))
print(sorted_students)

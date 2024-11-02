from new_student import Student

# Using the Car dataclass
try:
    student = Student(name="zakaria", surname="ihirri")
    print(student)
except TypeError as e:
    print(f"ERROR: {e}")
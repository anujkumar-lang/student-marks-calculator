name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
dld = float(input("Enter DLD marks: "))

total = maths + python + dld
percentage = total / 3

print("\n--- Result ---")
print("Name:", name)
print("Total:", total)
print("Percentage:", round(percentage, 2), "%")

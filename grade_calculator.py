name = input("Enter Student Name: ")

m1 = int(input("Enter Mark 1: "))
m2 = int(input("Enter Mark 2: "))
m3 = int(input("Enter Mark 3: "))
m4 = int(input("Enter Mark 4: "))
m5 = int(input("Enter Mark 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: D")

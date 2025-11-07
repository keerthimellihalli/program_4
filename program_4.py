num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")

choice = input("Enter 1, 2, or 3: ")

if choice == '1':
    result = num1 + num2
    print("Addition result:", result)
elif choice == '2':
    result = num1 - num2
    print("Subtraction result:", result)
elif choice == '3':
    result = num1 * num2
    print("Multiplication result:", result)
else:
    print("Invalid choice. Please enter 1, 2, or 3.")

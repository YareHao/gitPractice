def add(a, b):
    return a + b
 
def subtract(a, b):
    return a - b

print ("Welcome to Simple Calculator")

while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ")

    if choice == '3':
        print("Goodbye!")
        break

    if choice in ('1', '2'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
    
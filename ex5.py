import sys
exit = ""
counter = 0

while not exit == "exit":
    result = 0
    try:
        first_number = float(input("Provide your first number: "))
        operation = input("provide your arithmetic operation (plus, minus, multiply, divide): ")
        second_number = float(input("Provide your second number: "))

        if operation in ["plus", "minus", "multiply", "divide"]:
            if operation == "plus":
                result = sum(first_number, second_number)
                print(f"{first_number} + {second_number} = {result}")

            if operation == "minus":
                result = first_number - second_number
                print(f"{first_number} - {second_number} = {result}")

            if operation == "multiply":
                result = first_number * second_number
                print(f"{first_number} - {second_number} = {result}")

            if operation == "divide":
                result = first_number / second_number
                print(f"{first_number} - {second_number} = {result}")
            
            exit = input("Type exit to stop: ")
            counter += 1
        else:
            print("Invalid operation.")
            sys.exit()
    except ValueError as error:
        print(error)

print(f"You executed {counter} operations.")


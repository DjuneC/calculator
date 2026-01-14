def operation(first_number, next_number, operator):
    
    calculation = {
            "+": first_number + next_number,
            "-": first_number - next_number,
            "*": first_number * next_number,
            "/": first_number / next_number if next_number != 0 else "Error: Division by zero"
    }

    return calculation[operator]

def main():
    flow = "restart"
    result = 0 
    operators = ["+", "-", "*", "/"]
 
    while True:

        if flow == "restart":
            first_number = float(input("What's the first number?: "))

        print(", ".join(operators))   

        operator = input("Pick an operation: ")

        next_number = float(input("What's the next number?: "))
        
        if flow == "restart":
            result = operation(first_number, next_number, operator)
        else:
            result = operation(result, next_number, operator)


        print(f"{first_number} {operator} {next_number} = {result}")
        
        
        decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if decision == "y":
            flow = "continue"
            continue

        print("You choose 'n' or something else, we are starting blank!")
        flow = "restart"

if __name__ == "__main__":
    main()

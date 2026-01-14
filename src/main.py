def operation(first_number, next_number, operator):
    
    calculation = {
            "+": first_number + next_number,
            "-": first_number - next_number,
            "*": first_number * next_number,
            "/": first_number / next_number if next_number != 0 else "Error: Division by zero"
    }

    return calculation[operator]




def main():
    operators = ["+", "-", "*", "/"]
    
    first_number = float(input("What's the first number?: "))

    print(", ".join(operators))   

    operator = input("Pick an operation: ")

    next_number = float(input("What's the next number?: "))

    result = operation(first_number, next_number, operator)

    print(f"{first_number} {operator} {next_number} = {result}")


if __name__ == "__main__":
    main()

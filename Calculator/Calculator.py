import art
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def calculator():
    print(art.logo)
    Repeat = True
    operation={  "+":add,
                 "-":subtract,
                 "*":multiply,
                 "/":divide
                 }
    num1 = float(input("What is the first number?:\n"))
    while Repeat:
        for symbol in operation:
            print(symbol)
        operation_symbol =(input("Pick an operation:\n"))
        num2= float(input("What is the next number?:\n"))
        answer=operation[operation_symbol](num1,num2)
        print(f"\n{num1} {operation_symbol} {num2} = {answer}\n")

        choice=input(f"Type'y' to continue calculating with {answer} or type 'n' to start new calculation\n").lower()
        if choice == "y":
            num1=answer
            Repeat=True
        elif choice == "n":
            print("\n" * 50)
            calculator()
        else:
            print("Invalid input. Please type 'y' or 'n'.")

calculator()
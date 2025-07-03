def calculate(n1,n2,op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 == 0:
            return "Error: Division by zero!"
        return n1 / n2
    else:
        return "Invalid operation!"

choice = 'n'
while True:
    n1 = float(input("Enter first number: "))
    op = input("Select Operation (+, -, *, /): ")
    n2 = float(input("Enter second number: "))
    res = calculate(n1, n2, op)
    print(f"{n1} {op} {n2} = {res}")
    choice = input("Would you like to continue with result(y) or start a new calculation(n): ").lower()
    while choice == 'y':
        op = input("Select Operation (+, -, *, /): ")
        n2 = float(input("Enter second number: "))
        new = calculate(res, n2, op)
        print(f"{res} {op} {n2} = {new}")
        res = new
        choice = input("Would you like to continue with result(y) or start a new calculation(n): ").lower()
    if choice != 'n':
        print("Exiting calculator.")
        break
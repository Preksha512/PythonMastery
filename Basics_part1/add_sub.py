num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

op = input("Choose operation (add / subtract / multiply / divide): ")

if op == "add":
    print("Result:", num1 + num2)
elif op == "subtract":
    print("Result:", num1 - num2)
elif op == "multiply":
    print("Result:", num1 * num2)
elif op == "divide":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")

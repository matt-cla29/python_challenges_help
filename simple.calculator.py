while True:
    math_calculation = input("which math calculation do you want to do? (+, -, *, /): ")
    number1 = int(input("enter your first number: "))
    number2 = int(input("enter your second number: "))

    if math_calculation == "+":
        print(number1 + number2)
    elif math_calculation == "-":
        print(number1- number2)
    elif math_calculation == "*":
        print(number1 * number2)
    elif math_calculation == "/":
        print(number1 / number2)

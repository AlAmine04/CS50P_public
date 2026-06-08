def main():
    expression = input("Expression: ").strip()

    # assign each caracter to a number or sign
    x, sign, y = expression.split(" ")

    # transform x and y to float
    x = float(x)
    y = float(y)

    result = interpret_expression(x, sign, y)
    print(f"{result:.1f}")


# handle the operation logic
def interpret_expression(sx, ssign, sy):
    match ssign:
        case "+":
            result = sx + sy
        case "-":
            result = sx - sy
        case "*":
            result = sx * sy
        case "/":
            result = sx / sy
    return result


main()

def prefixToPostfix(expression: str) -> str:
    stack = []
    
    expression = expression[::-1]
    
    for i in range(len(expression)):
        if expression[i] not in "+-*^/":
            stack.append(expression[i])
        else:
            if len(stack) < 2:
                print("Invalid prefix expression")
            op1 = stack.pop()
            op2 = stack.pop()
            string = op1 + op2 + expression[i]
            stack.append(string)
    
    if len(stack) != 1:
        print("Invalid prefix expression")
    return stack.pop()


if __name__ == "__main__":
    expression = "*-A/BC-/AKL"
    print(prefixToPostfix(expression))
def postfixToInfix(expression: str) -> str:
    stack = []
    
    for i in range(len(expression)):
        if expression[i] not in "+-*^/":
            stack.append(expression[i])
        else:
            if len(stack) < 2:
                print("Invalid postfix expression")
            op1 = stack.pop()
            op2 = stack.pop()
            string =   '(' + op2 + expression[i] + op1 + ')'
            stack.append(string)
    
    if len(stack) != 1:
        print("Invalid postfix expression")
    return stack.pop()


if __name__ == "__main__":
    expression = "ABC/-AK/L-*"
    print(postfixToInfix(expression))
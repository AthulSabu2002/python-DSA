def infixToPostFix(expression: str) -> str:
    precedence = {'+': 1, '-': 1, '/': 2, '*': 2, '(': 0, '^': 3}
    stack = []
    postfix = []
    
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence[stack[-1]] >= precedence[char]:
                postfix.append(stack.pop())
            stack.append(char)
        
    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)



expression = "a+b*(c^d-e)^(f+g*h)-i"
print(infixToPostFix(expression))
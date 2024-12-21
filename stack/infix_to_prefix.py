def infixToPreFix(expression: str) -> str:
    expression = expression[::-1]
    precedence = {'+': 1, '-': 1, '/': 2, '*': 2, '^': 3, '(': 0, ')': 0}
    stack = []
    postfix = []
    
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence[stack[-1]] > precedence[char]:
                postfix.append(stack.pop())
            stack.append(char)
        
    while stack:
        postfix.append(stack.pop())
    
    postfix.reverse()

    return ''.join(postfix)



expression = "x+y*z/w+u"
print(infixToPreFix(expression))
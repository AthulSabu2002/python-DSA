def balanced_or_not(str):
    stack = []    
    index = 0
    balanced = True
    
    while index < len(str) and balanced:
        if str[index] in "[{(":
            stack.append(str[index])
        else:
            if not stack:
                balanced = False
            else:
                temp = stack.pop()
                if str[index] == ')' and temp != '(':
                    balanced = False
                elif str[index] == '}' and temp != '{':
                    balanced = False
                elif str[index] == ']' and temp != '[':
                    balanced = False
        index = index + 1
    
    if not stack and balanced:
        print("The brackets are balanced.")
    else:
        print("The brackets are not matched!")
    
    return 0

str = input("Enter the string: ")
balanced_or_not(str)
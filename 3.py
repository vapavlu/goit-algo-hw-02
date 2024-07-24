def is_balanced(expression):
    stack = []
    opening_brackets = '([{'
    closing_brackets = ')]}'
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return False
    return not stack

# Приклади використання
print(is_balanced("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # True (Симетрично)
print(is_balanced("( 23 ( 2 - 3);"))  # False (Несиметрично)
print(is_balanced("( 11 }"))  # False (Несиметрично)

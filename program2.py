def is_balanced_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return len(stack) == 0


# Test cases
test_cases = ["()", "(())", "(()", "())(", "", "((()))"]
for s in test_cases:
    print(f"{s}: {'Accepted' if is_balanced_parentheses(s) else 'Rejected'}")

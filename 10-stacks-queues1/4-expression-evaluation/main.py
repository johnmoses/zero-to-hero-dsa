# Expression Evaluation - Python Example

def evaluate_postfix(expr):
    stack = []
    for token in expr.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
    return stack[0]

expr = "3 4 2 * 1 5 - 2 3 ^ ^ / +"
print(f"Result of postfix expression: {evaluate_postfix(expr)}")

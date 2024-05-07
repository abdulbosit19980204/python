expression = "6 4 + 2 * 3 + 2 + 4 7 + 2 * 2 + *"
result = []
for i in expression.split():
    if i.isdigit():
        result.append(int(i))
    elif i == '+':
        op2 = result.pop()
        op1 = result.pop()
        result = op1 + op2
        result.append(result)
        print(result)
    elif i == '-':
        op2 = result.pop()
        op1 = result.pop()
        result = op1 - op2
        result.append(result)
        print(result)
    elif i == '*':
        op2 = result.pop()
        op1 = result.pop()
        result = op1 * op2
        result.append(result)
        print(result)
    else:
        raise ValueError(f"Недопустимый значикение: {i}")

print("Ответ", result)
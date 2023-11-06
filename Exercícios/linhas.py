def number(lines):
    return [f'{i + 1}: {lines[i]}' for i in range(len(lines))]

print(number(list(range(1, 6))))
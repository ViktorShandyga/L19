def divider(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if a < b:
        raise ValueError("a is less than b")
    if b > 100:
        raise IndexError("b is greater than 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(key, value)
        res.append(res)
    except Exception as e:
        print(f"Error for pair ({key}, {value}): {e}")

print("Result:",)

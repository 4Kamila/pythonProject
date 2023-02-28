result = []
def divider(a, b):
    try:
        return a / b
    except(ZeroDivisionError):
        print("Division by Zero")
        return 0
    except(ValueError):
        print("ValueError")
        return 0
    except(TypeError):
        print("TypeError")
        return 0


data = {10: 2, 2: 5, "123": 4, 18: 0, 6: 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)


print(result)
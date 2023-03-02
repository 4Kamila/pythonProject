# def __init__(self, number):
#     self.a = 0
#     self.number = number
# def __iter__(self):
#     self.a = 0
#     return self
# def generator (number, max_number):
#     a = 0
#     for _ in range:
#         yield number**a
#         a+=2
# def __next__():
#     return generator
# res = generator(124568, 800)
# print(res)
# for _ in res:
#     print(_)
def checker(*exc_types):
    def checker(function):
        def checker(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except (exc_types) as exc:
                print(f"We have problems {exc}")
            else:
                print(f"No problems. Result – {result}")
        return checker
    return checker
@checker(NameError, TypeError, SyntaxError, ZeroDivisionError)
def calculate(expression):
    a = float(input("a = "))
    b = float(input("b = "))
    c = input("sign: ")
    if c == "+":
        r = a + b
        print(a, '+', b, '=', r)
    elif c == "-":
        m = a - b
        print(a, '-', b, '=', m)
    elif c == "*":
        l = a * b
        print(a, '*', b, '=', l)
    elif c == "/":
        h = a * b * c * d
        print(a, '/', b, '=', h)
    else:
        print("Виберіть іншу дію!")
    return eval(expression)
calculate("5*5")

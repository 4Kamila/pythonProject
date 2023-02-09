# try:
#     print("Hello")
# except:
#     print("We have a problem")
# else:
#     print("no problems")

# try:
#     print("Hello")
#     print("no problems")
# except NameError as error:
#     print(error)
# else:
#     print("no problems")
# finally:
#     print("Finally code")

# def checker(var_1):
#     if type(var_1) != str:
#         raise TypeError(f"Sorry, we can't work with {type(var_1)}")
#     else:
#         return print(var_1)
# first_var = "10"
# checker(first_var)

# import  warnings
# warnings.warn("Warning, no code here", SyntaxWarning)

# import warnings
# warnings.simplefilter("ignore", SyntaxWarning)
# warnings.simplefilter("always", ImportWarning)
#
# warnings.warn("Warning, no code here", SyntaxWarning)
# warnings.warn("Warning, module not import", ImportWarning)

a = int(input("a = "))
b = int(input("b = "))
try:
    print(a*b)
except:
    print("error")
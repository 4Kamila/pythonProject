import logging
# logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w",format="We have next logging message: "
#                                                                                     "%(asctime)s:%(levelname)s-%(message)s")
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")
# try:
#     print(10/0)
# except Exception:
#     logging.exception("Exception")

# assert 2+2 == 5,"wrong assert"

# """
# >>> 2+2
# 5
# """
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
# """
# >>> 2+2
# 5
# """
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

# """
# >>>2+2*2
# 8
# """
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
    return result
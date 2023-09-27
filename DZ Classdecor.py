
class Power:
    def __init__(self, p):
        self.pow = p

    def __call__(self, fn):
        def wrap(x, y):
            return fn(x, y) ** self.pow

        return wrap


@Power(3)
def multiply(a, b):
    return a * b


print(multiply(2, 2))

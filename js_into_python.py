import math

class console:
    def log(*args, **kwargs):
        print(*args, **kwargs)


class Math:
    def round_(x):
        return round(x)
    
    def sin(x):
        return math.sin(x)
    
    def pow_(x, y):
        return math.pow(x, y)
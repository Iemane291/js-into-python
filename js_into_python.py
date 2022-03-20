import math
import random
import numpy

from typing import Union

true = True
false = False

class console:
    def log(*args, **kwargs):
        print(*args, **kwargs)


class Math:
    def round_(x: Union[int, float]):
        return round(x)
    
    def sin(x: Union[int, float]):
        return math.sin(x)
    
    def pow_(x: Union[int, float], y: Union[int, float]):
        return math.pow(x, y)
    
    def ceil(x: Union[int, float]):
        return math.ceil(x)

    def floor(x: Union[int, float]):
        return math.floor(x)
    
    def trunc(x: Union[int, float]):
        return int(x)
    
    def sign(x: Union[int, float]):
        if x > -1:
            return True
        elif x < 0:
            return False
        
    def min_(*args: Union[int, float], **kwargs: Union[int, float]):
        checkedContainer = list(*args, **kwargs)
        return min(checkedContainer)
    
    def max_(*args: Union[int, float], **kwargs: Union[int, float]):
        checkedContainer = list(*args, **kwargs)
        return max(checkedContainer)
    
    def random():
        return random.random()
    
    def log(x: Union[int, float]):
        return numpy.log(x)
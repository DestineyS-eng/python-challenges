#this will always return the number so that it can be used as symbol is always equal to None
def zero(symbol=None):
    if symbol is None:
        return 0
    return symbol(0)
def one(symbol=None):
    if symbol is None:
        return 1
    return symbol(1)
def two(symbol=None):
    if symbol is None:
        return 2
    return symbol(2)
def three(symbol=None):
    if symbol is None:
        return 3
    return symbol(3)
def four(symbol=None):
    if symbol is None:
        return 4
    return symbol(4)
def five(symbol=None):
    if symbol is None:
        return 5
    return symbol(5)
def six(symbol=None):
    if symbol is None:
        return 6
    return symbol(6)
def seven(symbol=None):
    if symbol is None:
        return 7
    return symbol(7)
def eight(symbol=None):
    if symbol is None:
        return 8
    return symbol(8)
def nine(symbol=None):
    if symbol is None:
        return 9
    return symbol(9)
#the innermost number is stored in right_num
#this is then used in a new inner function which adds/times/divides/subtracts the right_num and the outermost number stored in left_num
def plus(right_num):
    def symbol(left_num):
        return left_num + right_num
    return symbol
def minus(right_num):
    def symbol(left_num):
        return left_num - right_num
    return symbol
def times(right_num):
    def symbol(left_num):
        return left_num * right_num
    return symbol
def divided_by(right_num):
    def symbol(left_num):
        return left_num//right_num
    return symbol

def add(x, y):
    return x + y 
def substract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def devide(x, y):
    if y == 0:
        raise ValueError("Tidak diizinkan membagi dengan Nol")
    return x / y

def sum(a: int, b:int):
    """This function takes two integer parameter
    and returns the sum of two integers"""
    return a + b


def greet(name: str):
    """This function takes a string parameter
    and returns a greeting message"""
    return "hello" + " " + name

def say_bye(name: str):
    """This function takes a string parameter
    and returns a farewell message"""
    return "bye" + " " + name

def good_morning(name: str):
    """This function takes a string parameter
    and returns a good morning message"""
    return "good morning" + " " + name



def my_factorial(n):
    fact = 1
    for i in range(n , 0 , -1):
        fact = fact * i
    
    return fact

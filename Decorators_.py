#decorator is a fucntion that takes a function then it creates a new func inside its body (Wrapper). Then it returns the new function

def decorator(func):
    def wrapper():
        print("before function call")
        func() # f
        print("after function call")
    return wrapper

@decorator
def say_hello():
    print("hello !")

say_hello()
# f = decorator(say_hello)
# f()


#How f will look like
'''
def f():
    print("Before function call");
    print("Hello !");
    print("After Function Call"); 
'''
# Function definitions and calls
# 1 spell function
def addOne(nb):
    return nb + 1
print(addOne(5))  # This will print 6
def square (nb):
    return nb ** 2
print(square(4))  # This will print 16


# 2 spell function
def addition(a,b):
    return a+b 
print(addition(10,30))  # This will print 40

def mutliplication(a,b):
    return a*b
print(mutliplication(5,6))  # This will print 30


def ispalindrome(w):
    return w == w[::-1]
print(ispalindrome("radar"))  # This will print True
print(ispalindrome("hello"))  # This will print False
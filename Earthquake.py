# D.R.Y. = don't repeat yourself 
# W.E.T. Write Everything Twice 
def greeting(): 
    name = raw_input("What is your name? ")
    print "Hello, " + name

def hello(name):
    print "Hello, " + name 
def add(a, b):
    return a + b
    
hello("Tim")

print add(2, 3) + add(4, 5)




""" Implementing a simple calculator """
def filename():
    return(__name__)
def add(x,y):
    '''
    This function adds two numbers
    '''
    return(x+y)

def subtract(x,y):
    '''
    This function subtracts two numbers
    '''
    return(x-y)

def multiply(x,y):
    return(x*y)

def divide(x,y):
    if y!=0:
        return(x/y)
    else:
        print("Zero Divide")

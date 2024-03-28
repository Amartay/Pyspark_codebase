#installing retry Decorator
pip install retry
#intializaing global variable for testing
c = 0
from retry import retry

#retry decorator with 3 tries
@retry(tries=3)
def add(a,b):
    global c
    if a%2 ==0:
        raise Exception("Even")
    else:
        c= c + 1
        return a+b

#calling functions    
print(add(3,10))
#check value of 3 for retries
print(c)

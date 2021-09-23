#GENERATOR
def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    
    while True:
        yield a
        a, b = b, a + b
count=0
f=fibonacci()
for x in f:
    print x
    if count>=10:
        break
    count+=1
def GEN2(x):
    x=100
    k=100
    while k>10:
        yield x
        x+=1
        
        k-=1
        
    
l=GEN2(77)
for x in l:
    print x
def Factorial(x):
    k=1
    while x>0:
        yield k,x
        k=k*x
        x-=1
       
       
x=Factorial(10)
for l in x:
    print l

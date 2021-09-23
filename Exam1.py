import sys
f=open("Student.txt",'r')
'''line=f.readlines()
try:
    sys.stdout.write(line)
except:
    print "WAGATTA" '''
k=f.readline()
print k
print f.tell()
f.seek(0,0)
k=f.read()
print k                  #KEEPS GOING FORWARD
print f.tell()
f.seek(5)
print f.tell()
print k

words=k.split()
print words
o=sys.stdin.readline()
print o

f.close()

f2=open("Student.txt",'a')
f2.seek(9)
f2.write("YA")

f2.close()

f=open("Student.txt",'r')

k=f.read()
print k

while True:
    try:
        x=input("Enter a nubmer")
        break
    except:
        print "NOt a number"
print x+1

def GEN(x):
    n=input("Enter max value")
    while n>=x:
        print x
        x+=1
GEN(x)




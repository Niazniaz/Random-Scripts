#Program that adds after copying to another file
import os
f=open("Wagatta.txt",'r')
x=input("Enter line where to input")
cont=f.readlines()
k=cont[0:x]
f.close()
f2=open("Temp.txt",'w')
f2.writelines(k)
li=input("Enter line")
f2.write(li)
f2.writelines(cont[x:len(cont)])
f2.close()
os.remove("Wagatta.txt")
os.rename("Temp.txt","Wagatta.txt")

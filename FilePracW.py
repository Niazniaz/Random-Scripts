# -*- coding: cp1252 -*-
with open("Ex.txt",'w') as f:
    f.writelines(["Neither apple nor pine are in pineapple.\n","Boxing rings are square.\n","Writers write, but figures don’t find.\n","Overlook and oversee are opposites.\n","A house can burn up as it burns down.\n","An alarm goes off by going on."])
with open("Ex.txt") as f:
    print '''1.Using Read
2.Using Readlines'''
    ch=input("ENter your choice")
    if ch==1:
        cont=f.read()
        print cont
    elif ch==2:
        lines=f.readlines()
        print lines
with open("Ex.txt") as f:
    arecount=0
    lines=f.readlines()
    for line in lines:
        k=line.strip("\n")
        words=k.split(" ")
        for word in words:
            if word[0].upper()=="O":
                print word
            if word=="are":
                arecount+=1
    print "Arecount is",arecount
    
    

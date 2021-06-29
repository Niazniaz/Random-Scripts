import os
pth="D:/Spectacular Spider-man/Season 1"
oldNames=os.listdir(pth)
pth=pth+"/"
ep="Spectacular Spider-man S1E"
for i in range(1,len(oldNames)+1):
    new=ep+str(i)+".mkv"
    os.rename(pth+oldNames[i-1],pth+new)

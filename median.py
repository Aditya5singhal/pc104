import csv 
with open('HeightWeight.csv',newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newnum=[]
for i in range(len(filedata)):
    

    num=filedata[i][1]
    newnum.append(float(num))

n=len(newnum)
newnum.sort()




median=newnum[n//2]








print(median)



   
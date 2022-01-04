file=open('output.txt',mode='w+')
lst=[1,2,3,4,5]
for i in lst:
 file.write(str(i))
 print(i,file=file)
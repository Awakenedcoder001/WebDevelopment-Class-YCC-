#File Exists in the directory 
def file_write():
    print("Inside file_write Function !!") 
    file_write=open("writing.txt",'w') 
    print("Opened the file for writing !!") 
    file_write.write("Favrouite book : Three Little Pigs") 
    file_write.write("Favourite movie : Ae Dil Hai Mushkil") 
    file_write.write("Favourite actor : Prabhas") 
    file_write.write("Favourite Drinks : Lager") 
    file_write.write("Favourite Footballer : Lionel Messi") 
    print("Written in to the file Successfully !!") 
    file_write.close()
    print("File is Closed Succesfully !!") 
 
#FIle does not exists in the directory 
def file_write1(): 
    print("Inside file_write Function !!") 
    file_write=open("writing1.txt",'w') 
    print("Opened the file for writing !!") 
    file_write.write("Favrouite song :One Last Breath \n") 
    file_write.write("Favourite movie : Shershah \n") 
    file_write.write("Favourite actor : Prabhas \n") 
    file_write.write("Favourite Drinks : Lager \n") 
    file_write.write("Favourite Footballer : Lionel Messi \n") 
    print("Written in to the file Successfully !!") 
    file_write.close() 
    print("File is Closed Succesfully !!") 
 
if __name__== "__main__": 
    print("Inside If Block") 
    file_write() 
    file_write1() 
    print("INside If Block Compelted")
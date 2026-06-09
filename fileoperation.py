#f=open("file.txt","r")
#print(f.read())
#f=open("file.txt","w")
#f.write("This is a new line.")
#f=open("file.txt","a")
#f.write("This is an appended line.")
#f=open("file.txt","x")
#f.write("This is a new file.")
#with open("file.txt","r") as f:#auto close file after block
#    print(f.read())
#import os
#os.remove("file.txt")#delete file
with open("file.txt","r") as f:
    line=0
    for line in f:
        print(line.strip())
        if("gulu" in line):
            print(f"Found! at {line}")
            break
    print(line)
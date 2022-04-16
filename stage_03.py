with open("artifact01.txt","r") as f: 
    text=f.read()

with open("artifact02.txt","w") as f: 
    text=f.write(text+"added lines")
print("end of stage 03")
import glob, os
os.listdir()
os.chdir("img")
files=[]
f= open('train.txt',"w+")
for file in glob.glob("*.jpg"):
    print(str(file))
    f.write("data/img/"+str(file)+"\n")
f.close() 

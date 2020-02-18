import glob, os
os.listdir()
os.chdir("D:/OneDrive/Documentos/GitHub/AgroJetson/yolo-dataset/img")
files=[]
f= open('D:/OneDrive/Documentos/GitHub/AgroJetson/yolo-dataset/train.txt',"w+")
for file in glob.glob("*.jpg"):
    print(str(file))
    f.write("data/img/"+str(file)+"\n")
f.close() 

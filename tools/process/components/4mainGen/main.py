import json,shutil,os
out = []
temp = {}
month = ["01","02","03","04","05","06","07","08","09","10"]
for i in month:
    #print(os.getcwd()+"\\"+i+"\\searchindex.py")
    #shutil.copyfile(os.getcwd()+"\\searchindex.py", os.getcwd()+"\\"+i+"\\searchindex.py")
    #os.system("py "+os.getcwd()+"\\"+i+"\\searchindex.py")
    #os.system("cd "+i)
    #os.system("py searchindex.py")
    #os.remove(os.getcwd()+"\\"+i+"\\searchindex.py")
    with open(i+"/main.json","r",encoding="utf-8")as f:
        temp = json.loads(f.read())
        f.close()
    for i in temp:
        out.append(i)

with open("main.json","w",encoding="utf-8") as f:
    f.write(str(out).replace("'",'"'))
    f.close()
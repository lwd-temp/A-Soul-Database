import requests,os,json,time
HOME = os.getenv("HOME")

def main():
    with open(HOME+"/files.json") as f:
        allChanges = json.loads(f.read())
        f.close()


    result = {
        "time":time.time(),
        "db":False,
        "web":False,
        "tools":False
    }

    for i in allChanges:
        if i.split("/")[0] == "tools":
            result["tools"] = True
        if i.split("/")[0] == "db":
            result["db"] = True
        if i.split("/")[0] == "make-front-end":
            result["web"] = True

    requests.post("",json=result)

main()
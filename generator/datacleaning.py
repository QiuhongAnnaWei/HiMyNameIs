import os

nameList = []

newfilename = "allnames2010-.txt"
dirPath = "./names"
for filename in os.listdir(dirPath):
    # if filename.endswith(".txt"): 
    # if filename[3:6] == "201": 
    if filename.endswith(".txt") and int(filename[3:7]) >= 2015:
        with open(f"{dirPath}/{filename}") as f:
            print(f"Reading {dirPath}/{filename}")
            lines = f.readlines()
            for line in lines:
                nameList.append(line.split(",")[0]+"\n")

with open(f"{newfilename}", "w") as f:
    f.writelines(nameList)
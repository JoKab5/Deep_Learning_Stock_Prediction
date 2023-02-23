import numpy as np

res = []
with open("Google_Stock_Price_Train.csv") as f:
    while (l:=f.readline()) != "":
        if "Date" not in l:
            t = l.split("\"")
            print(t)
            t[1] = t[1].replace(",", "")
            if len(t)>4:
                t[3] = t[3].replace(",","")
            l = "".join(t)
        res.append(l)
with open("Google_Stock_Price_Train.csv", "w") as f:
    for l in res:
        f.write(l)

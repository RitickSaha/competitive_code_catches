distTopings = list()
rateIng = list()
interList = {}
streetList = list()
carPlist = list()
best_way = list()


def addtolist(list):
    for i in range(len(list)):
        if(distTopings.count(list[i]) == 0):
            distTopings.append(list[i])
            rateIng.append(1)
        else:
            rateIng[distTopings.index(list[i])] += 1


class Streets:
    def __init__(self, list, index):
        self.index = index
        self.starts = int(list[0])
        print(self.starts)
        self.ends = int(list[1])
        print(self.ends)
        self.sname = list[2]
        print(self.sname)
        self.time = int(list[3])
        print(self.time)


class CarPath:
    def __init__(self, list):
        self.paths = int(list[0])
        self.pathList = []
        for i in range(self.paths+1):
            self.pathList.append(list[i])
        print(self.paths, " ", self.pathList)


filelist = [
    "a",
    # "b",
    # "c",
    # "d",
    # "e",
    # "f"
]
for f in filelist:
    oFile = open(f+".out", "w")
    with open(f+".txt", "r") as ifile:
        stim, inter, street, car, score = list(
            map(int, ifile.readline().split()))
        for j in range(street):
            s = Streets(ifile.readline().split(), j)
            streetList.append(s)
            interList[str(s.ends)] = interList[str(s.ends)].concat(s.sname) if (interList[str(s.ends)] != None) else [s.sname]
        # print(interList)
        # for j in range(car):
        #     carPlist.append(CarPath(ifile.readline().split()))
        # findCarPath = []
        # tStim = stim
        # for h in [carPlist[0]]:
        #     findCarPath.clear()
        #     for i in h.pathList:
        #         for j in streetList:
        #             if(j.sname == i):
        #                 findCarPath.append(j)
        #     findCarPath.pop()
        #     outInter = []
        #     outtime = []
        #     for x in findCarPath:
        #         if(tStim > 0):
        #             outInter.append(x)
        #             outtime.append(x.time)
        #             tStim -= (x.time)
        #     oFile.write(str(len(outInter))+"\n")
        #     for x in outInter:
        #         oFile.write(str(x.index)+"\n")
        #         oFile.write(str(1)+"\n")
        #         oFile.write(x.sname + " " + str(x.time)+"\n")

        # best_way.append([plist[i].score, plist[i].index])
        #         print(best_way)
        #         best_way=sorted(best_way,key=lambda kv:(kv[0]),reverse=True)
        #         ctr=nopiz
        #         delieverto=0
        #         d=[]
        # # /////////////////////////////////////////////////////////////////////////////#
        # # /////////////////////////////////ALGO////////////////////////////////////////#
        # # /////////////////////////////////////////////////////////////////////////////#
        #         for j in range(t2):
        #             if(len(best_way)>=2):
        #                 delieverto+=1
        #                 dd=list()
        #                 dd.append(2)
        #                 dd.append(best_way[0][1])
        #                 best_way.pop(0)
        #                 dd.append(best_way[len(best_way)-1][1])
        #                 best_way.pop(len(best_way)-1)
        #                 d.append(dd)
        #             else:
        #                 break
        #         for j in range(t3):
        #             if(len(best_way)>=3):
        #                 delieverto+=1
        #                 dd=list()
        #                 dd.append(3)
        #                 dd.append(best_way[0][1])
        #                 best_way.pop(0)
        #                 dd.append(best_way[0][1])
        #                 best_way.pop(0)
        #                 dd.append(best_way[len(best_way)-1][1])
        #                 best_way.pop(len(best_way)-1)
        #                 d.append(dd)
        #             else:
        #                 break
        #         for j in range(t4):
        #             if(len(best_way)>=3):
        #                 delieverto+=1
        #                 dd=list()
        #                 dd.append(4)
        #                 dd.append(best_way[0][1])
        #                 best_way.pop(0)
        #                 dd.append(best_way[0][1])
        #                 best_way.pop(0)
        #                 dd.append(best_way[len(best_way)-2][1])
        #                 best_way.pop(len(best_way)-2)
        #                 dd.append(best_way[len(best_way)-1][1])
        #                 best_way.pop(len(best_way)-1)
        #                 d.append(dd)
        #             else:
        #                 break
        # # /////////////////////////////////////////////////////////////////////////////#
        # # /////////////////////////////////ALGO 1//////////////////////////////////////#
        # # /////////////////////////////////////////////////////////////////////////////#
        #         # while(len(best_way)>0):
        #         #     if(len(best_way)>=2):
        #         #         delieverto+=1
        #         #         dd=list()
        #         #         dd.append(2)
        #         #         dd.append(best_way[0][1])
        #         #         best_way.pop(0)
        #         #         dd.append(best_way[len(best_way)-1][1])
        #         #         best_way.pop(len(best_way)-1)
        #         #         d.append(dd)
        #         #     else:
        #         #         break
        #         #     if(len(best_way)>=3):
        #         #         delieverto+=1
        #         #         dd=list()
        #         #         dd.append(3)
        #         #         dd.append(best_way[0][1])
        #         #         best_way.pop(0)
        #         #         dd.append(best_way[0][1])
        #         #         best_way.pop(0)
        #         #         dd.append(best_way[len(best_way)-1][1])
        #         #         best_way.pop(len(best_way)-1)
        #         #         d.append(dd)
        #         #     else:
        #         #         break
        #         #     if(len(best_way)>=3):
        #         #         delieverto+=1
        #         #         dd=list()
        #         #         dd.append(4)
        #         #         dd.append(best_way[0][1])
        #         #         best_way.pop(0)
        #         #         dd.append(best_way[0][1])
        #         #         best_way.pop(0)
        #         #         dd.append(best_way[len(best_way)-2][1])
        #         #         best_way.pop(len(best_way)-2)
        #         #         dd.append(best_way[len(best_way)-1][1])
        #         #         best_way.pop(len(best_way)-1)
        #         #         d.append(dd)
        #         #     else:
        #         #         break
        #         oFile.writelines(str(delieverto)+"\n")
        #         for l in d:
        #             for p in l:
        #                 oFile.write(str(p)+" ")
        #             oFile.write("\n")

distTopings=list()
rateIng=list()
pizzaRate=list()
plist=list()
best_way=list()
def addtolist(list):
    for i in range(len(list)):
        if(distTopings.count(list[i])==0):
            distTopings.append(list[i])
            rateIng.append(1)
        else:
            rateIng[distTopings.index(list[i])]+=1

def ratepizza(list,nopiz):
    x=0
    for j in range(nopiz):
        x=0
        for i in plist[j].topings:
            x+=rateIng[distTopings.index(i)]
        plist[j].score = x

class Pizzawt:
    def __init__(self,list):
        self.no = name=int(list[0])
        list.remove(list[0])
        self.topings =list
        addtolist(list)
        self.score=0
        self.index=len(plist)
    def test(self):
        print(self.no,self.topings)
filelist=[
    "a_example",
    "b_little_bit_of_everything",
    "c_many_ingredients",
    "d_many_pizzas",
    "e_many_teams"
]   
for f in filelist:
    oFile=open(f+".out", "w")
    with open(f+".in","r") as ifile:
        nopiz,t2,t3,t4=list(map(int,ifile.readline().split()))
        rated=range(nopiz)
        for j in range(nopiz):
            plist.append(Pizzawt(ifile.readline().split()))
        ratepizza(plist,nopiz)
        for i in range(nopiz):
            best_way.append([plist[i].score,plist[i].index])
        print(best_way)
        best_way=sorted(best_way,key=lambda kv:(kv[0]),reverse=True)
        ctr=nopiz
        delieverto=0
        d=[]
# /////////////////////////////////////////////////////////////////////////////#
# /////////////////////////////////ALGO////////////////////////////////////////#
# /////////////////////////////////////////////////////////////////////////////#
        for j in range(t2):
            if(len(best_way)>=2):
                delieverto+=1
                dd=list()
                dd.append(2)
                dd.append(best_way[0][1])
                best_way.pop(0)
                dd.append(best_way[len(best_way)-1][1])
                best_way.pop(len(best_way)-1)
                d.append(dd)
            else:
                break
        for j in range(t3):
            if(len(best_way)>=3):
                delieverto+=1
                dd=list()
                dd.append(3)
                dd.append(best_way[0][1])
                best_way.pop(0)
                dd.append(best_way[0][1])
                best_way.pop(0)
                dd.append(best_way[len(best_way)-1][1])
                best_way.pop(len(best_way)-1)
                d.append(dd)
            else:
                break
        for j in range(t4):
            if(len(best_way)>=3):
                delieverto+=1
                dd=list()
                dd.append(4)
                dd.append(best_way[0][1])
                best_way.pop(0)
                dd.append(best_way[0][1])
                best_way.pop(0)
                dd.append(best_way[len(best_way)-2][1])
                best_way.pop(len(best_way)-2)
                dd.append(best_way[len(best_way)-1][1])
                best_way.pop(len(best_way)-1)
                d.append(dd)
            else:
                break
# /////////////////////////////////////////////////////////////////////////////#
# /////////////////////////////////ALGO 1//////////////////////////////////////#
# /////////////////////////////////////////////////////////////////////////////#
        # while(len(best_way)>0):
        #     if(len(best_way)>=2):
        #         delieverto+=1
        #         dd=list()
        #         dd.append(2)
        #         dd.append(best_way[0][1])
        #         best_way.pop(0)
        #         dd.append(best_way[len(best_way)-1][1])
        #         best_way.pop(len(best_way)-1)
        #         d.append(dd)
        #     else:
        #         break
        #     if(len(best_way)>=3):
        #         delieverto+=1
        #         dd=list()
        #         dd.append(3)
        #         dd.append(best_way[0][1])
        #         best_way.pop(0)
        #         dd.append(best_way[0][1])
        #         best_way.pop(0)
        #         dd.append(best_way[len(best_way)-1][1])
        #         best_way.pop(len(best_way)-1)
        #         d.append(dd)
        #     else:
        #         break
        #     if(len(best_way)>=3):
        #         delieverto+=1
        #         dd=list()
        #         dd.append(4)
        #         dd.append(best_way[0][1])
        #         best_way.pop(0)
        #         dd.append(best_way[0][1])
        #         best_way.pop(0)
        #         dd.append(best_way[len(best_way)-2][1])
        #         best_way.pop(len(best_way)-2)
        #         dd.append(best_way[len(best_way)-1][1])
        #         best_way.pop(len(best_way)-1)
        #         d.append(dd)
        #     else:
        #         break
        oFile.writelines(str(delieverto)+"\n")
        for l in d:
            for p in l: 
                oFile.write(str(p)+" ")
            oFile.write("\n")
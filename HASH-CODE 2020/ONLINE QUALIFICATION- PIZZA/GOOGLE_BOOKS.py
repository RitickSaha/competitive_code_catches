class Library(object):
    def __init__(self,bookInLib,signup,shipLimit,booklist):
        self.bookInLib=bookInLib
        self.signup=signup
        self.shipLimit=shipLimit
        self.booklist=booklist
def getList(dict):
    listind=[]
    i=0
    sums=0
    while(i<len(dict) and sums<daysFrScan):
        sums+=dict[i][2]
        listind.append(dict[i][0])
        i+=1 
    # listind.sort()
    return listind
#DATA SET READING AND OBJECT CREATION
# oFile=open("a_example.out", "w")
# with open("a_example.txt","r") as ifile:
oFile=open("b_read_on.out", "w")
with open("b_read_on.txt","r") as ifile:
# oFile=open("c_incunabula.out", "w")
# with open("c_incunabula.txt","r") as ifile:
# oFile=open("d_tough_choices.out", "w")
# with open("d_tough_choices.txt","r") as ifile:
# oFile=open("e_so_many_books.out", "w")
# with open("e_so_many_books.txt","r") as ifile:
# oFile=open("f_libraries_of_the_world.out", "w")
# with open("f_libraries_of_the_world.txt","r") as ifile:
    totalBooks,totalLib,daysFrScan=list(map(int,ifile.readline().split()))
    bookScore=list(map(int,ifile.readline().split()))
    librarylist=list()
    for i in range(0,totalLib):
        booklist=list()
        a,b,c=list(map(int,ifile.readline().split()))
        booklist.append(list(map(int,ifile.readline().split())))
        library=Library(a,b,c,booklist)
        librarylist.append(library)
scoresame=0
sameSignup=0
dayslist=list()
temp=list()
bookslst=list()
index=-1
prevtotalbook=0
limit=[]
best_way=[]
nobklist=[]
for i in range(0,totalLib):
    best_way.append([i,
                    librarylist[i].bookInLib,
                    librarylist[i].signup,
                    librarylist[i].shipLimit])
    nobklist.append(librarylist[i].bookInLib)
    dayslist.append(librarylist[i].signup)
    limit.append(librarylist[i].shipLimit)
best_way=sorted(best_way,key=lambda kv:(kv[1]),reverse=False)
best_way=sorted(best_way,key=lambda kv:(kv[3]),reverse=False)
best_way=sorted(best_way,key=lambda kv:(kv[2]),reverse=False)
scoresame=len(list(dict.fromkeys(bookScore)))
nobkcheck=len(list(dict.fromkeys(nobklist)))
sameSignup=len(list(dict.fromkeys(dayslist)))
samelimit=len(list(dict.fromkeys(limit)))
bestindex=list(getList(best_way))
length=len(str(len(bestindex))+"\n")
oFile.write(str(len(bestindex))+"\n")
finalScore=0
finalbooklist=[]
signupthresh=0
count=0
print(len(bestindex))
for i in bestindex:
    tempbooklist=[]
    signupthresh+=librarylist[i].signup
    x=0
    if(scoresame==1 and sameSignup==1):
        while(x<=(librarylist[i].shipLimit)*(daysFrScan-signupthresh-1) and x<=librarylist[i].bookInLib-1 and x<=daysFrScan-signupthresh):
            tempbooklist=librarylist[i].booklist[0]
            finalbooklist+=tempbooklist
            x+=1
    elif(scoresame==1 and sameSignup==1 and nobkcheck):
        while(x<=(librarylist[i].shipLimit)*(daysFrScan-signupthresh-1) and x<=librarylist[i].bookInLib-1 and x<=daysFrScan-signupthresh):
            tempbooklist=librarylist[i].booklist[0][0:len(librarylist[i].booklist[0])-signupthresh]
            finalbooklist+=tempbooklist
            x+=1
    elif(scoresame==1):
        for dele in finalbooklist:
            if dele in librarylist[i].booklist[0]:
                librarylist[i].booklist[0].remove(dele)
        while(x<=(librarylist[i].shipLimit)*(daysFrScan-signupthresh-1) and x<=librarylist[i].bookInLib-1 and x<=daysFrScan-signupthresh-1):
            tempbooklist=librarylist[i].booklist[0]
            finalbooklist+=tempbooklist
            x+=1
    else:
        librarylist[i].booklist[0]=sorted(librarylist[i].booklist[0],key=lambda kv:(bookScore[kv]),reverse=True)
        for dele in finalbooklist:
            if dele in librarylist[i].booklist[0]:
                librarylist[i].booklist[0].remove(dele)
        if len(librarylist[i].booklist[0])-1>=(librarylist[i].shipLimit)*(daysFrScan-signupthresh-1):
            tempbooklist=librarylist[i].booklist[0][0:((librarylist[i].shipLimit)*(daysFrScan-signupthresh-1))]
            finalbooklist+=tempbooklist
        elif len(librarylist[i].booklist[0])-1<(librarylist[i].shipLimit)*(daysFrScan-signupthresh-1):
            diffrence=(librarylist[i].shipLimit)*(daysFrScan-signupthresh-1)-len(librarylist[i].booklist[0])-1
            tempbooklist=librarylist[i].booklist[0][0:(((librarylist[i].shipLimit)*(daysFrScan-signupthresh-1))-diffrence)]
            finalbooklist+=tempbooklist
        elif daysFrScan-signupthresh-1>=len(librarylist[i].booklist[0])-1:
            tempbooklist=librarylist[i].booklist[0][0:(len(librarylist[i].booklist[0])-1)]
            finalbooklist+=tempbooklist
        else:
            tempbooklist=librarylist[i].booklist[0][0:(daysFrScan-signupthresh-1)]
            finalbooklist+=tempbooklist
    tempbooklist=list(dict.fromkeys(tempbooklist))
    if len(tempbooklist)==0:
        count+=1
    if len(tempbooklist)!=0:
        oFile.writelines(str(i)+" "+str(len(tempbooklist))+"\n")
        for l in range(0,len(tempbooklist)):
            oFile.write(str(tempbooklist[l])+" ")
        oFile.write("\n")
    print('[',tempbooklist,end="]")

summ=0
print("\n",finalbooklist)
if count>0:
    oFile.seek(0,0)
    oFile.write(str(len(bestindex)-count)+" "*(length-1-len(str(len(bestindex)-count)))+"\n")
for f in finalbooklist:
    summ+=bookScore[f]
print(summ)
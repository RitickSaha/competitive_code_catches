class Case(object):
    def __init__(self,p,n,mainsi):
        self.p=p
        self.n=n

        self.mainsi=mainsi
T=int(input())
caselist=list()
n=0
k=0
p=0
  
def ans(j,idx,taken):
    ans=0
    val=0
    if(taken==-1):
        return 0
    if taken<-1:
        return -2e9
    if(idx>n):
        return 0
    if(ans!=-1):
        return ans
    for i in range(len(caselist[j].mainsi[idx])):
        val+=caselist[j].mainsi[idx][i]
        print("ans",ans)
        ans=max(ans,val+[ans(idx+1,taken-1)])
    return ans

for i in range(T):
    mainsi=list()
    n,k,p=list(map(int,input().split()))
    for k in range(n):
        si=list(map(int,input().split()))
        mainsi.append(si)
    case=Case(p,n,mainsi)
    caselist.append(case)
for i in range(T):
    anss=ans(i,0,p)
    print("Case #",i+1,": ",anss,end="\n")
  

"""
2
2 4 5
10 10 100 30
80 50 10 50
3 2 3
80 80
15 50
20 10
"""

class Datacenter(object):
    def __init__(self,ms,conCache,cachelist):
        self.ms=ms
        self.conCache=conCache
        self.cachelist=cachelist
class Cache(object):
    def __init__(self,conCasheInd,cacheLatMs):
        self.conCasheInd=conCasheInd
        self.cacheLatMs=cacheLatMs
with open("me_at_the_zoo.in","r") as ifile:
    vid,end,req,cacheSrvr,capPerSrvr=list(map(int,ifile.readline().split()))
    sizeOfVid=list(map(int,ifile.readline().split()))
    dataCenterlist=list()
    requestlist=list()
    for i in range(0,end):
        cachelist=list()
        ltency,noOfSrvr=(list(map(int,ifile.readline().split())))
        for j in range(0,noOfSrvr):
            srvrId,srvrlatancy=list(map(int,ifile.readline().split()))
            cache=Cache(srvrId,srvrlatancy)
            cachelist.append(cache)
        datacenter=Datacenter(ltency,noOfSrvr,cachelist)
        dataCenterlist.append(datacenter)
    for i in range(0,req):
        requestlist.append(list(map(int,ifile.readline().split())))

# print("Videos=",vid,"\tendpoint=",end,"\trequests=",req,"\tno of cashe servers:",cacheSrvr,"\cap per server=",capPerSrvr)
# for k in range(0,end):
#     print(  "Datacenter index 0:",
#             "\n\tms:=",
#             dataCenterlist[k].ms,
#             "\n\tConected caches:",
#             dataCenterlist[k].conCache)
#     print("\t\tAll conected cashe server to data center")
#     for i in range(0,dataCenterlist[k].conCache):
#         print("The latency (of endpoint ",k,") to cache",dataCenterlist[k].cachelist[i].conCasheInd, "is",dataCenterlist[k].cachelist[i].cacheLatMs)

    
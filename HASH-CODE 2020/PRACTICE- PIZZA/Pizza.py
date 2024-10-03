# ofile=open("a_example.out","w")
# iFile=open("a_example.in", "rt")
# ofile=open("b_small.out","w")
# iFile=open("b_small.in", "rt")
# ofile=open("c_medium.out","w")
# iFile=open("c_medium.in", "rt")
ofile=open("d_quite_big.out","w")
iFile=open("d_quite_big.in", "rt")
# ofile=open("e_also_big.out","w")
# iFile=open("e_also_big.in", "rt")
iMaxS,iTypeS = list(map(int, iFile.readline().split()))
iTypeList = list(map(int, iFile.readline().split()))
max_sum=appi=appj=i=0
oTypeList=[]
iTypeList.reverse()
while i < len(iTypeList):
    temp_sum = 0
    temp_arr = []
    temp_count = 0
    for k in range(i,len(iTypeList)):
        if iTypeList[k]+temp_sum <= iMaxS:
            temp_sum += iTypeList[k]
            temp_arr.append(len(iTypeList)-1-k)
            temp_count += 1
    if max_sum<temp_sum:
        max_sum = temp_sum
        oTypeList = temp_arr
        count = temp_count
    i+=1
lastind=oTypeList[len(oTypeList)-1]
lstminfound=rem=iMaxS-max_sum
iTypeList.reverse()
oTypeList.reverse()
sums=0
for i in oTypeList:
    sums=sums+iTypeList[i]
def find(rem,lastind,tofound,sums):
    appj=-1
    appi=-1
    sum=sums
    tofound=iTypeList[lastind]+rem
    for i in range(lastind,0,-1):
        j=i-1
        for j in range(i,0,-1):
            finding=iTypeList[i]+iTypeList[j]
            if finding>tofound:
                continue
            tempsums=(sum-iTypeList[lastind])+finding
        
            if i not in oTypeList and j not in oTypeList:
                if tempsums==iMaxS:
                    rem=iMaxS-sums
                    appi=i
                    appj=j
                    return appi,appj
                elif tempsums>sums and tempsums<=iMaxS:
                    print("tempsum=",sum,"-",iTypeList[lastind],"+",finding,"=",tempsums)
                    sums=tempsums
                    rem=tofound-finding
                    appi=i
                    appj=j
    return appi,appj
if max_sum !=iMaxS:
    index=0
    while index<len(oTypeList):
        if rem==0:
            break
        tofound=iTypeList[oTypeList[index]]+rem
        appi,appj,=find(rem,oTypeList[index],tofound,sums)
        if appi!=-1 and appj!=-1:
            sums=(sums-iTypeList[oTypeList[index]])+iTypeList[appi]+iTypeList[appj]
            rem=iMaxS-sums
            oTypeList.remove(oTypeList[index])
            oTypeList.append(appi)
            oTypeList.append(appj)
            oTypeList.sort()
            index=0
        index+=1

ofile.write(str(len(oTypeList))+"\n")
for i in oTypeList:
    ofile.write(str(i)+" ")
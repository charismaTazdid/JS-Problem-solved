# Problem: https://www.hackerrank.com/challenges/toll-cost-digits


import sys
import itertools as it

n,e = input().strip().split(' ')
n,e = [int(n),int(e)]
connections =[]
for a0 in range(e):
    x,y,r = input().strip().split(' ')
    x,y,r = [int(x),int(y),int(r)]
    connections.append([x-1,y-1,r%10])
nNodes = n
nCon = e

Paths = {m:[] for m in range(nNodes)}
for i1 in connections:
    Paths[i1[0]].append((i1[1],i1[2]))
    Paths[i1[1]].append((i1[0],(10-i1[2])%10))   
    
StartNodeSet = set([m for m in range(nNodes)])    
TollSumFromZero = {m:set() for m in range(nNodes)}
CombDict = {}
MasterOut = [0 for m in range(10)]

def CombineSetPair(Comb):
    Out = [0 for m in range(10)]
    for i1 in Comb[0]:
        for i2 in Comb[1]:
            Out[(i1-i2)%10] = 1
    return Out

while len(StartNodeSet) > 0:
    SubGraphNodes = set()
    StartNode = StartNodeSet.pop()
    SubGraphNodes.add(StartNode)
    StartIterList = []    
    for i1 in Paths[StartNode]:
        if i1[1] not in TollSumFromZero[i1[0]]:
            TollSumFromZero[i1[0]].add(i1[1])
            StartIterList.append(i1)
            
    
    
    SIListNew = []
    #DenseGraph = False
#    Count = 0
    while len(StartIterList) > 0:# and not DenseGraph:
        for i1 in StartIterList:
            if i1[0] in StartNodeSet:
                StartNodeSet.remove(i1[0])
                SubGraphNodes.add(i1[0])
            for i2 in Paths[i1[0]]:
#                Count += 1
                NewTollDig = (i1[1]+i2[1])%10
                if NewTollDig not in TollSumFromZero[i2[0]]:
                    TollSumFromZero[i2[0]].add(NewTollDig)
    #                if len(TollSumFromZero[i2[0]]) == 10:
    #                    DenseGraph = True
                    SIListNew.append((i2[0],NewTollDig))
        StartIterList = SIListNew
        SIListNew = []
    

    SubgraphDict1 = {}
    for key in SubGraphNodes:
        FD = frozenset(TollSumFromZero[key])
        if SubgraphDict1.get(FD) == None:
            SubgraphDict1[FD] = 1
        else:
            SubgraphDict1[FD] += 1

    for Comb in it.product(SubgraphDict1.keys(),repeat=2):
        if CombDict.get(Comb) == None:
            CombDict[Comb] = CombineSetPair(Comb)
        MultFactor = SubgraphDict1[Comb[0]] * SubgraphDict1[Comb[1]]
        if Comb[0] == Comb[1]:
            MultFactor -= SubgraphDict1[Comb[0]]
#        print(Comb,'___',MultFactor,[m for m in range(10) if CombDict[Comb][m] > 0])
        if MultFactor > 0:
            CD = CombDict[Comb]
            for i1 in range(10):
                MasterOut[i1] += MultFactor * CD[i1]

    
    
for I1,i1 in enumerate(MasterOut):
    print(i1)  

      
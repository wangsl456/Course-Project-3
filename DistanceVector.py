# -*- coding: utf-8 -*-  
from MetroStation import *
from MetroTopo import *
ValueDict = {}
Src = None
Dst = None
Path = []
INFTY = float("inf")
PrePath = {}
MinPath = {}
def filt(string,s):
    resultlist = []
    tmpindex = 0
    preindex = 0
    while True:
        if s in string[preindex:]:
            tmpindex = string[preindex:].index(s)
        else:
            break
        resultlist.append(preindex + tmpindex)
        preindex = preindex + tmpindex + 1
        if preindex >= len(string):
            break
    return resultlist
def Bellman():
    global ValueDict
    global INFTY
    global PrePath
    global Src,Dst
    global MinPath
    while True:
        while True:
            SrcName = raw_input("请输入起点站:".decode('utf-8').encode('gbk'))
            if not (SrcName in StationNameList):
                print "站点名称不正确"
            else:
                break
        while True:
            DstName = raw_input("请输入终点站:".decode('utf-8').encode('gbk'))
            if not (DstName in StationNameList):
                print "站点名称不正确"
            else:
                break
        SrcList = filt(StationNameList,SrcName)
        DstList = filt(StationNameList,DstName)
        for z in range(2):
            for x in range(len(SrcList)):
                for y in range(len(DstList)):
                    iFlag = True
                    Src = SrcList[x]
                    Dst = DstList[y]
                    PreValue = 0
                    PrePath = {}
                    PrePath[Src] = Src
                    for i in range(len(StationList)):
                        ValueDict[StationList[i].Dpid] = 0 if StationList[i].Dpid == Src else INFTY
                    for i in range(len(StationList)):
                        for j in range(len(topo.LinkList)):
                            if(ValueDict[topo.LinkList[j][0]] > (ValueDict[topo.LinkList[j][1]] + TimeCostDictList[z][topo.LinkList[j]])):
                                ValueDict[topo.LinkList[j][0]] = ValueDict[topo.LinkList[j][1]] + TimeCostDictList[z][topo.LinkList[j]]
                                PrePath[topo.LinkList[j][0]] = topo.LinkList[j][1]
                            elif (ValueDict[topo.LinkList[j][1]] > (ValueDict[topo.LinkList[j][0]] + TimeCostDictList[z][topo.LinkList[j]])):
                                ValueDict[topo.LinkList[j][1]] = ValueDict[topo.LinkList[j][0]] + TimeCostDictList[z][topo.LinkList[j]]
                                PrePath[topo.LinkList[j][1]] = topo.LinkList[j][0]
                    if iFlag or (ValueDict[Dst] < PreValue):
                        iFlag = False
                        PreValue = ValueDict[Dst]
                        MinPath = {}
                        MinPath = PrePath
                        _Dst_ = Dst
            if z == 0:
                print "时延最小路线:",
            elif z == 1:
                print "换乘次数最少下，时延最小路线:",
            printpath(_Dst_)
def printpath(root):
    global MinPath
    while root != MinPath[root]:
        print "%s-->" %StationNameList[root],
        root = MinPath[root]
    if root == MinPath[root]:
        print "%s" %StationNameList[root]
if __name__ == '__main__':
    Bellman()
# -*- coding: utf-8 -*-  
from MetroStation import *
from MetroTopo import *
Src = None
Dst = None
Path = []
INFTY = float("inf")
PrePath = {}
MinPath = {}
def FindNearDpidList(dpid,dpidlist):
    ResultDpidList = []
    if not dpidlist:
        return ResultDpidList
    for i in range(len(topo.LinkList)):
        if dpid == topo.LinkList[i][0]:
            if topo.LinkList[i][1] in dpidlist:
                ResultDpidList.append(topo.LinkList[i][1])
        elif dpid == topo.LinkList[i][1]:
            if topo.LinkList[i][0] in dpidlist:
                ResultDpidList.append(topo.LinkList[i][0])
#    print "ResultDpidList"
#    print ResultDpidList
    return ResultDpidList
def FindNearLinkList(dpid,dpidlist):
    ResultLinkList = []
    if not dpidlist:
        return ResultLinkList
    for i in range(len(topo.LinkList)):
        if (dpid == topo.LinkList[i][0]) or (dpid == topo.LinkList[i][1]):
            if (topo.LinkList[i][0] in dpidlist) or (topo.LinkList[i][1] in dpidlist):
                ResultLinkList.append(topo.LinkList[i])
    return ResultLinkList

def FindMinCost(dpidlist,valuedict):
    if not dpidlist:
        return None
    tmp = valuedict[dpidlist[0]]
    tmpIndex = 0
    for i in range(len(dpidlist)):
        if (tmp < valuedict[dpidlist[i]]) or (valuedict[dpidlist[i]] == INFTY):
            pass
        else:
            tmp = valuedict[dpidlist[i]]
            tmpIndex = dpidlist[i]
    return tmpIndex
def dijkstra(dpid_src,dpid_dst,choose):
    global Path,PrePath
    _DpidList_ = []
    oldDpid = dpid_src
    oldValueDict = {}
    ValueDict = {}
    Path = []
    PrePath = {}
    PrePath[dpid_src] = dpid_src
    FirstEnterFlag = True
    for i in range(len(DpidList)):
        Path.append([oldDpid])
    for i in range(len(DpidList)):
        ValueDict[DpidList[i]] = INFTY
        ValueDict[oldDpid] = 0
    oldValueDict = ValueDict
    tmpDpidList = DpidList[:]
    while True:
        _DpidList_.append(oldDpid)
        del tmpDpidList[tmpDpidList.index(oldDpid)]
        if not tmpDpidList:
            break
        NearDpidList = FindNearDpidList(oldDpid,tmpDpidList)
        tmpFunc = lambda x,y:(x,y) if x < y else (y,x)
        for i in range(len(NearDpidList)):
            tmpValue = oldValueDict[oldDpid] + TimeCostDictList[choose][tmpFunc(oldDpid,NearDpidList[i])]
            if oldValueDict[NearDpidList[i]] == INFTY:
                ValueDict[NearDpidList[i]] = tmpValue
                PrePath[NearDpidList[i]] = oldDpid
            elif (oldValueDict[NearDpidList[i]] > tmpValue):
                ValueDict[NearDpidList[i]] = tmpValue
                PrePath[NearDpidList[i]] = oldDpid
        oldValueDict = ValueDict
        tmpMinIndex = FindMinCost(tmpDpidList,oldValueDict)
        oldDpid = tmpMinIndex
    return oldValueDict[dpid_dst]
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
def Dijkstra():
    global ValueDict
    global INFTY
    global PrePath
    global Src,Dst
    global MinPath
    preValue = 0
    nowValue = 0
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
                    preValue = 0
                    nowValue = 0
                    if x == 0 and y == 0:
                        preValue = dijkstra(Src,Dst,z)
                        _Dst_ = Dst
                        MinPath = PrePath
                    else:
                        nowValue = dijkstra(Src,Dst,z)
                    if preValue > nowValue:
                        _Dst_ = Dst
                        preValue = nowValue
                        MinPath = PrePath
            if z == 0:
                print "时延最小路线:",
                printpath(_Dst_)
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
#    while root != MinPath[root]:
#        print "%s-->" %StationNameList[root],
#        root = MinPath[root]
#    if root == MinPath[root]:
#        print "%s" %StationNameList[root]
if __name__ == '__main__':
    Dijkstra()


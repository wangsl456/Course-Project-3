#-*-coding:utf-8-*-
from MetroStation import *
def FindStation(stationname,stationnamelist):
    return [a for a in range(len(stationnamelist)) if stationname.decode('utf-8') == stationnamelist[a]]
class Topo:
    def __init__(self):
        self.LinkList = []
        self.StationList = []
        self.TimeCost = {}
        old_line = 0
        for j in range(len(StationList)):
            tmpindexlist = []
            if StationList[j].Line == old_line:
                if j == 112:
                    tmpindex = 87
                    tmpLink = (j,tmpindex) if j < tmpindex else (tmpindex,j)
                    self.addLink(tmpLink,TimeCostDict[tmpLink])
                elif j == 269:
                    tmpindex = 264
                    tmpLink = (j,tmpindex) if j < tmpindex else (tmpindex,j)
                    self.addLink(tmpLink,TimeCostDict[tmpLink])
                elif j == 302:
                    tmpindex = 298
                    tmpLink = (j,tmpindex) if j < tmpindex else (tmpindex,j)
                    self.addLink(tmpLink,TimeCostDict[tmpLink])
                else:
                    tmpLink = (j-1,j)
                    self.addLink(tmpLink,TimeCostDict[tmpLink])
            elif StationList[j].Line != old_line:
                old_line = StationList[j].Line
            tmpindexlist = FindStation(StationList[j].StationName,StationNameList[:j])
            for k in range(len(tmpindexlist)):
                tmpLink = (j,tmpindexlist[k]) if j < tmpindexlist[k] else (tmpindexlist[k],j)
                self.addLink(tmpLink,TransferTime)
    def addLink(self,link,t):
        self.LinkList.append(link)
        self.TimeCost[link] = t
topo = Topo()
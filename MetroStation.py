#-*-coding:utf-8-*-
def FindStation(stationname,stationnamelist):
    return [a for a in range(len(stationnamelist)) if stationname.decode('utf-8') == stationnamelist[a]]
class Station:
    def __init__(self,stationname,line):
        self.StationName = stationname
        self.Line = line
    def SetDpid(self,dpid):
        self.Dpid = dpid
    def out(self):
        print '%s station is ' %self.StationName,
        print 'Line ',
        print self.Line,
        print
_StationName_ = []
_StationList_ = []
_StationList_.append("莘庄 外环路 莲花路 锦江乐园 上海南站 漕宝路 上海体育馆 徐家汇 衡山路 常熟路 陕西南路 黄陂南路 人民广场 新闸路 汉中路 上海火车站 中山北路 延长路 上海马戏城 汶水路 彭浦新村 共康路 通河新村 呼兰路 共富新村 宝安公路 友谊西路 富锦路")
_StationList_.append("浦东国际机场 海天三路 远东大道 凌空路 川沙 华夏东路 创新中路 唐镇 广兰路 金科路 张江高科 龙阳路 世纪公园 上海科技馆 世纪大道 东昌路 陆家嘴 南京东路 人民广场 南京西路 静安寺 江苏路 中山公园 娄山关路 威宁路 北新泾 淞虹路 虹桥2号航站楼 虹桥火车站 徐泾东")
_StationList_.append("上海南站 石龙路 龙漕路 漕溪路 宜山路 虹桥路 延安西路 中山公园 金沙江路 曹杨路 镇坪路 中潭路 上海火车站 宝山路 东宝兴路 虹口足球场 赤峰路 大柏树 江湾镇 殷高西路 长江南路 淞发路 张华浜 淞滨路 水产路 宝杨路 友谊路 铁力路 江杨北路")
_StationList_.append("宜山路 上海体育馆 上海体育场 东安路 大木桥路 鲁班路 西藏南路 南浦大桥 塘桥 蓝村路 浦电路 世纪大道 浦东大道 杨树浦路 大连路 临平路 海伦路 宝山路 上海火车站 中潭路 镇坪路 曹杨路 金沙江路 中山公园 延安西路 虹桥路")
_StationList_.append("莘庄 春申路 银都路 颛桥 北桥 剑川路 东川路 金平路 华宁路 文井路 闵行开发区")
_StationList_.append("港城路 外高桥保税区北 航津路 外高桥保税区南 洲海路 五洲大道 东靖路 巨峰路 五莲路 博兴路 金桥路 云山路 德平路 北洋泾路 民生路 源深体育中心 世纪大道 浦电路 蓝村路 上海儿童医学中心 临沂新村 高科西路 东明路 高青路 华夏西路 上南路 灵岩南路 东方体育中心")
_StationList_.append("花木路 龙阳路 芳华路 锦绣路 杨高南路 高科西路 云台路 耀华路 长清路 后滩 龙华中路 东安路 肇嘉浜路 常熟路 静安寺 昌平路 长寿路 镇坪路 岚皋路 新村路 大华三路 行知路 大场镇 场中路 上大路 南陈路 上海大学 祁华路 顾村公园 刘行 潘广路 罗南新村 美兰湖")
_StationList_.append("沈杜公路 联航路 江月路 浦江镇 芦恒路 凌兆新村 东方体育中心 杨思 成山路 耀华路 中华艺术宫 西藏南路 陆家浜路 老西门 大世界 人民广场 曲阜路 中兴路 西藏北路 虹口足球场 曲阳路 四平路 鞍山新村 江浦路 黄兴路 延吉中路 黄兴公园 翔殷路 嫩江路 市光路")
_StationList_.append("杨高中路 世纪大道 商城路 小南门 陆家浜路 马当路 打浦桥 嘉善路 肇嘉浜路 徐家汇 宜山路 桂林路 漕河泾开发区 合川路 星中路 七宝 中春路 九亭 泗泾 佘山 洞泾 松江大学城 松江新城 松江体育中心 醉白池 松江南站")
_StationList_.append("新江湾城 殷高东路 三门路 江湾体育场 五角场 国权路 同济大学 四平路 邮电新村 海伦路 四川北路 天潼路 南京东路 豫园 老西门 新天地 陕西南路 上海图书馆 交通大学 虹桥路 宋园路 伊犁路 水城路 龙溪路 上海动物园 虹桥1号航站楼 虹桥2号航站楼 虹桥火车站 龙柏新村 紫藤路 航中路")
_StationList_.append("康新公路 秀沿路 罗山路 御桥 浦三路 三林东 三林 东方体育中心 龙耀路 云锦路 龙华 上海游泳馆 徐家汇 交通大学 江苏路 隆德路 曹杨路 枫桥路 真如 上海西站 李子园 祁连山路 武威路 桃浦新村 南翔 马陆 嘉定新城 白银路 嘉定西 嘉定北 上海赛车场 昌吉东路 上海汽车城 安亭 兆丰路 光明路 花桥")
_StationList_.append("金海路 申江路 金京路 杨高北路 巨峰路 东陆路 复兴岛 爱国路 隆昌路 宁国路 江浦公园 大连路 提篮桥 国际客运中心 天潼路 曲阜路 汉中路 南京西路 陕西南路 嘉善路 大木桥路 龙华中路 龙华 龙漕路 漕宝路 桂林公园 虹漕路 虹梅路 东兰路 顾戴路 虹莘路 七莘路")
_StationList_.append("金运路 金沙江西路 丰庄 祁连山南路 真北路 大渡河路 金沙江路 隆德路 武宁路 长寿路 江宁路 汉中路 自然博物馆 南京西路 淮海中路 新天地 马当路 世博会博物馆 世博大道")
_StationList_.append("滴水湖 临港大道 书院 惠南东 惠南 野生动物园 新场 航头东 鹤沙航城 周浦东 罗山路 华夏中路 龙阳路")
TimeCost = []
SplitStr = ' '
TimeCost.append([120, 120, 180, 180, 180, 180, 120, 120, 120, 120, 120, 180, 120, 120, 180, 120, 180, 120, 120, 180, 180, 120, 120, 180, 180, 120, 120])
TimeCost.append([180, 420, 300, 180, 300, 180, 180, 300, 180, 120, 240, 60, 180, 180, 120, 120, 180, 180, 120, 120, 180, 180, 120, 180, 120, 180, 420, 120, 120])
TimeCost.append([120, 120, 120, 180, 120, 120, 120, 180, 120, 120, 180, 120, 240, 120, 120, 180, 120, 120, 180, 180, 180, 120, 120, 120, 180, 120, 180, 120])
TimeCost.append([120, 120, 120, 60, 120, 180, 120, 180, 120, 120, 120, 180, 120, 120, 120, 120, 180, 180, 180, 120, 180, 60, 180, 120, 120, 120])
TimeCost.append([180, 120, 180, 240, 180, 120, 120, 180, 120, 120])
TimeCost.append([180, 120, 180, 180, 120, 120, 180, 120, 120, 120, 180, 120, 180, 120, 120, 120, 180, 120, 180, 180, 120, 180, 120, 180, 120, 120, 120])
TimeCost.append([180, 120, 180, 120, 180, 120, 120, 120, 120, 180, 120, 120, 180, 120, 180, 120, 120, 180, 120, 120, 120, 120, 180, 120, 120, 180, 180, 180, 180, 120, 240, 120])
TimeCost.append([120, 120, 120, 240, 180, 180, 180, 120, 120, 120, 120, 180, 120, 120, 60, 180, 120, 120, 180, 120, 120, 120, 120, 120, 180, 120, 120, 120, 60])
TimeCost.append([180, 120, 240, 180, 120, 120, 120, 180, 120, 180, 240, 180, 180, 180, 180, 120, 240, 420, 240, 180, 300, 180, 180, 180, 240])
TimeCost.append([120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 180, 120, 120, 180, 120, 120, 120, 120, 120, 180, 120, 180, 180, 60, 240, 120, 120])
TimeCost.append([180, 180, 180, 300, 180, 120, 300, 180, 120, 120, 180, 180, 180, 180, 180, 120, 120, 120, 180, 120, 180, 120, 120, 240, 360, 180, 180, 240, 120, 240, 360, 180, 120, 120, 180, 120])
TimeCost.append([240, 120, 120, 180, 120, 180, 120, 120, 180, 120, 120, 120, 180, 180, 120, 180, 180, 120, 180, 120, 180, 180, 120, 180, 120, 120, 120, 180, 120, 180, 120])
TimeCost.append([180, 180, 120, 180, 180, 180, 180, 120, 120, 120, 180, 120, 120, 180, 180, 60, 180, 180])
TimeCost.append([180, 360, 660, 300, 480, 420, 360, 240, 360, 420, 240, 300])
StationList = []
StationListStr = []
StationNameList = []
for i in range(0,14):
    tmpList = _StationList_[i].split(SplitStr)
    tmpLen = len(tmpList)
    for j in range(0,tmpLen):
        if i != 13:
            StationList.append(Station(tmpList[j],i + 1))
        elif i == 13:
            StationList.append(Station(tmpList[j],16))
        StationNameList.append(tmpList[j].decode('utf-8'))
TimeCostDict = {}
_TimeCostDict_ = {}
TimeCostDictList = []
k = 0
old_line = -1
TransferTime = 0
for i in range(len(TimeCost)):
    for j in range(len(TimeCost[i])):
        TransferTime = TransferTime + TimeCost[i][j]
for i in range(len(_StationList_)):
    for j in range(len(_StationList_[i].split(SplitStr))):
        tmpindexlist = []
        if i == old_line:
            if (i == 3) and (j == (len(_StationList_[i].split(SplitStr)) - 1)):
                TimeCostDict[k,j+k] = TimeCost[i][j]
                TimeCostDict[j+k-1,j+k]=TimeCost[i][j-1]
                _TimeCostDict_[k,j+k] = TimeCost[i][j]
                _TimeCostDict_[j+k-1,j+k]=TimeCost[i][j-1]
            elif (i == 9) and (j == 28):
                TimeCostDict[k+23,j+k] = TimeCost[i][j-1]
                _TimeCostDict_[k+23,j+k] = TimeCost[i][j-1]
            elif (i == 10) and (j == 30):
                TimeCostDict[k+26,j+k] = TimeCost[i][j-1]
                _TimeCostDict_[k+26,j+k] = TimeCost[i][j-1]
            else:
                TimeCostDict[j+k-1,j+k]=TimeCost[i][j-1]
                _TimeCostDict_[j+k-1,j+k]=TimeCost[i][j-1]
        elif i != old_line:
            old_line = i
        tmpindexlist = FindStation(StationList[j+k].StationName,StationNameList[:j+k])
        for p in range(len(tmpindexlist)):
            tmpLink = (j+k,tmpindexlist[p]) if (j+k) < tmpindexlist[p] else (tmpindexlist[p],j+k)
            TimeCostDict[tmpLink] = 300
            _TimeCostDict_[tmpLink] = TransferTime
    k = k + len(_StationList_[i].split(SplitStr))
TimeCostDictList.append(TimeCostDict)
TimeCostDictList.append(_TimeCostDict_)
DpidList = []
passedStationNameList = []
print "请输入正确的站名，所有站点名称如下："
for i in range(len(StationList)):
    StationList[i].SetDpid(i)
    DpidList.append(i)
    if StationNameList[i] not in passedStationNameList:
        print StationNameList[i],
    passedStationNameList.append(StationNameList[i])
print
if __name__ == '__main__':
    for i in range(len(StationList)):
        print i
        StationList[i].out()

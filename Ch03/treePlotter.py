import matplotlib.pyplot as plt





# 定义文本框 和 肩头
# dict() 用于创建一个字典
decisionNode = dict(boxstyle = 'sawtooth', fc = '0.8')
leafNode = dict(boxstyle = 'round4', fc = '0.8')
arrowArgs = dict(arrowstyle = '<-')


'''
数据源
'''
def retrieveTree(i):
    listOfTrees = [
        {'no surfacing': 
            {0: 'no', 
             1: {'flippers': 
                {0: 'no', 
                 1: 'yes'}}}}, 
        {'no surfacing': 
            {0: 'no', 
             1: {'flippers': 
                {0: {'head':
                    {0: 'no',
                     1: 'yes'}},
                 1: 'yes'}}}}]
    
    return listOfTrees[i]



'''
叶节点的数目
'''
def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    
    return numLeafs



'''
数的层数
'''
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisPepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisPepth = 1
        if thisPepth > maxDepth:
            maxDepth = thisPepth
    
    return maxDepth



'''
画节点
'''
def plotNode(nodeText, centerPt, parentPt, nodeType):
    # https://blog.csdn.net/helunqu2017/article/details/78659490
    createPlot.ax1.annotate(
        nodeText,
        xy = parentPt,
        xycoords = 'axes fraction',
        xytext = centerPt,
        textcoords = 'axes fraction',
        va = 'center',
        ha = 'center',
        bbox = nodeType,
        arrowprops = arrowArgs )



'''
在父子节点间 填充文本信息
'''
def plotMinText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)



'''
绘制图像
'''
def plotTree(myTree, parentPt, nodeText):
    # 计算宽高
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)

    firstStr = myTree.keys()[0]
    tmpTotalW = (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW
    cntrPt = (plotTree.xOff + tmpTotalW, plotTree.yOff)
    # 标记子节点属性值
    plotMinText(cntrPt, parentPt, nodeText)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)

    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(
                secondDict[key], 
                (plotTree.xOff, plotTree.yOff),
                cntrPt,
                leafNode)
            plotMinText(
                (plotTree.xOff, plotTree.yOff),
                cntrPt, 
                str(key))

    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD
    



'''
画图像
'''
def createPlot(inTree):
    # https://blog.csdn.net/admin_maxin/article/details/80667671
    fig = plt.figure(num = 1, facecolor = 'white')
    fig.clf()
    # ax1 是 createPlot() 函数的属性;
    # ax1 是 Axes 的缩写，表示子图
    # subplot() 创建子图
    # https://blog.csdn.net/gatieme/article/details/61416645
    # xticks yticks 表示x，y轴取值，为空就是木有
    # axprops = dict(xticks = [], yticks = [])
    # createPlot.ax1 = plt.subplot(111, frameon = True, **axprops)
    createPlot.ax1 = plt.subplot(111, frameon = True)

    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = - 0.5 / plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    
    plt.show() 


inTree = retrieveTree(0)
createPlot(inTree)
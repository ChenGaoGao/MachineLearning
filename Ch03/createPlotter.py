import matplotlib.pyplot as plt



# 定义文本框 和 肩头
# dict() 用于创建一个字典
decisionNode = dict(boxstyle = 'sawtooth', fc = '0.8')
leafNode = dict(boxstyle = 'round4', fc = '0.8')
arrowArgs = dict(arrowstyle = '<-')

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

def createPlot():
    # https://blog.csdn.net/admin_maxin/article/details/80667671
    fig = plt.figure(num = 1, facecolor = 'white')
    fig.clf()
    # ax1 是 createPlot() 函数的属性;
    # ax1 是 Axes 的缩写，表示子图
    # subplot() 创建子图
    # https://blog.csdn.net/gatieme/article/details/61416645
    createPlot.ax1 = plt.subplot(111, frameon = True)
    plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show() 

createPlot()
import matplotlib.pyplot as plt



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



print getNumLeafs(retrieveTree(1))
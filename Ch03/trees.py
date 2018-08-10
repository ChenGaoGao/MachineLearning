# -*- coding: utf-8 -*-
from math import log


'''
源数据
'''
def createDataSet():
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'] ]
    labels = ['no surfacing', 'flippers']

    return dataSet, labels



'''
计算数据的信息熵
'''
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
            
    return shannonEnt
    


'''
按照给定特征 划分数据集
'''
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    
    return retDataSet


'''
选择最好的数据集划分方式
'''
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1

    # numFeatures 有多少个特征点
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        # uniqueVals 每个特征点 对应有多少个取值
        for value in uniqueVals:
            # 根据特征点 取值 划分数据集
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet) 

        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
            
    return bestFeature
    








dataSet, labels = createDataSet()
print dataSet

# print calcShannonEnt(dataSet)

# print splitDataSet(dataSet, 1, 1)
# print splitDataSet(dataSet, 1, 0)

print chooseBestFeatureToSplit(dataSet)
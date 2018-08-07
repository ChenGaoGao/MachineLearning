# -*- coding: utf-8 -*-
from math import log


'''
源数据
'''
def createDataSet():
    dataSet = [
        [1, 1, 'maybe'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'yes'] ]
    labels = ['no surfacing', 'flippers']

    return dataSet, labels



'''
计算数据的 最后一项分类(featVec[-1]) 的信息熵
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
    






dataSet, labels = createDataSet()

print calcShannonEnt(dataSet)
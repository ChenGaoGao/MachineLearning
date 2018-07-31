# -*- coding: utf-8 -*-
from numpy import *
import operator

def createDataSet():
	group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
	labels = ['A', 'A', 'B', 'B']

	return group, labels


def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	print('dataSet')
	print(dataSet)
	
	'''
	计算距离
	'''
	# tile(parameter1, parameter2)按照 参数2 的规则复制 参数1 
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	print('diffMat')
	print(diffMat)
	# **2表示平方
	sqDiffMat = diffMat **2
	print('sqDiffMat')
	print(sqDiffMat)
	# sum()普通求和  sum(axis=1)将一个矩阵的每一行向量相加
	sqDistances = sqDiffMat.sum(axis=1)
	print('sqDistances')
	print(sqDistances)
	distances = sqDistances **0.5
	print('distances')
	print(distances)

	'''
	对距离排序
	'''
	# 将distances中的元素从小到大排列，提取其对应的index(索引)
	sortedDistIndicies = distances.argsort()
	print('sortedDistIndicies')
	print(sortedDistIndicies)

	print('labels')
	print(labels)
	
	# 
	classCount = {}
	print('classCount')
	print(classCount)
	for i in range(k):
		print('iiiiiiiii', i)
		print('sortedDistIndicies i')
		print(sortedDistIndicies[i])
		voteIlabel = labels[sortedDistIndicies[i]]
		print('voteIlabel')
		print(voteIlabel)
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
		print('classCount[voteIlabel]')
		print(classCount)
	sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
	print('sortedClassCount')
	print(sortedClassCount)

	
	return sortedClassCount[0][0]

	
	




group, labels = createDataSet()

classify0([0, 0], group, labels, 3)

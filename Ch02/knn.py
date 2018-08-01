# -*- coding: utf-8 -*-
from numpy import *
import operator

import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
	group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
	labels = ['A', 'A', 'B', 'B']

	return group, labels


'''
k-近邻算法
inX		待测试
dataSet	源数据
labels	源数据对应的类型
k		取多少个特征点
'''
def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	
	'''
	计算距离
	'''
	# tile(parameter1, parameter2)按照 参数2 的规则复制 参数1 
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	# **2表示平方
	sqDiffMat = diffMat **2
	# sum()普通求和  sum(axis=1)将一个矩阵的每一行向量相加
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances **0.5

	'''
	对距离排序
	'''
	# 将distances中的元素从小到大排列，提取其对应的index(索引)
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

	sortedClassCount = sorted(classCount.iteritems(),
	 key=operator.itemgetter(1), reverse=True)

	return sortedClassCount[0][0]


'''
将文本记录 转换为 NumPy矩阵
'''
def file2matrix(filename):
	fr = open(filename)
	'''
	得到文件行数
	'''
	arrayOLines = fr.readlines()
	numberOfLines = len(arrayOLines)

	'''
	创建 NumPy 矩阵
	'''
	# zeros((a,b)) 创建二维数组
	returnMat = zeros((numberOfLines, 3))
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		# strip() 去除首尾空格
		line = line.strip()
		# split() 通过指定分隔符对字符串进行切片   \t 制表符
		listFromLine = line.split('\t')
		returnMat[index, :] = listFromLine[0 : 3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return returnMat, classLabelVector


'''
归一化特征值
'''
def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals

	# 3×3的单位矩阵e, e.shape为（3，3），表示3行3列,
	# 第一维的长度为3，第二维的长度也为3 
	# e.shape[1] 为第一维的长度，e.shape[0] 为第二维的长度。
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals, (m, 1))
	normDataSet = normDataSet / tile(ranges, (m, 1))

	return normDataSet, ranges, minVals


def datingClassTest():
	hoRaio = 0.10
	datingDataMat, datingLabels = file2matrix(
	'/Users/gao/Documents/MachineLearning/Ch02/datingTestSet2.txt')
	normMat, ranges, minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m*hoRaio)
	errorCount = 0.0

	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i, :],
		 normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
		print classifierResult, datingLabels[i]
		if classifierResult != datingLabels[i]:
			errorCount += 1
	print errorCount / float(numTestVecs)



'''
group, labels = createDataSet()

classify0([0, 0], group, labels, 3)
'''


'''
fig = plt.figure()
# add_subplot(349) 参数349的意思是：将画布分割成3行4列，
# 图像画在从左到右从上到下的第9块
ax = fig.add_subplot(121)
# scatter(x, y, s, c...) x、y 坐标; s 点的大小;  c 颜色;
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2],
 15.0*array(datingLabels), 15.0*array(datingLabels))

ax = fig.add_subplot(122)
ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1],
 15.0*array(datingLabels), 15.0*array(datingLabels))

plt.show()
'''

datingClassTest()
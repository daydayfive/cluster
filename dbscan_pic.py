# -*- coding: UTF-8 -*-

# @author Wujunjun
# @based dbscan algorithm
# @create time 2019.7.14
# @for test pictures
# 密度聚类可适用于形状不规则的

import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
import random

#获取黑点的坐标值
def get_point(area,x_add,y_add):

    x,y=area.shape
    black_point=[]
    for i in range(x):
        for j in range(y):
            if area[i][j]<128:
                black_point.append([i+x_add,j+y_add])
    return  black_point


def get_dis(point,point_around):
	dis_point=((point[0]-point_around[0])**2+(point[1]-point_around[1])**2)**0.5
	return dis_point


def get_Neps(Dataset,point,eps):
	N=0
	n_eps=[]
	for i in range(len(Dataset)):
	
		dis=get_dis(point,Dataset[i])
		if dis<=eps:
			N+=1
			n_eps.append(i)
	return N,n_eps
	


def dbscan(eps,MinPts,Dataset):
	core_project=[]
	for i in range(len(Dataset)):
		n,n_eps=get_Neps(Dataset,Dataset[i],eps)
		if n>=MinPts:
			core_project.append(i)
		
	
	k=0
	T=[i for i in range(len(Dataset))]
	
	cluster=[]
	while len(core_project)>0:
		Q = []
		T_old=T
	
		
		ob=random.choice(core_project)
	
		Q.append(ob)

		
		#core_project.remove(ob)
		T=list(set(T)-set(Q))
		while len(Q)>0:
			q=Q[0]
			Q.remove(q)
			
			n,n_eps=get_Neps(Dataset,Dataset[q],eps)
			if n>=MinPts:
				delta=list(set(n_eps).intersection(set(T)))
				Q=list(set(Q).union(set(delta)))
				T=list(set(T).difference(set(delta)))
		
		
				
		
		cluster.append(list(set(T_old).difference(set(T))))
		#print(len(cluster[k]))
		core_project=list(set(core_project).difference(set(cluster[k])))
		
		k+=1
	
	return cluster,k
				
		
		
	

	
	



if __name__=="__main__":
	pic=np.asarray(Image.open("test.jpg"))
	pic_part=pic[100:150,100:150]
	
	data_set=get_point(pic_part,100,100)
	print(len(data_set))
	eps=2
	MinPts=4
	cluster,k=dbscan(eps,MinPts,data_set)
	colors = ['#0000FF', '#FF0000', '#00FF00', '#666666', '#FFFF00']
	
	for i in range(k):
		color = colors[i % 5]
		print(len(cluster[i]))
		for j in cluster[i]:
			plt.scatter(data_set[j][0], data_set[j][1], c=color, alpha=0.5)
		
	plt.show()

	

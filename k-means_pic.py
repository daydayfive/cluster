# -*- coding: UTF-8 -*-

# @author Wujunjun
# @create time 2019.7.11
# @for test pictures



import numpy as np
from PIL import Image
from random import random,sample
import matplotlib.pyplot as plt


#获取黑点的坐标值
def get_point(area,x_add,y_add):

    x,y=area.shape
    black_point=[]
    for i in range(x):
        for j in range(y):
            if area[i][j]<128:
                black_point.append([i+x_add,j+y_add])
    return  black_point


#将list中的黑点坐标绘制出来
def draw_point(pic_black_point):
    for i in range(len(pic_black_point)):
        plt.scatter(pic_black_point[i][0],pic_black_point[i][1])
    plt.show()



def cal_dis(point,cores):
    dis=[]
    dist=0
    for i in range(len(cores)):
        dist=((point[0]-cores[i][0])**2+(point[1]-cores[i][1])**2)**0.5
        dis.append(dist)
    return  dis
def put_point_into_cluster(pic_black_point,cores,k):
    cl=[]
    for i in range(k):
        cl.append([])

    for i in pic_black_point:
        dis=cal_dis(i,cores)
        cl[dis.index(min(dis))].append(i)
    return cl



def cal_cores(cl):
    new_cores=[]

    for i in range(len(cl)):
        xs=0
        ys=0
        for j in range(len(cl[i])):
            xs+=cl[i][j][0]
            ys+=cl[i][j][1]
        x_new=xs/len(cl[i])
        y_new=ys/len(cl[i])
        x_new=round(x_new,2)
        y_new=round(y_new,2)
        new_cores.append([x_new,y_new])

    return new_cores




#对输入的坐标点进行k-means聚类
def k_means(pic_black_point,k):
    my_cores=sample(pic_black_point,k)
    print(my_cores)
    iter=0

    while True:
        iter+=1

        cl=put_point_into_cluster(pic_black_point,my_cores,k)


        news_cores=cal_cores(cl)


        if my_cores==news_cores:
            break
        else:
            my_cores=news_cores

        print("经历了%d次迭代，迭代后的质心如下：\n",iter)
        print(my_cores)

    colors = ['#0000FF', '#FF0000', '#00FF00', '#666666', '#FFFF00']
    for i in range(k):
        color = colors[i % 5]
        for j in cl[i]:
            plt.scatter(j[0],j[1], c=color, alpha=0.5)
        plt.scatter(my_cores[i][0],my_cores[i][1], marker='+', c='#000000', s=180)
    plt.show()




























if __name__=="__main__":
    pic = np.asarray(Image.open("test.jpg"))
    map=pic[100:150,100:150]
    x_add=100
    y_add=100
    rows,cols=map.shape

    pic_black_point=get_point(map,x_add,y_add)         #增加x_add，y_add变量是为了从局部地图得到的点的值是全局的

    draw_point(pic_black_point)

    k=int(input("请输入你需要分成的k簇：\n"))

    k_means(pic_black_point,k)















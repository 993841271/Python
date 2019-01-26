import matplotlib.pyplot as plt
from 随机漫步 import RandomWalk
"""rw=RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,c=rw.x_values,cmap=plt.cm.Blues,s=10)
plt.show()"""
#从左到右颜色渐变


rw=RandomWalk()
rw.fill_walk()
"""plt.figure(figsize=(10,6))"""
#用于修改图标尺寸
point_numbers=list(range(rw.num_points))
#从起点到终点颜色渐变

plt.scatter(rw.x_values,rw.y_values,
            c=point_numbers,cmap=plt.cm.Reds,s=15)
            
"""plt.plot(rw.x_values,rw.y_values,linewidth=1)"""
#用于模拟线条随机
"""plt.scatter(0,0,c='green',s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='green',s=100)"""
#设置起点终点突出显示
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
#用于隐藏坐标轴
plt.show()
import matplotlib.pyplot as plt

x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values, y_values, c=x_values,cmap=plt.cm.Reds, edgecolor='none',
            s=10)
#plt.scatter(x_values,y_values,c='red',edgecolor='none',s=10)
#横坐标，纵坐标，c=颜色，cmap=plt.cm.Reds(颜色的映射)，edgecolor=线的颜色,s=线条大小
#可在matplotlib.org里面查看更多的颜色映射
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major',labelsize=14)
plt.axis([0,1100,0,1100000])
plt.show()
#plt.savefig('abc.png',bbox_inches='tight')
#上面注释用于直接保存图片，第二个实参指定将图表中多余的空白区域裁剪掉
import matplotlib.pyplot as plt

input_values=[1,2,3,4,5,6,7,8,9]
squares=[1,4,9,16,25,36,49,64,81]

plt.plot(input_values,squares,linewidth=5)
#横坐标，纵坐标，线的宽度
plt.title("Square Numbers",fontsize=24)
#标题
plt.xlabel("Value",fontsize=14)
#横坐标名称
plt.ylabel("Square of Value",fontsize=14)
#纵坐标名称
plt.tick_params(axis='both',labelsize=14)
#刻度的样式
plt.show()

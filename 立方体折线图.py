import matplotlib.pyplot as plt

x=list(range(1,1000))
y=[a**3 for a in x]
plt.scatter(x,y,c=x,cmap=plt.cm.Reds,s=10)
plt.title('立方体',fontsize=14)
plt.xlabel('x',fontsize=14)
plt.ylabel('y',fontsize=14)
plt.show()
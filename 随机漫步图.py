import matplotlib.pyplot as plt
from 随机漫步 import RandomWalk
rw=RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,c=rw.x_values,cmap=plt.cm.Blues,s=10)
plt.show()


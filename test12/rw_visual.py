import matplotlib.pyplot as plt

from random_walk import RandomWalk

#创建一个RandomWalk实例
rw = RandomWalk();
rw.fill_walk();
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=10);
plt.show();
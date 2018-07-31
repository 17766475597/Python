import matplotlib.pyplot as plt

x_values = list(range(1,1001));
y_values = [x**2 for x in x_values];

plt.scatter(x_values, y_values, s=1, c='red',edgecolors='none');

plt.axis([0, 1100,0 ,1100000]);

plt.show();

plt.savefig('square_plot.png',bbox_inches='tight')      #保存图像 第二个参数为是否裁剪空白
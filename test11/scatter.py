import matplotlib.pyplot as plt

input_value = [1,2,3,4,5];
square = [1,4,9,16,25];
#绘制散点图
plt.scatter(input_value,square,linewidth=3);

plt.title("Square Numbers", fontsize=24);
plt.xlabel("Value", fontsize=14);
plt.ylabel("Square of Value", fontsize=14);

plt.tick_params(axis='both', labelsize=12)

plt.show()
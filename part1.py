#字符串

car = ['Honda','Toyota','Benz','BMW'];   #列表方括号
car.insert(1,'Hyundai');      #插入元素
print(car);

car.append("append");         #追加元素
print(car);

del car[0];       #删除元素
print(car);

pop_ele = car.pop();     #弹出最后一个元素
print(car);
print(pop_ele);

pop_eler = car.pop(0);      #弹出任意位置元素（下标从0开始）
print(car);
print(pop_eler);

car.remove('Benz');       #根据值删除元素
print(car);

a = len(car);              #列表长度
print(a);

car.sort(reverse=True);        #反向排序
print(car);


#for循环

for car_ele in car:          #遍历car列表
    print(car_ele);

for value in range(1,5):      #打印1-5
    print(value);

for value in range(0,len(car)):
    print(car[value]);

digits = [1,2,3,4,5,6,7,8,9,0];

print("min = "+ str(min(digits)));
print("min = "+ str(max(digits)));
print("min = "+ str(sum(digits)));

print(digits[1:4]);          #index from 1 to 4
print(digits[:4]);           #index from start to 4
print(digits[4:]);           #index from 3 to end
print(digits[-3:]);          #Last 3
print(digits[:])             #ALL

digits_1 = digits[:];        #copy digits to digits_1xd
print(digits_1[:]);
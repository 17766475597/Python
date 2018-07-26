# 字典

alien_0 = {'color':'green' , 'points':5};
print(alien_0['color']);

# 创建一个空字典 并加入键值对
alien_0 = {};
alien_0['color'] = 'red';
alien_0['points'] = 7;
print(alien_0);

# 修改字典的值
if alien_0['color'] == 'red':
    alien_0['color'] = 'blue';
print(alien_0);

#删除键值对
del alien_0['points'];
print(alien_0);

#由类似对象组成的字典
basic_imfomation = {
    'name' : 'Jack',
    'age' : 18,
    'city' : 'Singapore',
}
print("My name is " + basic_imfomation['name']);

#遍历字典
for key,value in basic_imfomation.items():
    print('Key: ' + key)
    print('Value: ' + str(value));

#遍历字典所有键
num_of_keys = 0;
for key in basic_imfomation.keys():
    num_of_keys = num_of_keys + 1;
print(num_of_keys);

#遍历字典所有值
for value in basic_imfomation.values():
    print(value);
#上述做法可能存在重复值 用Set可有效避免
for value in set(basic_imfomation.values()):
    print(value);

#列表存储在字典中
fav_language = {
    'Jack' : ['Java','C++'],
    'Carol' : ['Python','C#'],
}
print(fav_language['Jack']);

#字典中储存字典
cities = {
    'Shanghai':{
        'country':'China',
        'Population':'2400',
    },

    'Guangzhou':{
        'country':'China',
        'Population':'2100',
    }
}

for city,cityattr in cities.items():
    print(city + " " + cityattr['country'] + " " + cityattr['Population'])
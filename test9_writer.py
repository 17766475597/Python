#向存储数据的json文件中写入数据
import json

numbers = [2, 4, 6, 8, 9];

filename = 'numbers.json';
with open(filename,'w') as f_obj:
    json.dump(numbers, f_obj);
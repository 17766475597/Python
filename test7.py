#文件

with open('pi_digits') as file_object:       #相对路径
    contents = file_object.read()
    print(contents);
    print(contents.rstrip());      #删除空行

with open("C:\\Users\HP\\Desktop\\task1.txt") as file_object:      #绝对路径
    contents = file_object.read();
    print(contents);

#逐行读取
file_name = 'pi_digits'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip());

#创建一个包含文件各行内容的列表
with open(file_name) as file_object:
    lines = file_object.readlines();

for line in lines:
    print(line.rstrip());

#使用文件的内容
pi_string = '';
for line in lines:
    pi_string += line.rstrip();

print(pi_string);
print(len(pi_string));


#写入空文件
filename = 'write_message';

with open(filename,'w') as file_object:           #默认只读方式打开
    file_object.write("I love Python!\n");        #不换行会自动挤在一起
    file_object.write("Python also loves me!\n");

#附加到文件
with open(filename,'a') as file_object:           #默认只读方式打开
    file_object.write("I love fish!\n");        #不换行会自动挤在一起
    file_object.write("Fish also loves me!\n");

#Ex 10-3
name = input('input your name?');
with open(filename,'a') as file_object:
    file_object.write(name + "\n");
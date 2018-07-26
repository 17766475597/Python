#输入
name = input("What's your name? ");
print("Hello , " + name);

age = input("age:");
age = int(age);
if age<18:
    print("too young too simple");
elif age>60:
    print("sophisticated");
else:
    print("adult");

#while循环
current_num = 0;
while current_num<5:
    print(current_num);
    current_num = current_num+1;

#标志变量
active = True;
while active:
    message = input("...");
    if message == 'quit':
        active = False;
    else:
        print(message);

#打印10以内的奇数 continue
num = 1;
while num<10:
    if(num % 2==0):
        num = num + 1;
        continue;
    else:
        print(num);
        num = num+ + 1;

#while处理列表
list_area = ['Canada' , 'America' , 'Japan'];
while 'Japan' in list_area:
    list_area.remove('Japan');
print(list_area);

#使用用户输入填充字典
responses = {};
this_active = True;
while this_active:
    name = input('name? ');
    language = input('language? ');
    responses[name] = language;
    this_active = input("continue? ");
    if this_active == 'No':
        this_active = False;
for name,language in responses.items():
    print(name + " " + language);

#Exercise 登记游客与目的地
dic = {};
this_active1 = True;
while this_active1:
    visitor = input("Visitor's name : ");
    destination = input("Visitor's destination : ");
    dic[visitor] = destination;
    flag = input("Continue to register?");
    if flag == "No":
        this_active1 = False;
for visitor,destination in dic.items():
    print("visitor:" + visitor + "   " + "destination:" + destination);

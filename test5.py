#函数
def greet_user(username):
    print("Hello " + username);

greet_user("Jack");


#关键字实参
def info(name , age):
    print("age:" + age);
    print("name:" + name);

info(name = "Jack",age = "18");    #避免参数顺序输入错误


#返回值
def get_fommatted_name(first_name,last_name):
    full_name = last_name + " " + first_name;
    return full_name;

name = get_fommatted_name("Yuxuan","Zhang");
print(name);


#返回字典
def build_person(name,age):
    person = {'name':name,'age':age};
    return person;

writter = build_person('Jack','20');
print(writter);

#Ex1 city_name
def city_name(city,country):
    full_info = city + "," + country;
    return full_info;

city1 = city_name("Beijing","China");
print(city1);

#Ex2 make_album
def make_album(album_name,singer):
    album = {"name":album_name,"singer":singer};
    return album;

#name = input("Album name? ");
#singer = input("Singer name? ");
#album_info = make_album(name,singer);
#print(album_info);


#传递列表
def greetusers(names):
    for name in names:
        print("Hello " + name);

names = ('Jack','Carol','Maria');
greetusers(names);


#eg. 函数中pop掉unprinted_designs以及append空列表completed_models
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop();
        print("Printing model: " + current_design);
        completed_models.append(current_design);

def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model);

unprinted_designs = ['iphone','Huawei','Samsung'];
completed_models = [];
print_models(unprinted_designs,completed_models);
show_completed_models(completed_models);


#传递任意数量的实参
def make_pizza(*toppings):
    print(toppings);

make_pizza("pepperoni");
make_pizza("pepperoni","green pepper","extra cheese");


#使用任意数量的关键字实参
def build_profile(first,last,**user_info):
    profile = {};
    profile['first_name'] = first;
    profile['last_name'] = last;
    for key,value in user_info.items():
        profile[key] = value;
    return profile;

user_profile = build_profile('albert','einstein',location='princeton',field='physics');
print(user_profile);

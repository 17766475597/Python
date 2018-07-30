#异常处理

try:
    print(5/0);
except ZeroDivisionError:
    print("You can't divide by zero!");


print("Two number divide");
print("Enter 'q' to quit");
while True:
    first_number = input('a=?');
    if(first_number == 'q' ):
        break;
    second_number = input('b=?');
    try:
        answer = int(first_number)/int(second_number);
    except ZeroDivisionError:
        print("You can't divide by zero!");
    else:
        print(answer);


#处理FileNotFoundError异常
filename = 'alice.txt';

try:
    with open(filename) as file_obj:
        contents = file_obj.read();
except FileNotFoundError:
    print("File is not found!");


#分析文本有多少单词
def count_words(filename):
    try:
        with open(filename) as file_obj:
            contents = file_obj.read();
    except FileNotFoundError:
        msg = "Sorry,the file " + filename + "is not found!";
    else:
        words = contents.split();
        num = len(words);
        print("the file " + filename +" has " + str(num) + " words.");


filenames = ["write_message", "write_message1"];
for filename in filenames:
    count_words(filename);


#失败时一声不吭
filename = 'alice.txt';

try:
    with open(filename) as file_obj:
        contents = file_obj.read();
except FileNotFoundError:
    pass;      #什么都不做
#导入整个模块
import test5;
writter = test5.build_person('Jack','18');
print(writter);

#导入特定函数
from test5 import build_person
writter = build_person('Carol','17');
print(writter);

#导入特定模块给函数起别名
from test5 import build_person as bp
writter = bp('Cathy','16');
print(writter);

#使用as给模块起别名
import test5 as t
writter = t.build_person('Lisa','15');
print(writter);

#导入模块中所有函数
from test5 import *
writter = t.build_person('Ann','14');
print(writter);
###时间戳
import time
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

###configparser模块简介
#“该模块适用于配置文件的格式与windows ini文件类似，可以包含一个或多个节（section），每个节可以有多个参数（键=值）。节与java原先的配置文件相同的格式”
import configparser #引入模块
config = configparser.ConfigParser()  #类中一个方法 #实例化一个对象
#写入配置
config["information"] = {'name': 'via',
                      'age': '24',
                     'job': '9'
                     }	#类似于操作字典的形式
with open('example.ini', 'w') as configfile:
   config.write(configfile)	#将对象写入文件

config.read('example.ini')
print('information' in config) # True
print(config.sections())  #列出所有section
for key in config['information']: #循环读取section中的值
    print("%s:%s" % (key,config['information'][key],))
print(config.options('information'))  #通for取information下所有键
print(config.items('information'))  #取information下键值对
print(config.get('information','name')) #准确取section出键对应的值
#修改配置
config.add_section('service') #添加section
config.remove_option('information',"age") #删除一个配置项
config.remove_section('say something')  #删除section
config.set('information','name','cjk')  #修改配置项值
with open('example.ini','w') as f:
    config.write(f) #保存

###json文件处理
# json.dumps()和json.loads()是json格式处理函数（可以这么理解，json是字符串）
# json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
# json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）
# json.dump()和json.load()主要用来读写json文件函数
import json
dict = {'name': 'lk','age': 23}
json_infor = json.dumps(dict) #字典转字符串
aa = '{"name": "lk","age": 123}'  
bb = json.loads(aa) #字符串转字典
with open('example.json','w',encoding='utf-8') as f:
    json.dump(bb,f) #写入json文件
f = open('example.json','r',encoding='utf-8')
info = json.load(f) #读取json文件

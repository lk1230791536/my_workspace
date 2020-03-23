#时间戳
import time
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

#configparser模块简介
“该模块适用于配置文件的格式与windows ini文件类似，可以包含一个或多个节（section），每个节可以有多个参数（键=值）。节与java原先的配置文件相同的格式”
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

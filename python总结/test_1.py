#!/usr/bin/python
import logger
import json
import time
import commands
import requests
import kmc.kmc as k
from sys import argv
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import getpass
import re
import os
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

log_path = "/root/test"
host = 'https://127.0.0.1:19091'
url_sub = '/test_project/v1/validatetest_projectInfo'
class test_projectUser:
    def __init__(self):
        self.user = None
        self.authpass = None
        self.HeadersToken = None
        self.logger = logger.init(log_path)
        self.file_path = "/root/via.yml"
        self.pass_path = "/root/login.yml"

    def post(self,url,headers=None):
        try:
            response = requests.post(url, headers=headers, verify=False)
        except:
            return None
        if response.status_code != 200:
            return None
        resp = json.loads(response.content)
        if resp['data']:
            return resp['data']
        return None

    def run_cmd(self, cmd):
        try:
            (status, output) = commands.getstatusoutput(cmd)
            if status == 0:
                return output
            else:
                self.logger.info(output)
                return False
        except Exception as e:
            self.logger.error(e.message)
            return False

    def checkpass_repeat(self, pwd1, pwd2):
        if pwd1 == pwd2:
            return True
        else:
            return False

    def write_conf(self,content):
        with open(self.file_path, "a") as fp:
            fp.write(content)

    def test_project_count(self,name):
        with open(self.file_path, "r") as fp:
            content = fp.read()
            count = content.count(name)
            return count

    def checkip(self,hostip):
        pat = re.compile(r'([0-9]{1,3})\.')
        r = re.findall(pat, hostip + ".")
        if len(r) == 4 and len([x for x in r if int(x) >= 0 and int(x) <= 255]) == 4:
            return True
        else:
            return False

    def confire(self):
        confire = raw_input("Please enter [y/n] to confirm: ")
        if confire == 'n':
            exit(0)
        elif confire == 'y':
            return True
        else:
            print("Input error")
            return False

    def user_identity(self):
        uri = host + '/test_project/login'
        self.user = raw_input("Please enter user name(default admin): ")
        if len(self.user) == 0:
            self.user = 'admin'
        while True:
            self.authpass = getpass.getpass("Please enter user password: ")
            if len(self.authpass) == 0:
                print 'Password is empty, please re-input.'
                continue
            break
        headers = {'username': self.user, 'password': self.authpass}
        token = self.post(uri, headers)
        if not token:
            print 'User or Password incorrect , get token failed.'
            return False
        else:
            if token:
                self.HeadersToken = {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'X-Auth-Token': token
                }
                return True
            print "connect to server error."
            self.logger.info("login failed, error:%s" % token)
            return False

    def test_project_get_ip(self,action='update'):
        count_ip = 0
        if action == 'update':
            while count_ip < 4:
                test_project_ip = raw_input("Please enter the old test_project_user IP: ")
                if not self.checkip(test_project_ip) :
                    print("IP format error!")
                    count_ip = count_ip + 1
                    continue
                elif self.test_project_count(test_project_ip) == 0 :
                    print("The test_project_user IP not exists!")
                    count_ip = count_ip + 1
                    continue
                else:
                    return test_project_ip
                break
            print("Input test_project_user ID fail!!")
        elif action == 'add':
            while count_ip < 4:
                test_project_ip = raw_input("Please enter the test_project_user IP: ")
                if not self.checkip(test_project_ip):
                    print('IP format error!')
                    count_ip = count_ip + 1
                    continue
                elif self.test_project_count(test_project_ip) > 0:
                    print("The test_project_user IP already exists!")
                    count_ip = count_ip + 1
                    continue
                else:
                    return test_project_ip
                break
            print("Input test_project_user ID fail!!")

    def test_project_get_delete_ip(self):
        count_ip = 0
        while count_ip < 4:
            test_project_ip = raw_input("Please enter the test_project_user IP: ")
            if not self.checkip(test_project_ip) :
                print("IP format error!")
                count_ip = count_ip + 1
                continue
            elif self.test_project_count(test_project_ip) == 0 :
                print("The test_project_user IP not exists!")
                count_ip = count_ip + 1
                continue
            else:
                return test_project_ip
            break
        print("Input test_project_user ID fail!!")

    def test_project_get_username(self):
        count_user = 0
        while count_user < 4 :
            test_project_user = raw_input("Please enter the test_project_user user name: ")
            if not test_project_user:
                print("The input is null,please enter again!")
                count_user = count_user + 1
                continue
            else:
                return test_project_user
            break
        print("Input test_project_user USER fail!!")

    def test_project_get_pass(self):
        count_pass = 0
        while count_pass < 4 :
            test_project_password = getpass.getpass("Please enter the test_project_user password: ")
            test_project_password2 = getpass.getpass("Please enter the test_project_user password again: ")
            if not self.checkpass_repeat(test_project_password, test_project_password2) :
                print 'The password you entered is different, please re-enter !'
                continue
            return test_project_password2
            break

    def test_project_add_infor(self):
        infor = {}
        infor['ip'] = self.test_project_get_ip("add")
        infor['username'] = self.test_project_get_username()
        password = self.test_project_get_pass()
        infor['password'] = k.API().encrypt(0, password)
        url = host + url_sub
        body = {
            "ip": infor['ip'],
            "username": infor['username'],
            "password": password,
        }
        try:
            response = requests.post(url, json=body, headers=self.HeadersToken, verify=False, timeout=10)
            get_data = json.loads(response.content).get("data")
            if get_data.get("validationResult"):
                infor['test_projectId'] = get_data.get("test_projectId")
            else:
                self.logger.info(json.loads(response.content).get("msg"))
                return False
        except Exception as e:
            self.logger.error(e.message)
            print('Add test_project user fail!')
            return False
        return infor

    def test_project_update_infor(self):
        infor = {}
        infor['old_ip'] = self.test_project_get_ip("update")
        infor['ip'] = self.test_project_get_ip("add")
        infor['username'] = self.test_project_get_username()
        password = self.test_project_get_pass()
        infor['password'] = k.API().encrypt(0, password)
        url = host + url_sub
        body = {
            "ip": infor['ip'],
            "username": infor['username'],
            "password": password,
        }
        try:
            response = requests.post(url, json=body, headers=self.HeadersToken, verify=False, timeout=10)
            get_data = json.loads(response.content).get("data")
            if not get_data.get("validationResult"):
                self.logger.info(json.loads(response.content).get("msg"))
                return False
        except Exception as e:
            self.logger.error(e.message)
            return False

        script1 = 'sed -n "/%s/,/test_projectId/=" %s |tail -n1' % (infor['old_ip'], self.file_path)
        id_num = self.run_cmd(script1)
        script2 = "awk 'NR==%s {print}' %s | awk '{print $2}'" % (id_num, self.file_path)
        infor['test_projectId'] = self.run_cmd(script2)
        return infor

    def test_project_delete_infor(self, delte_ip):
        script1 = 'sed -n "/%s/,/test_projectId/=" %s |tail -n1' % (delte_ip, self.file_path)
        num = int(self.run_cmd(script1)) - 4
        script2 = 'sed -i "%s,%sd" %s' % (str(num), self.run_cmd(script1), self.file_path)
        result = os.system(script2)
        if result == 0:
            return True
        else:
            return False

    def add_test_project_info(self):
        if not self.user_identity():
            exit(1)
        self.logger.info('Add wmware user begin.')
        while True:
            notice = raw_input("Enter n to exit / enter to continue: ")
            if not notice:
                pass
            elif notice == 'n':
                exit(0)
            else:
                print("Input error")
                exit(1)
            contents = self.test_project_add_infor()
            if not contents:
                print('Add test_project user fail!')
                continue
            num = self.test_project_count('test_project') + 1
            title = "test_project%s:" % num + '\n'
            self.write_conf(title)
            for key, value in contents.items():
                content = "  " + key + ':' + " " + value + '\n'
                self.write_conf(content)
            print('Add %s success.' % contents['ip'])
            self.logger.info('Add %s success.' % contents['ip'])
            continue

    def delete_test_project_info(self):
        while True:
            notice = raw_input("Enter n to exit / enter to continue: ")
            if not notice:
                pass
            elif notice == 'n':
                exit(0)
            else:
                print("Input error")
                exit(1)
            delte_ip = self.test_project_get_delete_ip()
            confirm_notice = raw_input("Please enter [y/n] to confirm: ")
            if confirm_notice == 'n':
                exit(0)
            elif confirm_notice == 'y':
                pass
            else:
                print("Input error")
                exit(1)
            if self.test_project_delete_infor(delte_ip):
                print(' Delete %s success.' % delte_ip)
                self.logger.info('Delete %s success.' % delte_ip)
            else:
                print(' Delete %s fail.' % delte_ip)
                self.logger.error('Delete %s fail.' % delte_ip)

            continue

    def update_test_project_info(self):
        if not self.user_identity():
            exit(1)
        self.logger.info('Update wmware user begin.')
        while True:
            notice = raw_input("Enter n to exit / enter to continue: ")
            if not notice:
                pass
            elif notice == 'n':
                exit(0)
            else:
                print("Input error")
                exit(1)
            contents = self.test_project_update_infor()
            if not contents:
                print('Update test_project user fail!')
                continue
            self.test_project_delete_infor(contents['old_ip'])
            num = self.test_project_count('test_project') + 1
            title = "test_project%s:" % num + '\n'
            self.write_conf(title)
            for key, value in contents.items():
                if key == 'old_ip':
                    continue
                content = "  " + key + ':' + " " + value + '\n'
                self.write_conf(content)
            print('Update %s success.' % contents['ip'])
            self.logger.info('Update %s success.' % contents['ip'])
            continue

    def show_test_project_info(self):
        script = 'grep -v password %s | grep -v test_projectId' % self.file_path
        result = self.run_cmd(script)
        if not result:
            print("No test_project users.")
            exit(0)
        print(result)

    def usage(self):
        print '''usage: python test_project_tool.py {add|delete|update|display}  '''

if __name__ == '__main__':
    manager = test_projectUser()
    if len(argv) !=2:
        manager.usage()
        exit(1)
    try:
        if argv[1] == "add":
            manager.add_test_project_info()
        elif argv[1] == "delete":
            manager.delete_test_project_info()
        elif argv[1] == "update":
            manager.update_test_project_info()
        elif argv[1] == "display":
            manager.show_test_project_info()
        else:
            manager.usage()
    except KeyboardInterrupt:
        print '\nTerminated.'
        exit(1)
    exit(0)

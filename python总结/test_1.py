def information():
    infor = {}
    notice = input("input n to exit / enter to continue: ")
    if not notice :
        ip = input('please input IP: ')
        user = input('please input USER: ')
        password = input('please input PASS: ')
        infor['ip'] = ip
        infor['user'] = user
        infor['password'] = password
        return infor
    elif notice == 'n' :
        exit()
    else:
        print("input error")
        exit()

def write_file():
    file = './cjk.yml'
    for count in range(2):

        aa = information()
        for key, value in aa.items():
            with open(file,'a') as fp:
                fp.write(key + ':  ' + value + '\n')

write_file()




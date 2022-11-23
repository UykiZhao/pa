import base64

import requests
from selenium import webdriver


#      登录后台
def login(account, pwd, code):
    login_url = 'http://jwgl.thxy.cn/login!doLogin.action'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52",
        'cookie': 'JSESSIONID=0BF243207DAAF6FD546D468E1FE872BB; browserID=2999282456'
    }
    data = {
        "account": account,
        "pwd": pwd,
        "verifycode": code
    }
    response = requests.post(login_url, data=data, headers=headers)
    content = response.text
    with open('教务系统.html', 'w', encoding='utf-8') as fp:
        fp.write(content)


#     用户填写账号密码
def usermessage():
    account = int(input('请输入你的学号：'))
    pwd = input('请输入你的密码：')

    return account, pwd


# 验证码照片获取
def page_code():
    url = 'http://jwgl.thxy.cn/yzm'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52",
        'cookie': 'JSESSIONID=0BF243207DAAF6FD546D468E1FE872BB; browserID=2999282456'
    }
    # 转换时间戳
    import time
    t = int(time.time())
    time = int(round(t * 1000))
    data = {
        'd': time
    }
    request = requests.get(url, params=data, headers=headers)
    content = request.content
    with open('验证码.jpg', 'wb') as fp:
        fp.write(content)


# 超级鹰打码平台
def chaojiying():
    # !/usr/bin/env python
    # coding:utf-8
    from hashlib import md5

    class Chaojiying_Client(object):

        def __init__(self, username, password, soft_id):
            self.username = username
            password = password.encode('utf8')
            self.password = md5(password).hexdigest()
            self.soft_id = soft_id
            self.base_params = {
                'user': self.username,
                'pass2': self.password,
                'softid': self.soft_id,
            }
            self.headers = {
                'Connection': 'Keep-Alive',
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
            }

        def PostPic(self, im, codetype):
            """
            im: 图片字节
            codetype: 题目类型 参考 http://www.chaojiying.com/price.html
            """
            params = {
                'codetype': codetype,
            }
            params.update(self.base_params)
            files = {'userfile': ('ccc.jpg', im)}
            r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                              headers=self.headers)
            return r.json()

        def PostPic_base64(self, base64_str, codetype):
            """
            im: 图片字节
            codetype: 题目类型 参考 http://www.chaojiying.com/price.html
            """
            params = {
                'codetype': codetype,
                'file_base64': base64_str
            }
            params.update(self.base_params)
            r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, headers=self.headers)
            return r.json()

        def ReportError(self, im_id):
            """
            im_id:报错题目的图片ID
            """
            params = {
                'id': im_id,
            }
            params.update(self.base_params)
            r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
            return r.json()

    if __name__ == '__main__':
        chaojiying = Chaojiying_Client('uyki123', 'uyki123', '941904')  # 用户中心>>软件ID 生成一个替换 96001
        im = open('验证码.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        code = chaojiying.PostPic(im, 1902).get('pic_str')  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
        print(code)
        return code
        # print chaojiying.PostPic(base64_str, 1902)  #此处为传入 base64代码


if __name__ == '__main__':
    # account, pwd = usermessage()
    # page_code()
    # code = chaojiying()
    # login(account, pwd, code)
    pwd = bytes('zyq030909')
    base64_pwd = str(base64.b64encode(pwd),'utf-8')
    print(base64_pwd)

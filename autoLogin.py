import requests
import socket, re
import time
import ipRequest
from config import *


class login:
    def __init__(self, ip, url):
        self.ip = ip
        self.url = url

    def response(self):
        responses = requests.get(url=self.url, verify=False, timeout=3)
        return responses

    def run(self):
        return self.response()


def get_host_ip():
    try:
        s: socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('223.5.5.5', 80))
        ip = ipRequest.ipRequest()

    except Exception as e:
        print(f"获取ip失败{e}")
    finally:
        s.close()
    return ip


def autoLogin():
    ip = get_host_ip()
    if ip:
        print(f"当前ip为：{ip}\n")
    else:
        print(f"获取ip失败！脚本将无法生效")
        print(f"5秒后程序自动退出")
        time.sleep(5)
        return
    url = f"http://172.21.255.105:801/eportal/?c=Portal&a=login&callback=dr1004&login_method=1&user_account={user_account}%40{operator}&user_password={user_password}&wlan_user_ip={ip}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.3&v=4374"
    a = login(ip, url=url)
    while True:
        try:
            print("正在检测网络状态...")
            if requests.get("https://www.baidu.com", timeout=3).status_code == 200:
                print("当前在线")
        except Exception:
            print("当前网络不通畅\n正在尝试自动登录...")
            try:
                response = a.run()
                result = re.findall(r'"result":"(.*?)"', response.text)
                print(response.text)
                if result[0] == '1':
                    print("登录成功!")
                    print("是否进行网络监测？是请输入y，否则输入其它按键")
                    key = input()
                    if key == 'y':
                        print("OK!现在你可以把程序切换到后台，程序实时监测校园网登录情况")
                        continue
                    else:
                        print("程序即将在5秒后退出")
                        time.sleep(5)
                        return
                else:
                    print(f'登录失败，返回代码{result[0]}!')
            except:
                print("出现了某种错误!")
        finally:
            # 每15秒检查一次
            time.sleep(15)

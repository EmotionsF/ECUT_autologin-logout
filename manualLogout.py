import requests
import socket, re
import time
import ipRequest
from config import *

class logout:
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

def manualLogout():
    ip = get_host_ip()
    if not ip:
        print("无法获取IP地址，退出程序")
        time.sleep(5)
        return
    print(f"当前ip为：{ip}\n")
    urll = f'http://172.21.255.105:801/eportal/?c=Portal&a=unbind_mac&callback=dr1004&user_account={user_account}%40{operator}&wlan_user_mac=000000000000&wlan_user_ip={ip}&jsVersion=3.3.3&v=4374'
    b = logout(ip, url=urll)
    time.sleep(3)
    response = b.run()
    if response is None:
        print("请求失败，退出程序")
        time.sleep(5)
        return

    result = re.findall(r'"result":"(.*?)"', response.text)
    if result:
        if result[0] == '1':
            print("登出成功!")
        else:
            print(f'登出失败，返回代码{result[0]}!')
    else:
        print("未找到返回结果，退出程序")
    
    print("5秒之后程序关闭")
    time.sleep(5)



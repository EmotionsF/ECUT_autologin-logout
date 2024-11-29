import requests
import re

def ipRequest():
    # 设置目标 URL
    url = "http://172.21.255.105" 

    # 发送 GET 请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 获取文本内容
        text = response.text

        # 使用正则表达式提取 wlan_user_ip
        match = re.search(r'v46ip\s*=\s*["\']([^"\']+)["\']', text)
        match2 = re.search(r'v4ip\s*=\s*["\']([^"\']+)["\']', text)

        if match:
            wlan_user_ip = match.group(1)  # 提取到的 IP 地址
            print(f"wlan_user_ip: {wlan_user_ip}")
            return wlan_user_ip
        elif match2:
            wlan_user_ip = match2.group(1)  # 提取到的 IP 地址
            print(f"wlan_user_ip: {wlan_user_ip}")
            return wlan_user_ip
        else:
            print("wlan_user_ip not found in the response.")
            return 0
    else:
        print(f"Request failed with status code {response.status_code}")
        return 0
    

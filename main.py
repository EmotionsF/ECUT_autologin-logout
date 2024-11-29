# -*- coding:utf-8 -*-
# @author : washiobi3109@gmail.com
# @Github : https://github.com/EmotionsF
# @Time : 2021/4/10 7:57 下午（第一版）
# @Time : 2024/11/29 19:00 傍晚（改进版）
from autoLogin import *
from manualLogout import *
from reLog import *
pre = "##########################################\n" \
      "@author : 原作者hailong学长 此为 Citrus de Hikaru 改进版\n" \
      "@Github（hailong）: https://github.com/hailong-z\n" \
      "@Github（Citrus） : https://github.com/EmotionsF\n" \
      "请确保已经在configs.yaml置了你的账号密码以及运营商！\n\n" \
      "##########################################"

if __name__ == "__main__":
    print(pre)
    print("选择操作：")
    print("1. 自动登录")
    print("2. 手动登出")
    print("3. 重新登录")
    choice = input("请输入数字 (1或2)：")

    if choice == "1":
        autoLogin()
    elif choice == "2":
        manualLogout()
    elif choice == "3":
        reLog()
    else:
        print("无效的选择！你等会再来把")
        time.sleep(2)
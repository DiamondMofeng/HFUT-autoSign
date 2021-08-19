# coding=utf-8

import random
import time
import json
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from selenium import webdriver
from time import sleep
import os


# ####DEF PART#####
# def getLoginInfo():
def isElementExists_byXpath(browser, elementXpath):
    isExists = True
    try:
        browser.find_element_by_xpath(elementXpath)
        # print("今日未填报")
        return isExists
    except:
        isExists = False
        # print("今日已填报或未找到入口")
        return isExists


def emailModule(subject, text):
    # 打开config.json并读取是否启用邮件模块，以及其他信息
    configFile = open("config.json", "r", encoding="utf-8")
    config = json.loads(configFile.read())
    enable = config["是否启用邮件模块"]
    if enable == False:
        return
    mailserver = config["邮箱的smtp服务器地址"]
    sender = config["发件人邮箱账号"]
    passwd = config["发件人邮箱授权码"]
    receiver = config["收件人邮箱账号"]

    configFile.close()

    # 邮件内容部分

    msg = MIMEText(text)  # 主体，同时赋予文本
    msg['From'] = Header("HFUT-自动打卡", 'utf-8')  # 发送者
    # msg['To'] = Header("", 'utf-8')  # 接收者
    msg['Subject'] = Header(subject, 'utf-8')  # 标题

    # 邮件发送部分

    server = smtplib.SMTP(mailserver, 25)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(sender, passwd)  # 发件人邮箱账号、邮箱授权码
    # msg.as_string()中as_string()是将msg(MIMEText或MIMEMultipart对象)变为str。
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()


# #####MAIN######


try:
    # 从config.json读取驱动路径
    configFile = open("config.json", "r", encoding="utf-8")
    configInfo = json.loads(configFile.read())
    PATH = configInfo['驱动路径']
    # 打开浏览器
    br = webdriver.Chrome(executable_path=PATH)
    # 打开HFUT学工工作平台,并登录HFUT CAS统一认证平台
    br.get("https://cas.hfut.edu.cn/cas/login")

    # 从config.json读取用户名(学号)，密码并登录
    # print(configInfo.items())#for debug
    username = configInfo['学号']
    password = configInfo['密码']
    configFile.close()
    # 填入学号密码
    br.find_element_by_id("username").send_keys(username)
    br.find_element_by_id("pwd").send_keys(password)

    # 点击登录
    br.find_element_by_id("sb2").click()

    if isElementExists_byXpath(br, '/html/body/div[2]/div/div[2]/form/div[2]/div/span/div/span'):
        br.close()
        print("学号/密码错误！")
        raise Exception
    # 进入学生疫情信息收集页面

    br.get("http://stu.hfut.edu.cn/xsfw/sys/xsyqxxsjapp/*default/index.do#/mrbpa")
    sleep(random.randint(3, 5))
    br.find_element_by_xpath("/html/body/div[1]/div/div/div/div/button[1]").click()
    sleep(random.randint(3, 5))

    # 判断今日是否未填报
    if isElementExists_byXpath(br, '//*[@id="save"]') == False:

        if isElementExists_byXpath(br, '/html/body/main/article/section/div/div[3]/div[2]/div/div[4]/div['
                                       '2]/div/table/tbody/tr[1]/td[2]/a[1]'):
            print("自动打卡失败！原因：可能已打过卡""，若不放心请登录今日校园检查")
            emailModule("自动打卡失败！原因：可能已打过卡", "可能今日已打过卡，若不放心请登录今日校园检查")
        else:
            print("自动打卡失败！原因：可能程序出现故障"".今日请手动打卡，闲时可向作者反馈问题")
            emailModule("自动打卡失败！原因：可能程序出现故障", "可能程序出现故障，今日请手动打卡，闲时可向作者反馈问题")

    else:
        # 点击保存按钮，提交打卡信息
        br.find_element_by_xpath('//*[@id="save"]').click()
        print("自动打卡成功！")
        emailModule("自动打卡成功！", "于" + time.strftime("%Y-%m-%d-%H时%M分%S秒", time.localtime()) + "进行了自动打卡")

    br.close()
except:
    br.close()
    print("自动打卡失败！"", 程序运行出现错误")
    os.system('pause')
    emailModule("自动打卡失败！", "程序运行出现错误")

# HFUT-疫情信息填报自动打卡
## 免责声明：
若您下载本脚本，则视为您已经阅读、了解并接受以下内容：

本脚本仅供同学在确认所提交的疫情相关报备信息准确无误的情况下使用，若其中涉及的任何内容发生改变，须根据真实情况自行修改疫情信息报备内容。
因使用本脚本可能带来的任何风险问题均由使用者本人承担。

## 介绍：
基于selenium的自动打卡脚本，原理为模拟浏览器操作，自动按前一天的疫情信息填报内容进行打卡。

（虽然这种方法显得不太高级，碍于技术有限……其他原理实现(http请求)可见
[ qdddz / HFUT_AutoSubmit ](https://github.com/qdddz/HFUT_AutoSubmit)
(一开始也是用的selenium……)

## 使用方法：

(git actions还没用过..因为我有服务器用所以自动化部署比较方便)
## 使用方法没有写完，如果你没有阅读脚本中代码的能力（这个代码很低级），请不要跟着往下做，实在太不值得了

### 1.安装python
<https://www.python.org/downloads/>

安装时不要取消勾选pip!

### 2.下载本脚本并解压
<https://github.com/DiamondMofeng/HFUT-autoSign/archive/refs/heads/main.zip>
### 3.为脚本下载python依赖包
win+R并输入cmd进入命令行窗口，

输入脚本所在硬盘分区的 盘符+冒号 
(如你的脚本下载在D盘，则输入   D：  )

输入cd 空格 脚本所在文件夹路径
(如你的脚本下载并解压到了D:\python\HFUT-autoSign,则输入   cd D:\python\HFUT-autoSign)

输入下列指令以安装所需python包

pip install -r requirements.txt
### 4.配置config.json
用记事本或其他文本编辑器(注意打开格式为utf-8)修改config.json文件中对应项的值，其中学号和密码为学校的[CAS统一身份认证登录](https://cas.hfut.edu.cn/cas/login)
中所对应的学号和密码信息

Selenuim相关信息和邮件模块相关信息详见后节

(config.json中的数据仅用于脚本中登录和邮件提醒功能，且仅保存于本地，
不会泄露至网络上其他任何地方，可查看本脚本代码以证明这一点)

### 5.配置Selenuim相关信息
…………………………

在这一步结束后，脚本就大致可以使用了，直接使用python运行main.py即可。

---
### 6.(可选)配置邮件模块相关信息

### 7.(可选)为脚本配置计划任务以达到每日自动运行的效果~~


## 其他：
文档写到一半突然觉得没有写下去的意义了，因为小小的脚本从零开始配置居然如此麻烦，
所需时间甚至很可能会超过一个学期点开今日校园手动打卡的时间总和…………
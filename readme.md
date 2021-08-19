# HFUT-疫情信息填报自动打卡
## 免责声明：
若您下载本脚本，则视为您已经阅读、了解并接受以下内容：

本脚本仅供同学在确认所提交的疫情相关报备信息准确无误的情况下使用，若其中涉及的任何内容发生改变，须根据真实情况自行修改疫情信息报备内容。
因使用本脚本可能带来的任何风险问题均由使用者本人承担。

## 介绍：
基于selenium的自动打卡脚本，原理为模拟浏览器操作，自动按前一天的疫情信息填报内容进行打卡。

同时提供邮件功能，通过配置邮箱的smtp服务器以实现脚本运行结果的反馈。

（虽然自动模拟浏览器操作这种方法显得不太高级，碍于技术有限……其他原理实现(http请求)可见
[ qdddz / HFUT_AutoSubmit ](https://github.com/qdddz/HFUT_AutoSubmit)
(一开始也是用的selenium……)

## 使用方法：

(因为我有服务器，部署比较方便，还没有用过github Actions,不过看起来很方便)

###提供的配置文件暂时只支持chrome，想用别的浏览器的话可以先修改脚本

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

不知道该怎么写，最好网上找个教程然后改main里面的代码

配置文件里暂时只支持Google Chrome.

(1)从<http://npm.taobao.org/mirrors/chromedriver/>找到对应你本地chrome版本的驱动并下载

(需要下载叫chromedriver.exe的文件，位于 版本号/ （是个文件夹）内)

(2)解压并把chromedriver.exe放到一个你喜欢的地方。如果你放到python的安装目录下，可以跳过(3)

(3)为chromedriver.exe所在的文件夹引入系统环境变量PATH，具体如何操作可以
[百度](https://zhidao.baidu.com/question/204690598371989925.html)

因为python在安装时，可以将安装目录添加进系统环境变量PATH，所以……

(4)在config.json中，将"驱动路径"的值修改为chromedriver.exe的路径，
注意末端不用加.exe，且文件夹\文件之间为两个反斜杠\\

在这一步结束后，脚本就大致可以使用了，直接使用python运行main.py即可。
各种异常报错百度即可解决。

---
### 6.(可选)配置邮件模块相关信息

"是否启用邮件模块":false,//控制开关

"邮箱的smtp服务器地址":"smtp.qq.com",//从网上搜索你的邮箱所对应的smtp服务器

"发件人邮箱账号":"sample@qq.com",//你的邮箱账号

"发件人邮箱授权码":"auth**** code****",//这个授权码并不是你的邮箱密码，请从网上搜索如何获取smtp授权码

"收件人邮箱账号":"sample@qq.com",//可以自己发给自己

上述各项修改完成后可以运行脚本测试，若出现问题，控制台中应该会有异常提示，进行百度就好

### 7.(可选)为脚本配置计划任务以达到每日自动运行的效果

Windows环境下可以参考百度经验[如何用windows任务计划程序设置程序定时任务](https://jingyan.baidu.com/article/154b463130041128ca8f41c7.html)

Linux环境下可以使用crontab.

如果是在你的个人电脑上进行计划任务的话需要保持开机..

## 其他：
文档写到一半突然觉得没有写下去的意义了，因为小小的脚本从零开始配置居然如此麻烦，
所需时间甚至很可能会超过一个学期点开今日校园手动打卡的时间总和…………

或许把脚本放入github Actions可以极大的节约时间
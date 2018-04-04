# coding:utf-8
import random
import time
import sys
from urllib import request

from selenium import webdriver
# 引入配置对象DesiredCapabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Loginer:
    def __init__(self,url,username,password):
        self.LoginUrl=url
        self.username=username
        self.password=password

    def MY_USER(self):
        MY_USER_AGENT = [
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" ,
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
            ]
        return MY_USER_AGENT

    def login(self):
        print("Procedure Begin...")

        #测试网线是否插好
        try:
            status=request.urlopen(self.LoginUrl).code
            print("ping "+self.LoginUrl+" return "+str(status))
        except:
            return "4"

        dcap = dict(DesiredCapabilities.PHANTOMJS)
        # 从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
        print("UserAgent:\t"+random.choice(self.MY_USER()))
        dcap["phantomjs.page.settings.userAgent"] = (random.choice(self.MY_USER())+"")
        # aa=random.choice(self.MY_USER())+""
        # dcap["phantomjs.page.settings.userAgent"]=(aa)

        # 不载入图片，爬页面速度会快很多
        # dcap["phantomjs.page.settings.loadImages"] = False

        # 打开带配置信息的phantomJS浏览器
        executable_path = r'E:\PhantomjsChromedriver\phantomjs-2.1.1-windows\bin\phantomjs.exe'
        # 构造网页驱动
        driver = webdriver.PhantomJS(executable_path , desired_capabilities=dcap,service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])

        # 设置10秒页面超时返回,以前遇到过driver.get(url)一直不返回，但也不报错的问题，这时程序会卡住，设置超时选项能解决这个问题。
        driver.set_page_load_timeout(10)

        TIME = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
        print(TIME+"  Beginning to load PhantomJS")

        driver.get(self.LoginUrl)  # 打开网页

        TIME = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
        print(TIME+"  Beginning to open the URL:"+self.LoginUrl)
        for i in range(1,2):
            time.sleep(1)
            TIME = time.strftime('%Y-%m-%d-%H%M%S', time.localtime(time.time()))
            driver.save_screenshot(TIME + '.png')
        try:

            print("Input the PostData")
            #下面的xpath需要结合自己的情况去设计
            # print(driver.find_element_by_xpath(".//div[@id='inputs']/input[@id='username']"))
            driver.find_element_by_xpath(".//div[@id='inputs']/input[@id='username']").send_keys(self.username)
            driver.find_element_by_xpath(".//div[@id='inputs']/input[@id='password']").send_keys(self.password)
            print('Input is ok!')

            # driver.get_screenshot_as_file('验证码.png')               # 截取当前页面的图片
            # input_solution = input('请输入验证码 :')            #手工打码
            # driver.find_element_by_xpath('//input[@name="captcha"]').send_keys(input_solution)
            # time.sleep(2)

            TIME = time.strftime('%Y-%m-%d-%H%M%S', time.localtime(time.time()))
            driver.save_screenshot(TIME + '.png')
        except:
            print("Input is failed!")
            driver.quit()
            return "2"
        try:
            # print(driver.find_element_by_xpath("//div[@id='btn']/input[@id='submit'][1]"))
            driver.find_element_by_xpath(".//div[@id='btn']/input[@id='submit'][1]").click()  # 表单的提交  表单的提交，可以选择登录按钮然后使用click方法，也可以选择表单然后使用submit方法
            print('Submit is ok!')
        except:
            print("Submit is failed!")
            driver.quit()
            return "3"

        try:
            print("Page return:")
            for i in range(1,2):
                time.sleep(1)
                TIME=time.strftime('%Y-%m-%d-%H%M%S', time.localtime(time.time()))
                driver.save_screenshot(TIME+'.png')
                res=driver.find_element_by_xpath(".//div[@id='btn']/input[@id='submit']")
            print("Submit value:"+res.get_attribute("value"))
            if res.get_attribute("value")[0]=="注":
                driver.save_screenshot('successed.png')  # 截取当前页面的图片
                driver.quit()
                return "0"
            else:
                driver.save_screenshot("failed1.png")
                driver.quit()
                return "1"
        except:
            print('登录失败')
            driver.quit()
            return "4"

def main():
    username = input("Enter username:")
    password = input("Enter password:")
    url = "http://172.18.2.2/0.htm"
    do = Loginer(url, username, password)
    value=do.login()
    if (value=="0"):
        print("Successfully!")
        sys.exit(0)     #程序退出
    return value

if __name__=="__main__":
    value=main()
    # print(value[0])
    while(value!="0"):
        if(value=="1"):
            print("failed! Please check the username or password and try again!")
        elif(value=="2"):
            print("failed Please  check the input!")
        elif(value=="3"):
            print("failed Please check the submit!")
        elif(value=="4"):
            print("failed Please check the NetWork!")
        value=main()

    sys.exit(0)

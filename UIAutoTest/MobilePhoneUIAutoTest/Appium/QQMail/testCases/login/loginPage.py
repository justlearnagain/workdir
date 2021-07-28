import sys
from selenium.webdriver.common.by import By
sys.path.append("../../")
from Pages.basePage import basePage
from config.data import loginData

class loginPage(basePage):
    # 多个编辑窗口-关闭按钮
    closeBtn = "com.tencent.androidqqmail:id/bb5"
    # 同意邮箱协议
    hz = "com.tencent.androidqqmail:id/hz"
    # 同意按钮
    agreeBtn = "com.tencent.androidqqmail:id/aqa"
    # 163邮箱
    mailAccessibilityId = "163邮箱"
    mailXpath = "//android.widget.ImageView[@content-desc=\"163邮箱\"]"
    # 登录163邮箱文本
    mailText163 = "com.tencent.androidqqmail:id/az_"
    # 邮箱
    email = "com.tencent.androidqqmail:id/l"
    # 密码
    passWord = "com.tencent.androidqqmail:id/a1p"
    # 登录按钮
    enterBtn= "com.tencent.androidqqmail:id/az7"
    # 进入邮箱按钮
    enterMail = "com.tencent.androidqqmail:id/bd4"
    # 邮箱主页邮箱名称文本
    mailMainUser = "com.tencent.androidqqmail:id/afc"
    # 密码输入错误后的文本提示
    errorEmailText = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView"
    # 密码输入错误后点击确定按钮
    errorEmailAgreeBtn = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[1]"

    def __init__(self, driver):
        basePage.__init__(self, driver)

    # 多个编辑窗口、用户协议窗口、选择163邮箱
    def userNotice(self):
        self.driver.implicitly_wait(10)
        # 关闭多个编辑窗口
        # 进入登录页面比较慢，等待10秒
        self.click(By.ID, self.closeBtn)
        # 同意用户协议
        self.click(By.ID, self.hz)
        # 点击确定按钮
        self.click(By.ID, self.agreeBtn)
        # 选择163邮箱
        self.click(By.XPATH, self.mailXpath)

    # 判断页面是否正确
    def judgeLoginPage(self):
        self.driver.implicitly_wait(10)
        # 判断页面是否有登录163邮箱这几个字
        assert self.get_text(By.ID, self.mailText163) == "登录163邮箱"
        # 判断“登录”按钮是否为灰色
        assert self.get_att("enabled", By.ID, self.enterBtn) == "false"

    # 输入正确账号和密码登录
    def successLogin(self):
        self.driver.implicitly_wait(10)
        # 输入账号密码登录
        self.click(By.ID, self.email)
        self.send_keys(loginData["trueUsername"], By.ID, self.email)
        self.click(By.ID, self.passWord)
        self.send_keys(loginData["truePassword"], By.ID, self.passWord)
        self.click(By.ID, self.enterBtn)
        self.click(By.ID, self.enterMail)
        # 判断是否进入邮箱主页面
        assert self.get_text(By.ID, self.mailMainUser) == "smallteaforever@163.com"

    # 输入错误账号登录
    def errorLogin(self):
        self.driver.implicitly_wait(10)
        # 不输入账号登录
        self.clear(By.ID, self.email)
        self.clear(By.ID, self.passWord)
        self.click(By.ID, self.passWord)
        self.send_keys(loginData["truePassword"], By.ID, self.passWord)
        self.click(By.ID, self.enterBtn)
        assert self.get_att("enabled", By.ID, self.enterBtn) == "false"

        # 不输入密码登录
        self.clear(By.ID, self.email)
        self.clear(By.ID, self.passWord)
        self.click(By.ID, self.email)
        self.send_keys(loginData["trueUsername"], By.ID, self.email)
        self.click(By.ID, self.enterBtn)
        assert self.get_att("enabled", By.ID, self.enterBtn) == "false"

        '''
        # 输入错误格式的的账号和密码
        self.clear(By.ID, self.email)
        self.clear(By.ID, self.passWord)
        self.click(By.ID, self.email)
        self.send_keys(loginData["errFormatUsername"], By.ID, self.email)
        self.click(By.ID, self.passWord)
        self.send_keys(loginData["errPassword"], By.ID, self.passWord)
        assert self.get_att("enabled", By.ID, self.enterBtn) == "true"
        self.click(By.ID, self.enterBtn)
        #assert self.get_text(By.ID, self.errorEmailText) == "帐号或密码错误"
        #self.click(By.ID, self.errorEmailAgreeBtn)
        '''

        # 输入错误的账号和密码
        self.clear(By.ID, self.email)
        self.clear(By.ID, self.passWord)
        self.click(By.ID, self.email)
        self.send_keys(loginData["errUsername"], By.ID, self.email)
        self.click(By.ID, self.passWord)
        self.send_keys(loginData["errPassword"], By.ID, self.passWord)
        assert self.get_att("enabled", By.ID, self.enterBtn) == "true"
        self.click(By.ID, self.enterBtn)
        #assert self.get_text(By.ID, self.errorEmailText) == "帐号或密码错误"
        #self.click(By.ID, self.errorEmailAgreeBtn)
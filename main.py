PROMISED_DOWN = '20Mbps'
PROMISED_UP = '2Mbps'
CHROME_DRIVER_PATH = '/home/vishal/Downloads/chromedriver'
TWITTER_EMAIL = 'Your registered email id'
TWITTER_PASSWORD = 'Your password'

from selenium import webdriver
import time

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.up = ''
        self.down = ''
        
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(100)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(self.down, self.up)
    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/?lang=en')
        time.sleep(5)
        log_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span').click()
        time.sleep(5)
        email = self.driver.find_element_by_name('session[username_or_email]').send_keys(TWITTER_EMAIL)
        password = self.driver.find_element_by_name('session[password]').send_keys(TWITTER_PASSWORD+'\n')
        
        message = f"Hey Internet Provider! Why is my internet speed {self.down}Mbps down/{self.up}Mbps up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up"
        time.sleep(100)
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div').click()
        time.sleep(5)
        tweet_input = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        tweet_input.send_keys(message+'\n')
        send = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]/div/span/span').click()

        
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

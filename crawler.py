from selenium import webdriver
import pickle
from bs4 import BeautifulSoup as bs

# login with cookie: https://stackoverflow.com/questions/45417335/python-use-cookie-to-login-with-selenium
def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)

def get_driver(mode=''):
	options = ''
	# headless mode
	# references: https://stackoverflow.com/questions/16180428/can-selenium-webdriver-open-browser-windows-silently-in-background
	if mode is 'headless':
		options = webdriver.ChromeOptions()
		options.add_argument("headless")
	driver = webdriver.Chrome(executable_path='/webdriver/chromedriver', chrome_options=options)
	driver.implicitly_wait(3)
	return driver

def login_naver(driver, userid, userpw):
	driver.get('https://nid.naver.com/nidlogin.login')
	driver.implicitly_wait(5)
	driver.find_element_by_name('id').send_keys(userid)
	driver.find_element_by_name('pw').send_keys(userpw)
	driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

def check_login(driver):
	driver.switch_to_frame('minime')
	html = driver.page_source
	soup = bs(html, 'html.parser')
	print(soup.select('strong#user_name')[0])

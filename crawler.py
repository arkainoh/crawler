from selenium import webdriver
import pickle
from bs4 import BeautifulSoup as bs

# read from configuration
chromedriver_path = '/webdriver/chromedriver'

# login with cookie
# reference: https://stackoverflow.com/questions/45417335/python-use-cookie-to-login-with-selenium
def save_cookie(browser, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(browser.get_cookies(), filehandler)

def load_cookie(browser, path):
  # need to browser.refresh() after call this function
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            browser.add_cookie(cookie)

def open_browser(mode=''):
  options = ''
  # headless mode
  # reference: https://stackoverflow.com/questions/16180428/can-selenium-webdriver-open-browser-windows-silently-in-background
  if mode is 'invisible':
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
  browser = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)
  browser.implicitly_wait(3)
  return browser

def login_naver(browser, userid, userpw):
  browser.get('https://nid.naver.com/nidlogin.login')
  browser.implicitly_wait(5)
  browser.find_element_by_name('id').send_keys(userid)
  browser.find_element_by_name('pw').send_keys(userpw)
  browser.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

def check_login(browser):
  browser.switch_to_frame('minime')
  html = browser.page_source
  soup = bs(html, 'html.parser')
  print(soup.select('strong#user_name')[0])

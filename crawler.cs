using OpenQA.Selenium;
using OpenQA.Selenium.IE;
using System.Threading;

/***************************************************
  Tips:
  (1) If the browser doesn't show up, enable protected mode for all zones in the security tab of Internet Options, and apply zoom 100%.
  (2) If SendKeys() is too slow, use 32-bit IEDriverServer.exe instead of 64-bit one.
****************************************************/

// path of IEDriverServer: %PROJECT_PATH%\bin\Debug
IWebDriver open_browser(string mode = "")
{
  var driverService = InternetExplorerDriverService.CreateDefaultService();
  driverService.HideCommandPromptWindow = true;
  IWebDriver browser = new InternetExplorerDriver(driverService); // PATH: %PROJECT_PATH%\bin\Debug
  if (mode.Equals("invisible")) browser.Manage().Window.Minimize();
  return browser;
}

void login_naver(IWebDriver browser, string userid, string userpw)
{
  browser.Url = "https://nid.naver.com/nidlogin.login";
  IWebElement login_id = browser.FindElement(By.Name("id"));
  IWebElement login_pw = browser.FindElement(By.Name("pw"));
  IWebElement login_button = browser.FindElement(By.XPath("//*[@id=\"frmNIDLogin\"]/fieldset/input"));
  login_id.Clear();
  login_pw.Clear();
  login_id.SendKeys(userid);
  login_pw.SendKeys(userpw);
  login_button.Click();
}

void check_login(IWebDriver browser)
{
  browser.SwitchTo().Frame("minime");
  IWebElement user_name = browser.FindElement(By.Id("user_name"));
  MessageBox.Show(user_name.Text);
}
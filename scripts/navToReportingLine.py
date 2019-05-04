from selenium import webdriver
from homepage import locate
from webdriver_manager.chrome import ChromeDriverManager

class navigateToReportingLine():

    def test(self):
        baseUrl = "https://www.mga.edu"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(2)
        element = driver.find_element_by_xpath(locate('reporting line'))
        element.click()
        driver.implicitly_wait(2)

       
nav = navigateToReportingLine()
nav.test()
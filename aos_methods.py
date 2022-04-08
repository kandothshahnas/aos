import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import aos_locators as locators
s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)
aos_url = 'https://advantageonlineshopping.com/'

def setup():
    print('-------------------------------*set up*----------------------')
    print(f'-----------Test started @{datetime.datetime.now()}------------------')
    #maximise window
    driver.maximize_window()
    driver.implicitly_wait(30)
    #navigate to advantageshoppingonline webpage
    driver.get(locators.aos_url)
    aos_title =driver.title
    if driver.current_url == locators.aos_url and driver.title == aos_title:
        print(f'We are at the correct web page {driver.current_url}')
        print(f'We are seeing the title of web page as : {driver.title}')
    else:
        print(f'We are not at the correct web page!! check your code')
        driver.close()  # close the current tab
        driver.quit()  # close the browser completely

def teardown():
    if driver is not None:
        print('-----------------*tear down*------------------')
        print(f'Test completed at:{datetime.datetime.now()}')
        driver.close()
        driver.quit()

def create_new_account():
    print('-------------------*create new account*--------------')
    driver.implicitly_wait(3)
    assert driver.find_element(By.ID,'menuUser').is_displayed()
    #driver.implicitly_wait(3)
    driver.find_element(By.ID,'menuUser').click()
    sleep(3)
    driver.find_element(By.XPATH, "//a[@class = 'create-new-account ng-scope']").click()
    sleep(0.25)
    driver.find_element(By.XPATH,"//input[@name = 'usernameRegisterPage']").send_keys(locators.aos_username)
    sleep(0.25)
    driver.find_element(By.XPATH,"//input[@name = 'emailRegisterPage']").send_keys(locators.aos_email)
    sleep(0.25)
    driver.find_element(By.XPATH,"//input[@name = 'passwordRegisterPage']").send_keys(locators.aos_password)
    sleep(0.25)
    driver.find_element(By.XPATH,"//input[@name = 'confirm_passwordRegisterPage']").send_keys(locators.aos_password)
    driver.find_element(By.XPATH, "//input[@name = 'first_nameRegisterPage']").send_keys(locators.first_name)
    driver.find_element(By.XPATH, "//input[@name = 'last_nameRegisterPage']").send_keys(locators.last_name)
    driver.find_element(By.XPATH, "//input[@name = 'phone_numberRegisterPage']").send_keys(locators.phone)
    #Select(driver.find_element(By.XPATH,"//select")).select_by_visible_text('Canada')
    driver.find_element(By.XPATH,"//select/option[@label='Canada']").click()

    sleep(0.25)
    driver.find_element(By.XPATH, "//input[@name = 'cityRegisterPage']").send_keys(locators.city)
 #aos_address = f'{fake.street_address()}, {fake.street_name()}'
    driver.find_element(By.XPATH, "//input[@name = 'addressRegisterPage']").send_keys(locators.address)
    driver.find_element(By.XPATH, "//input[@name = 'state_/_province_/_regionRegisterPage']").send_keys(locators.province)
    driver.find_element(By.XPATH, "//input[@name = 'postal_codeRegisterPage']").send_keys(locators.postal_code)
    sleep(0.25)
    driver.find_element(By.XPATH,"//input[@name = 'i_agree']").click()
    sleep(0.25)
    driver.find_element(By.ID,"register_btnundefined").click()
    sleep(0.25)
    breakpoint()
    #check usename is displayed
    driver.find_element(By.XPATH, "//span[@class='hi-user containMiniTitle ng-binding']").is_displayed()
    print(f'username {locators.aos_username}displayed at the top menu')
    sleep(0.25)
    print("\n")

def logOut():
    print('----------------*log out *-----------------')
    driver.find_element(By.XPATH, "//span[@class='hi-user containMiniTitle ng-binding']").click()
    driver.find_element(By.XPATH,"//div[@class='mini-title']/label[@href='javascript:void(0)'][3]").click()
    print(f'user  logged out successfuly at :{datetime.datetime.now()}')


def logIn(username,password):
    print("----------------*log in*-------------------")
    driver.get(aos_url)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys(username)
    sleep(0.25)
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)
    sleep(0.25)
    driver.find_element(By.XPATH,"//button[@id='sign_in_btnundefined']").click()
    sleep(0.25)
    print(f'user {locators.full_name} is logged in successfully at:{datetime.datetime.now()}')
    driver.find_element(By.XPATH,"//span[@class='hi-user containMiniTitle ng-binding']").is_displayed()
    print('username displayed at the top menu')
#Lab 4
def validate_dash_borad():
    print('--------------*validate dashboard*-------------')
    #check the advantageDEMO logo is present
    sleep(2)
    display = driver.find_element(By.XPATH,"//div[@class='logo']/a").is_displayed()
    sleep(0.25)
    if display:
        print('--dashborad logo for AOS is displayed--')
    else:
        print('--dashborad logo for AOS is not displayed--')
    #check SPEAKER text is diplayed
    display = driver.find_element(By.XPATH, "//span[@id ='speakersTxt']").is_displayed()
    sleep(0.25)
    if display:
        print('--SPEAKERS text  is displayed--')
    else:
        print('--SPEAKERS text is not displayed--')
    #check TABLETS text is displayed
    display = driver.find_element(By.XPATH, "//span[@id ='speakersTxt']").is_displayed()
    sleep(0.25)
    if display:
        print('-- text  is displayed--')
    else:
        print('--SPEAKERS text is not displayed--')

#



#setup()
#validate_dash_borad()
#create_new_account()
#logOut()
#logIn()
#logOut()
#teardown()




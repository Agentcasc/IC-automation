from selenium import webdriver
import time

while True:
    try:
        print('executing')
        PATH = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        driver = webdriver.Chrome(PATH)

        driver.get("https://ic.leusd.k12.ca.us/campus/portal/students/lakeElsinore.jsp")

        user_input = driver.find_element_by_id('username')
        user_input.send_keys("312299")
        pass_input = driver.find_element_by_id('password')
        pass_input.send_keys("06162008")
        print('logging in')

        login_button = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/input[6]")
        login_button.click()

        time.sleep(5)
        driver.switch_to.frame("main-workspace")
        time.sleep(5)
        ##### Find Class check in
        class_button = driver.find_element_by_xpath("/html/body/app-root/ng-component/app-today/app-portal-page/div[2]/app-payments-cart/div/div/div[1]/app-attendance-checkin-list/div/div/ul/li")
        time.sleep(5)
        class_button.click() ##### Enter class check in environment
        time.sleep(5)
        ##### Find Check in button
        yes_im_here = driver.find_element_by_xpath("/html/body/app-root/ng-component/app-attendance-checkin/app-portal-page/div[2]/div/div/div[2]/div/div[2]/button")
        yes_im_here.click() ##### Click check in Button
        print('checking in')
        driver.quit()
    except:
        print("couldn't find check in button")
        print("breaking")
        break
    finally:
        driver.quit()

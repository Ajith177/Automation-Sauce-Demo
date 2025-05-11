import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from colorama import Fore
import shutil
import os
import pytest


class Test_Login:
    target_folder = r'C:\Users\AJITH\PycharmProjects\PythonProject\Sauce-demo\Screenshots'
    email_input = "//input[contains(@placeholder,'Username')]"
    password_input="//input[contains(@placeholder,'Password')]"
    login_button = "//input[contains(@name,'login-button')]"
    taking_user_name_1 = "//div[contains(@id,'login_credentials')]"

    # By the above User_name Credentials User can able to Select the list of User_name that get listed in the UI.

    @pytest.mark.run(order=1)
    def test_case_one(self, driver):
        print("Running test_case_one")
        time.sleep(2)
        screenshot_file = "Testcase_1.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        print(Fore.RED + "The entered URL is Correct")
        time.sleep(2)
        print(Fore.GREEN + "Login Page opened successfully")

    @pytest.mark.run(order=2)
    def test_case_two(self, driver):
        print("Checking the Email Input")
        driver.execute_script("alert('Entering the Input on the Input Box')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()

    @pytest.mark.run(order=3)
    def test_case_three(self, driver):
        print("Entering the random Values in the Email Fields")
        email = driver.find_element(By.XPATH, self.email_input).send_keys("random")
        time.sleep(5)
        driver.execute_script("alert('Entering the Small Characters in the Input Box')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()

    @pytest.mark.run(order=4)
    def test_case_four(self, driver):
        driver.execute_script("alert('Click on Login Button and Check Whether it is Logging in or Not')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        login_button = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        screenshot_file = "Testcase_4.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)
        print(Fore.GREEN, "Clicking on the Login Button by Not filling the Password")

    @pytest.mark.run(order=5)
    def test_case_five(self, driver):
        print("Moving to Next steps")
        time.sleep(2)
        print("Clearing the Username Input")
        clearing_the_email_Input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        cleared_the_email_Input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        screenshot_file = "Testcase_5.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)
        print("Username Input is get Cleared")

    @pytest.mark.run(order=6)
    def test_case_six(self, driver):
        driver.execute_script("alert('Printing the Capital letters length less than 5 for User-name Input')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        email_input = driver.find_element(By.XPATH, self.email_input).send_keys("DEMO")
        time.sleep(2)
        driver.execute_script("alert('Click on login Button to check the Login Functionality')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_6.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=7)
    def test_case_seven(self, driver):
        login_button = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        screenshot_file = "Testcase_7.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)
        driver.execute_script("alert('It is Not get Logged in by empty Password')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()

    @pytest.mark.run(order=8)
    def test_case_eight(self, driver):
        print(Fore.LIGHTRED_EX,"Clearing the Input of the User-name")
        clearing_the_email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        cleared_email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        driver.refresh()
        driver.execute_script("alert('User-name input get Cleared')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_8.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=9)
    def test_case_nine(self, driver):
        email_input = driver.find_element(By.XPATH, self.email_input).send_keys("DEMOUSERSADF")
        time.sleep(2)
        login_button = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        driver.execute_script("alert('Giving the Username Input (Capital) greater than 5')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_9.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=10)
    def test_case_ten(self, driver):
        print(Fore.BLACK,"Clearing the Input of the Username Input")
        clearing_email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        cleared_email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        print("User-name Input Cleared -> Test Case 10")
        driver.refresh()
        time.sleep(2)
        email_input = driver.find_element(By.XPATH, self.email_input).send_keys("12344")
        time.sleep(2)
        print("Giving the Numbers Input in the User-name")
        login_button = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        driver.execute_script("alert('Giving the User-name Input as Numbers')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        screenshot_file = "Testcase_10.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=11)
    def test_case_eleven(self, driver):
        print(Fore.CYAN,"Clearing the Input of the User-name Input for 11th Test case")
        clearing_email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        cleared_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        email_input = driver.find_element(By.XPATH, self.email_input).send_keys("762525252572727373736363")
        time.sleep(2)
        driver.execute_script("alert('Giving the User-name Input as Numbers length > 10')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        login_button = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        screenshot_file = "Testcase_11.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=12)
    def test_case_twelve(self, driver):
        print(Fore.MAGENTA,"Clearing the Input of the User-name Input for the 12th Test Case")
        clearing_email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        cleared_email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.BACKSPACE)
        time.sleep(3)
        driver.refresh()
        email_input = driver.find_element(By.XPATH, self.email_input).send_keys("@#$%")
        time.sleep(2)
        clicking_on_login_button = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        driver.execute_script("alert('Giving the User-name Input as Special Characters length < 10')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_12.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=13)
    def test_case_thirteen(self, driver):
        print(Fore.LIGHTBLUE_EX,"Clearing the Input of the User-name Input for 13th Test Case")
        clearing_email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        cleared_email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.BACKSPACE)
        time.sleep(3)
        driver.refresh()
        email_input = driver.find_element(By.XPATH, self.email_input).send_keys("@#$%#$%^&*(")
        time.sleep(2)
        clicking_on_login_button = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        driver.execute_script("alert('Giving the User-name Input as Special Characters length > 10')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_13.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=14)
    def test_case_fourteen(self, driver):
        print(Fore.LIGHTMAGENTA_EX,"Clearing the Input of the User-name Input for 14th Test Case")
        clearing_email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        cleared_email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.BACKSPACE)
        time.sleep(3)
        driver.refresh()
        time.sleep(3)
        taking_usser_name_on_UI = driver.find_element(By.XPATH, self.taking_user_name_1)
        a = taking_usser_name_on_UI.text
        lines = a.splitlines()
        first_name_in_UI = lines[1]
        print(Fore.GREEN, "Entering the data that get displayed in the UI")
        email_input = driver.find_element(By.XPATH, self.email_input).send_keys(first_name_in_UI)
        time.sleep(2)
        print("Moving to Password Input for the First time")
        time.sleep(2)
        driver.execute_script("alert('Moving to the Password Input --> For the First time')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        password_input = driver.find_element(By.XPATH, self.password_input).send_keys("HBDE")
        time.sleep(2)
        driver.execute_script("alert('Giving the Capital letters for the Password Input length < 5 ')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_14.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=15)
    def test_case_fifteen(self, driver):
        print(Fore.LIGHTBLUE_EX,"Clearing the Input of the User-name Input for 15th Test Case")
        clearing_the_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        cleared_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.refresh()
        taking_usser_name_on_UI = driver.find_element(By.XPATH, self.taking_user_name_1)
        a = taking_usser_name_on_UI.text
        lines = a.splitlines()
        second_name_in_UI = lines[2]
        time.sleep(2)
        email_input = driver.find_element(By.XPATH, self.email_input).send_keys(second_name_in_UI)
        time.sleep(2)
        entering_password_input = driver.find_element(By.XPATH, self.password_input).send_keys("DDHJEBDHJEBDJBDJBED")
        time.sleep(2)
        click_on_login_button = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        driver.execute_script("alert('Giving the Capital letters in the Password Input length > 10')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_15.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=16)
    def test_case_sixteen(self, driver):
        print(Fore.BLUE,"Clearing the Input of the User-name Input for 16th Test Case")
        clearing_the_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        cleared_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        driver.refresh()
        taking_usser_name_on_UI = driver.find_element(By.XPATH, self.taking_user_name_1)
        a = taking_usser_name_on_UI.text
        lines = a.splitlines()
        third_name_in_UI = lines[3]
        time.sleep(2)
        email_input = driver.find_element(By.XPATH, self.email_input).send_keys(third_name_in_UI)
        time.sleep(2)
        entering_password_input = driver.find_element(By.XPATH, self.password_input).send_keys("123435")
        time.sleep(2)
        login_button_click = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        driver.execute_script("alert('Giving the Numbers  in the Password Input length < 10')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_16.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=17)
    def test_case_seventeen(self, driver):
        print(Fore.CYAN,"Clearing the Input of the User-name Input for 16th Test Case")
        clearing_the_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        cleared_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        driver.refresh()
        taking_usser_name_on_UI = driver.find_element(By.XPATH, self.taking_user_name_1)
        a = taking_usser_name_on_UI.text
        lines = a.splitlines()
        fourth_name_in_UI = lines[4]
        time.sleep(2)
        email = driver.find_element(By.XPATH, self.email_input).send_keys(fourth_name_in_UI)
        time.sleep(2)
        entering_password_input = driver.find_element(By.XPATH, self.password_input).send_keys("12343572727273737373")
        time.sleep(2)
        login_button_click = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        driver.execute_script("alert('Giving the Numbers  in the Password Input length > 10')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_16.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=17)
    def test_case_seventeen(self, driver):
        print(Fore.RED, "Clearing the Input of the User-name Input for 17th Test Case")
        clearing_the_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(
            Keys.CONTROL + "a")
        time.sleep(2)
        cleared_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        driver.refresh()
        taking_usser_name_on_UI = driver.find_element(By.XPATH, self.taking_user_name_1)
        a = taking_usser_name_on_UI.text
        lines = a.splitlines()
        fourth_name_in_UI = lines[4]
        time.sleep(2)
        email = driver.find_element(By.XPATH, self.email_input).send_keys(fourth_name_in_UI)
        time.sleep(2)
        entering_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(
            "12343572727273737373")
        time.sleep(2)
        login_button_click = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        driver.execute_script("alert('Giving the Numbers  in the Password Input length > 10')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_17.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=18)
    def test_case_eighteen(self, driver):
        print(Fore.BLUE, "Clearing the Input of the User-name Input for 18th Test Case")
        clearing_the_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(
            Keys.CONTROL + "a")
        time.sleep(2)
        cleared_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        driver.refresh()
        taking_usser_name_on_UI = driver.find_element(By.XPATH, self.taking_user_name_1)
        a = taking_usser_name_on_UI.text
        lines = a.splitlines()
        fifth_name_in_UI = lines[5]
        time.sleep(2)
        email = driver.find_element(By.XPATH, self.email_input).send_keys(fifth_name_in_UI)
        time.sleep(2)
        entering_password_input = driver.find_element(By.XPATH, self.password_input).send_keys("!@##$")
        time.sleep(2)
        login_button_click = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        driver.execute_script("alert('Giving the Special Charcters  in the Password Input length < 10')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_18.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=19)
    def test_case_nineteen(self, driver):
        print(Fore.BLACK, "Clearing the Input of the User-name Input for 19th Test Case")
        clearing_the_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(
            Keys.CONTROL + "a")
        time.sleep(2)
        cleared_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        driver.refresh()
        taking_usser_name_on_UI = driver.find_element(By.XPATH, self.taking_user_name_1)
        a = taking_usser_name_on_UI.text
        lines = a.splitlines()
        sixth_name_in_UI = lines[6]
        time.sleep(2)
        email = driver.find_element(By.XPATH, self.email_input).send_keys(sixth_name_in_UI)
        time.sleep(2)
        entering_password_input = driver.find_element(By.XPATH, self.password_input).send_keys(
            "!@##$@#$%^$%^&*%^&$%^&*")
        time.sleep(2)
        login_button_click = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        driver.execute_script("alert('Giving the Special Charcters  in the Password Input length < 10')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_19.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=20)
    def test_case_twenty(self, driver):
        print(Fore.CYAN, "Clearing the Input of the User-name Input for 20th Test Case")
        email = driver.find_element(By.XPATH, self.email_input).send_keys("   ")
        time.sleep(2)
        entering_password_input = driver.find_element(By.XPATH, self.password_input).send_keys("    ")
        time.sleep(2)
        login_button_click = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        driver.execute_script("alert('Checking the Email & Password Input by Giving the Empty Spaces.')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_20.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=21)
    def test_case_twenty_one(self, driver):
        print(Fore.BLUE, "Clearing the Input of the User-name Input for 21th Test Case")
        time.sleep(2)
        email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        email_the_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.BACKSPACE)
        time.sleep(5)
        driver.refresh()
        time.sleep(2)
        email_input_1 = driver.find_element(By.XPATH, self.email_input).send_keys("fcwcgcdc225266763")
        time.sleep(2)
        password_input_1 = driver.find_element(By.XPATH, self.password_input).send_keys("98398398jnjnfrjfn")
        time.sleep(2)
        driver.execute_script(
            "alert('Checking the Email & Password by giving the Combination of Letters and numbers')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_21.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=22)
    def test_case_twenty_two(self, driver):
        print(Fore.BLUE, "Clearing the Input of the User-name Input for 22th Test Case")
        time.sleep(2)
        email_the_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.BACKSPACE)
        time.sleep(5)
        password_input_1 = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        password_input_2 = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.BACKSPACE)
        time.sleep(5)
        driver.refresh()
        email_input_3 = driver.find_element(By.XPATH, self.email_input).send_keys("BDDJDJHJRRNRHI3334343")
        time.sleep(2)
        password_input2 = driver.find_element(By.XPATH, self.password_input).send_keys("YUGDDDB8787")
        time.sleep(2)
        driver.execute_script(
            "alert('Checking the Email & Password by giving the Combination of Capital Letters and numbers')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_22.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=23)
    def test_case_twenty_three(self, driver):
        print(Fore.BLUE, "Clearing the Input of the User-name Input for 23th Test Case")
        time.sleep(2)
        email_the_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        email_input = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.BACKSPACE)
        time.sleep(5)
        password_input_1 = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        password_input_2 = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.BACKSPACE)
        time.sleep(5)
        driver.refresh()
        email_input_4 = driver.find_element(By.XPATH, self.email_input).send_keys("!@$#@%$@%$#%77687687")
        time.sleep(2)
        password_input4 = driver.find_element(By.XPATH, self.password_input).send_keys("Y^#^$^^^#%&8787")
        time.sleep(2)
        driver.execute_script(
            "alert('Checking the Email & Password by giving the Combination of Special Letters and numbers')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_23.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=24)
    def test_case_twenty_four(self, driver):
        print(Fore.BLUE, "Clearing the Input of the User-name Input for 24th Test Case")
        email_input_7 = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        email_input_8 = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        password_input_1 = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        password_input_2 = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.BACKSPACE)
        time.sleep(5)
        driver.refresh()
        email_input_11 = driver.find_element(By.XPATH, self.email_input).send_keys("")
        time.sleep(2)
        password_input_6 = driver.find_element(By.XPATH, self.password_input).send_keys("")
        time.sleep(2)
        login_button = driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)
        driver.execute_script(
            "alert('Checking the Email & Password by giving the Combination of Special Letters and numbers')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        screenshot_file = "Testcase_24.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=25)
    def test_case_twenty_four(self, driver):
        print(Fore.BLUE, "Clearing the Input of the User-name Input for 25th Test Case")
        email_input_7 = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        email_input_8 = driver.find_element(By.XPATH, self.email_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        password_input_1 = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        password_input_2 = driver.find_element(By.XPATH, self.password_input).send_keys(Keys.BACKSPACE)
        time.sleep(5)
        driver.refresh()
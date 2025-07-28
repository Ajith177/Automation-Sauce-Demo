import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from colorama import Fore
from Login.test_login_helper import LoginHelper
import shutil
import os
import pytest
from urllib3.poolmanager import key_fn_by_scheme
from Login.test_login_helper import LoginHelper
from selenium.common.exceptions import UnexpectedAlertPresentException


class Test_Swag:
    target_folder = r'C:\Users\AJITH\PycharmProjects\PythonProject\Sauce-demo\Screenshots\Swag_lab'
    click_on_three_dots="//button[contains(@id,'react-burger-menu-btn')]"
    click_on_all_items="//a[contains(text(),'All Items')]"
    click_on_about="//a[contains(text(),'About')]"
    click_on_Log_out="//a[contains(text(),'Logout')]"
    click_on_reset_app_state="//a[contains(text(),'Reset')]"
    close_btn_side_bar="//button[contains(@id,'react-burger-cross-btn')]"

    sauce_labs_back_pack = "//button[contains(@id,'add-to-cart-sauce-labs-backpack')]"
    sauce_labs_bike_light = "//button[contains(@id,'add-to-cart-sauce-labs-bike-light')]"
    sauce_labs_bolt_t_shirt = "//button[contains(@name,'add-to-cart-sauce-labs-bolt-t-shirt')]"
    sauce_labs_fleece_jacket = "//button[contains(@name,'add-to-cart-sauce-labs-fleece-jacket')]"
    sauce_labs_onesie = "//button[contains(@name,'add-to-cart-sauce-labs-onesie')]"
    sauce_labs_red_t_shirt = "//button[contains(@id,'add-to-cart-test.allthethings()-t-shirt-(red)')]"

    click_on_back_to_products="//button[contains(text(),'Back')]"

    click_on_Back_pack="//div[contains(text(),'Sauce Labs Backpack')]"
    click_on_Bike_Light="//div[contains(text(),'Sauce Labs Bike Light')]"
    click_on_Bolt_T_shirt="//div[contains(text(),'Sauce Labs Bolt T-Shirt')]"
    click_on_fleece_jacket="//div[contains(text(),'Sauce Labs Fleece Jacket')]"
    click_on_One_sie="//div[contains(text(),'Sauce Labs Onesie')]"

    Back_pack_price="(//div[contains(@data-test,'inventory-item-price')])[1]"
    Bike_light_price="(//div[contains(@data-test,'inventory-item-price')])[2]"
    Bolt_t_shirt_price="(//div[contains(@data-test,'inventory-item-price')])[3]"
    Fleece_jacket_price="(//div[contains(@data-test,'inventory-item-price')])[4]"
    One_sie_price="(//div[contains(@data-test,'inventory-item-price')])[5]"
    T_shirt_red_price="(//div[contains(@data-test,'inventory-item-price')])[6]"

    clicked_on_about="//a[contains(@id,'about_sidebar_link')]"
    clicked_on_sign_up_for_free="(//button[contains(@type,'button')])[8]"

    clicked_on_AI_Powered_Insights="//button[contains(text(),'AI-Powered Insights')]"
    clicked_on_Mobile_App_Testing="//button[contains(text(),'Mobile App Testing')]"
    clicked_on_Web_testing="//button[contains(text(),'Web Testing')]"
    clicked_on_Mobile_App_Distribution="//button[contains(text(),'Mobile App Distribution')]"
    clicked_on_Error_Reporting="//button[contains(text(),'Error Reporting')]"
    clicked_on_Visual_Testing="//button[contains(text(),'Visual Testing')]"


    clicked_on_Products="(//span[contains(text(),'Products')])[2]"

    clicked_on_platform_test_website="//span[contains(text(),'Platform for Test')]"
    clicked_on_sauce_web_testing_website="//span[contains(text(),'Sauce Web Testing')]"
    clicked_on_sauce_mobile_app_testing_website="//span[contains(text(),'Sauce Mobile App Testing')]"
    clicked_on_mobile_app_distribution_testing="(//span[contains(text(),'Mobile App Distribution')])[2]"
    clicked_on_sauce_error_reporting_website="//span[contains(text(),'Sauce Error Reporting')]"
    clicked_on_sauce_visual_website="//span[contains(text(),'Sauce Visual')]"

    move_to_home_website_sauce_labs="//span[contains(text(),'Home')]"

    clicked_on_global_tools="//span[contains(text(),'Global tools')]"

    clicked_on_sauce_performance="//span[contains(text(),'Sauce Performance')]"
    clicked_on_sauce_insights="//span[contains(text(),'Sauce Insights')]"

    clicked_on_set_up_and_integrate="//span[contains(text(),'Set up and integrate')]"

    clicked_on_integrations_and_plugins="//span[contains(text(),'Integrations & plugins')]"
    clicked_on_supported_browser_and_devices="//span[contains(text(),'Supported browsers and devices')]"
    clicked_on_platform_configurator="//span[contains(text(),'Platform configurator')]"

    clicked_on_resources="(//span[contains(text(),'Resources')])[2]"

    clicked_on_resources_by_topic="//span[contains(text(),'Resources by topic')]"
    clicked_on_blog="//span[contains(text(),'Blog')]"
    clicked_on_FAQ="//span[contains(text(),'FAQs')]"
    clicked_on_Documentation="//span[contains(text(),'Documentation')]"
    clicked_on_support="(//span[contains(text(),'Support')])[2]"
    clicked_on_events="//span[contains(text(),'Events')]"
    clicked_on_videos="//span[contains(text(),'Videos')]"
    clicked_on_webinars="//span[contains(text(),'Webinars')]"

    clicked_on_company="//span[contains(text(),'Company')]"

    clicked_on_about_us="//span[contains(text(),'About us')]"
    clicked_on_security="//span[contains(text(),'Security')]"
    clicked_on_partners="//span[contains(text(),'Partners')]"
    clicked_on_news="//span[contains(text(),'News')]"
    clicked_on_awards="//span[contains(text(),'Awards')]"
    clicked_on_contact="//span[contains(text(),'Contact us')]"
    clicked_on_system_status="//span[contains(text(),'Systems status')]"

    clicked_on_cart_selected="//div[contains(@id,'shopping_cart_container')]"
    continue_shopping="//button[contains(text(),'Continue Shopping')]"
    check_out="//button[contains(text(),'Checkout')]"
    first_name_input="//input[contains(@id,'first-name')]"
    last_name_input="//input[contains(@id,'last-name')]"
    postal_code_input="//input[contains(@id,'postal-code')]"
    continue_button_on_check_out="//input[contains(@id,'continue')]"

    finish_button="//button[contains(text(),'Finish')]"
    Cancel_button="//button[contains(text(),'Cancel')]"

    email_input = "//input[contains(@placeholder,'Username')]"
    password_input = "//input[contains(@placeholder,'Password')]"
    login_button = "//input[contains(@name,'login-button')]"





    @pytest.mark.run(order=27)
    def test_case_twenty_seven(self, driver):
        print("Moved to the Swag_labs_Module")
        time.sleep(2)
        driver.execute_script("alert('View the Sidebar in the UI')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        three_lines_on_side_bar = driver.find_element(By.XPATH, self.click_on_three_dots).click()
        time.sleep(2)
        print("Side-bar is Opened in the UI")
        time.sleep(3)
        screenshot_file = "Testcase_27.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=28)
    def test_case_twenty_eight(self, driver):
        print("Clicked on the All Items")
        time.sleep(2)
        driver.execute_script("alert('View the Sidebar in the UI')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        three_lines_on_side_bar = driver.find_element(By.XPATH, self.click_on_all_items).click()
        time.sleep(2)
        print("Clicked on the All Items in the UI")
        time.sleep(3)
        screenshot_file = "Testcase_28.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=29)
    def test_case_twenty_nine(self, driver):
        print("Clicked on the Closed Icon and closed the Sidebar")
        time.sleep(2)
        driver.execute_script("alert('Clicked on the Closed Icon by clicking the Close Button')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        three_lines_on_side_bar = driver.find_element(By.XPATH, self.close_btn_side_bar).click()
        time.sleep(2)
        print("Clicked on the Closed Icon by Clicking the Close Button")
        time.sleep(3)
        screenshot_file = "Testcase_28.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=30)
    def test_case_thirty(self, driver):
        print("Clicked on the Add to Cart of the Backpack")
        time.sleep(2)
        driver.execute_script("alert('Clicking the Add to Cart Button in the Backpack')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(5)
        clicked_the_cart_button_back_pack = driver.find_element(By.XPATH, self.sauce_labs_back_pack).click()
        time.sleep(2)
        print("Clicked on the Cart button of Back_pack")
        time.sleep(3)
        screenshot_file = "Testcase_30.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=31)
    def test_case_thirty_One(self, driver):
        print("Clicked on the Add to Cart of the Bike_light")
        time.sleep(2)
        driver.execute_script("alert('Clicking the Add to Cart Button in the Bike_Light')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        clicked_the_cart_button_bike_light = driver.find_element(By.XPATH, self.sauce_labs_bike_light).click()
        time.sleep(3)
        screenshot_file = "Testcase_31.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=32)
    def test_case_thirty_two(self, driver):
        print("Clicked on the Add to Cart of the Bolt_t_shirt")
        time.sleep(2)
        driver.execute_script("alert('Clicking the Add to Cart Button in the Bolt_t_shirt')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(10)
        clicked_the_cart_button_bolt_t_shirt = driver.find_element(By.XPATH, self.sauce_labs_bolt_t_shirt)
        time.sleep(3)
        driver.execute_script("arguments[0].scrollIntoView(true);", clicked_the_cart_button_bolt_t_shirt)
        time.sleep(2)
        clicked_the_cart_button_bolt_t_shirt.click()
        time.sleep(2)
        screenshot_file = "Testcase_32.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=33)
    def test_case_thirty_three(self, driver):
        print("Clicked on the Add to Cart of the Fleece_jacket")
        time.sleep(2)
        driver.execute_script("alert('Clicking the Add to Cart Button in the Fleece_Jacket')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(10)
        clicked_the_cart_button_fleece_jacket = driver.find_element(By.XPATH, self.sauce_labs_fleece_jacket)
        time.sleep(3)
        driver.execute_script("arguments[0].scrollIntoView(true);", clicked_the_cart_button_fleece_jacket)
        time.sleep(2)
        clicked_the_cart_button_fleece_jacket.click()
        time.sleep(2)
        screenshot_file = "Testcase_33.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=34)
    def test_case_thirty_four(self, driver):
        print("Clicked on the Add to Cart of the One_Sie")
        time.sleep(2)
        driver.execute_script("alert('Clicking the Add to Cart Button in the One_Sie')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        clicked_the_cart_button_onesie = driver.find_element(By.XPATH, self.sauce_labs_onesie).click()
        time.sleep(3)
        screenshot_file = "Testcase_34.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=35)
    def test_case_thirty_five(self, driver):
        print("Clicked on the Add to Cart of the Red_t_shirt")
        time.sleep(2)
        driver.execute_script("alert('Clicking the Add to Cart Button in the Red_t_Shirt')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(10)
        clicked_the_cart_button_red_t_shirt = driver.find_element(By.XPATH, self.sauce_labs_red_t_shirt).click()
        time.sleep(3)
        screenshot_file = "Testcase_35.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=36)
    def test_case_thirty_six(self, driver):
        print("Clicked on the Back-pack Product")
        time.sleep(2)
        driver.execute_script("alert('Clicking on the Back-pack Product')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        clicked_the_cart_button_back_pack = driver.find_element(By.XPATH, self.click_on_Back_pack).click()
        time.sleep(3)
        screenshot_file = "Testcase_36.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)
        clicked_on_the_back_button = driver.find_element(By.XPATH, self.click_on_back_to_products).click()
        time.sleep(2)
        print("Moving Back to Product Listing Module")
        time.sleep(2)

    @pytest.mark.run(order=37)
    def test_case_thirty_seven(self, driver):
        print("Clicked on the Bike_light Product")
        time.sleep(2)
        driver.execute_script("alert('Clicking on the Bike_light Product')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        clicked_the_cart_button_bike_light = driver.find_element(By.XPATH, self.click_on_Bike_Light).click()
        time.sleep(3)
        screenshot_file = "Testcase_37.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)
        clicked_on_the_back_button = driver.find_element(By.XPATH, self.click_on_back_to_products).click()
        time.sleep(2)
        print("Moving Back to Product Listing Module")
        time.sleep(2)

    @pytest.mark.run(order=38)
    def test_case_thirty_eight(self, driver):
        print("Clicked on the Bolt_t_shirt Product")
        time.sleep(2)
        driver.execute_script("alert('Clicking on the Bolt_t_shirt Product')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        clicked_the_cart_button_bolt_t_shirt = driver.find_element(By.XPATH, self.click_on_Bolt_T_shirt).click()
        time.sleep(3)
        screenshot_file = "Testcase_38.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)
        clicked_on_the_back_button = driver.find_element(By.XPATH, self.click_on_back_to_products).click()
        time.sleep(2)
        print("Moving Back to Product Listing Module")
        time.sleep(2)

    @pytest.mark.run(order=39)
    def test_case_thirty_nine(self, driver):
        print("Clicked on the fleece_jacket Product")
        time.sleep(2)
        driver.execute_script("alert('Clicking on the fleece_jacket Product')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        clicked_the_cart_button_fleece_jacket = driver.find_element(By.XPATH, self.click_on_fleece_jacket).click()
        time.sleep(3)
        screenshot_file = "Testcase_39.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)
        clicked_on_the_back_button = driver.find_element(By.XPATH, self.click_on_back_to_products).click()
        time.sleep(2)
        print("Moving Back to Product Listing Module")
        time.sleep(2)


    @pytest.mark.run(order=40)
    def test_case_forty(self, driver):
        print("Clicked on the One_sie Product")
        time.sleep(2)
        driver.execute_script("alert('Clicking on the One_sie Product')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        clicked_the_cart_button_One_sie = driver.find_element(By.XPATH, self.click_on_One_sie).click()
        time.sleep(3)
        screenshot_file = "Testcase_40.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)
        clicked_on_the_back_button = driver.find_element(By.XPATH, self.click_on_back_to_products).click()
        time.sleep(2)
        print("Moving Back to Product Listing Module")
        time.sleep(2)

    @pytest.mark.run(order=41)
    def test_case_forty_one(self, driver):
        print("Calculating the Total Items Cost Price")
        time.sleep(2)
        driver.execute_script("alert('Calculating the Total Items Cost Price')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        Back_pack_prices = driver.find_element(By.XPATH, self.Back_pack_price)
        back_pack = Back_pack_prices.text.replace("$", "")
        print(back_pack, "This is Back_pack_price")
        a = float(back_pack)
        time.sleep(2)
        Bike_light_prices = driver.find_element(By.XPATH, self.Bike_light_price)
        bike_light = Bike_light_prices.text.replace("$", "")
        print(bike_light, "This is Bike_Light_Price")
        b = float(bike_light)
        time.sleep(2)
        Bolt_t_shirt_prices = driver.find_element(By.XPATH, self.Bolt_t_shirt_price)
        bolt_t_shirt = Bolt_t_shirt_prices.text.replace("$", "")
        print(bolt_t_shirt, "This is Bolt_t_shirt_price")
        c = float(bolt_t_shirt)
        time.sleep(2)
        Fleece_jacket_prices = driver.find_element(By.XPATH, self.Fleece_jacket_price)
        fleece_jacket = Fleece_jacket_prices.text.replace("$", "")
        print(fleece_jacket, "This is Fleece_jacket_price")
        d = float(fleece_jacket)
        time.sleep(2)
        One_sie_prices = driver.find_element(By.XPATH, self.One_sie_price)
        one_sie = One_sie_prices.text.replace("$", "")
        print(one_sie, "This is One_sie_prices")
        e = float(one_sie)
        time.sleep(2)
        t_shirt_prices = driver.find_element(By.XPATH, self.T_shirt_red_price)
        t_shirt = t_shirt_prices.text.replace("$", "")
        print(t_shirt, "This is the T-shirt Price")
        time.sleep(3)
        f = float(t_shirt)
        time.sleep(3)
        sum = a + b + c + d + e + f
        print(sum, "This is the Total Value")
        driver.execute_script(f"alert('This is the Total Value: {sum}')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()

    @pytest.mark.run(order=42)
    def test_case_forty_two(self, driver):
        print(Fore.CYAN,"Clicking the Cart Icon")
        time.sleep(2)
        click_cart_icon=driver.find_element(By.XPATH,self.clicked_on_cart_selected).click()
        time.sleep(3)
        click_on_continue_shopping=driver.find_element(By.XPATH,self.continue_shopping).click()
        time.sleep(3)
        screenshot_file = "Testcase_42.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=43)
    def test_case_forty_three(self, driver):
        print(Fore.BLUE,"Again Clicking on the Cart Icon")
        time.sleep(2)
        click_cart_icon=driver.find_element(By.XPATH,self.clicked_on_cart_selected).click()
        time.sleep(2)
        click_on_check_out=driver.find_element(By.XPATH,self.check_out).click()
        time.sleep(3)
        driver.execute_script("alert('Now Moving to the Check-out Pages')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        screenshot_file = "Testcase_43.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=44)
    def test_case_forty_four(self, driver):
        print(Fore.MAGENTA,"Entering the Inputs for the Check-out")
        time.sleep(2)
        driver.execute_script("alert('Entering the Inputs for the Check-out --> First name input length less than 5 (Only small letters)')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        entering_the_first_name=driver.find_element(By.XPATH,self.first_name_input).send_keys("a")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button=driver.find_element(By.XPATH,self.continue_button_on_check_out).click()
        time.sleep(2)
        entering_the_first_name=driver.find_element(By.XPATH,self.first_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_the_first_name=driver.find_element(By.XPATH,self.first_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        screenshot_file = "Testcase_44.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=45)
    def test_case_forty_five(self, driver):
        print(Fore.BLUE,"First name input equal to length =5")
        time.sleep(2)
        driver.execute_script("alert('First name Input length equal to 5 (Small letters)')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys("demoq")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        screenshot_file = "Testcase_45.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)


    @pytest.mark.run(order=46)
    def test_case_forty_six(self, driver):
        print(Fore.BLUE, "First name input equal to length > 5")
        time.sleep(2)
        driver.execute_script("alert('First name Input length greater than 5 (Small letters)')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys("demoqufiurbfrfhrfhrfhurhfiu")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        screenshot_file = "Testcase_46.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=47)
    def test_case_forty_seven(self, driver):
        print(Fore.BLUE, "First name input equal to length < 5 (Capital letters)")
        time.sleep(2)
        driver.execute_script("alert('First name Input length less than 5 (Capital letters)')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(
            "DEMO")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        screenshot_file = "Testcase_47.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=48)
    def test_case_forty_eight(self, driver):
        print(Fore.BLUE, "First name input equal to length > 5 (Capital letters)")
        time.sleep(2)
        driver.execute_script("alert('First name Input length Greater than 5 (Capital letters)')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(
            "DEMOIUHFFRFRFJKNRFRFHIO")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        screenshot_file = "Testcase_48.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=49)
    def test_case_forty_nine(self, driver):
        print(Fore.BLUE, "First name input (Special Characters)")
        time.sleep(2)
        driver.execute_script("alert('First name Input length less than 5 (Special Characters)')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(
            "$%^&")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        screenshot_file = "Testcase_49.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=50)
    def test_case_fifty(self, driver):
        print(Fore.BLUE, "First name input (Special Characters)")
        time.sleep(2)
        driver.execute_script("alert('First name Input length Greater than 5 (Special Characters)')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(
            "$%^&#$%^^&*^&*")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        screenshot_file = "Testcase_50.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=51)
    def test_case_fifty_one(self, driver):
        print(Fore.BLUE, "First name input (Small & Capital letters)")
        time.sleep(2)
        driver.execute_script("alert('First name Input Combination of (Small & Capital letters) each 1')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(
            "aS")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        screenshot_file = "Testcase_51.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=52)
    def test_case_fifty_two(self, driver):
        print(Fore.BLUE, "First name input (Small & Capital letters)")
        time.sleep(2)
        driver.execute_script("alert('First name Input Combination of (Small & Capital letters) length less than 5')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(
            "aSdF")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        screenshot_file = "Testcase_52.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=53)
    def test_case_fifty_three(self, driver):
        print(Fore.BLUE, "First name input (Small & Capital letters)")
        time.sleep(2)
        driver.execute_script("alert('First name Input Combination of (Small & Capital letters) length Greater than 5')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(
            "aSdFjhfhrifirfjrjriofTFTED")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        screenshot_file = "Testcase_53.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)


    @pytest.mark.run(order=54)
    def test_case_fifty_four(self, driver):
        print(Fore.BLUE, "First name input (Small & Capital letters & Special Characters)")
        time.sleep(2)
        driver.execute_script(
            "alert('First name Input Combination of (Small & Capital letters & Special Characters) length less than 5')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(
            "aSd&")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)

    @pytest.mark.run(order=55)
    def test_case_fifty_five(self, driver):
        print(Fore.BLUE, "First name input (Small & Capital letters & Special Characters)")
        time.sleep(2)
        driver.execute_script(
            "alert('First name Input Combination of (Small & Capital letters & Special Characters) length Greater than 5')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(
            "aSd&hbfhruHEHBD#$%^&*(")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(3)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_the_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)

    @pytest.mark.run(order=56)
    def test_case_fifty_six(self, driver):
        print(Fore.BLUE, "Moving to the last-name Input less than 2")
        time.sleep(2)
        entering_the_first_name=driver.find_element(By.XPATH,self.first_name_input).send_keys("Demo-user")
        time.sleep(2)
        driver.execute_script(
            "alert('Last name Input of Giving the Small Characters length less than 2')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_last_name=driver.find_element(By.XPATH,self.last_name_input).send_keys("r")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(2)
        entering_last_name=driver.find_element(By.XPATH,self.last_name_input).send_keys(Keys.CONTROL +"a")
        time.sleep(2)
        entering_last_name=driver.find_element(By.XPATH,self.last_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)

    @pytest.mark.run(order=57)
    def test_case_fifty_seven(self, driver):
        print(Fore.BLUE, "Moving to the last-name Input less than 10")
        time.sleep(5)
        driver.execute_script(
            "alert('Last name Input of Giving the Small Characters length less than 10')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys("rijie")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(3)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)

    @pytest.mark.run(order=58)
    def test_case_fifty_eight(self, driver):
        print(Fore.BLUE, "Moving to the last-name Input less than 5")
        time.sleep(5)
        driver.execute_script(
            "alert('Last name Input of Giving the Capital Characters length less than 5')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys("HSHS")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(3)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)

    @pytest.mark.run(order=59)
    def test_case_fifty_nine(self, driver):
        print(Fore.BLUE, "Moving to the last-name Input Greater than 5")
        time.sleep(5)
        driver.execute_script(
            "alert('Last name Input of Giving the Capital Characters length Greater than 5')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys("HSHSKJRNFJRFN")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(2)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)

    @pytest.mark.run(order=60)
    def test_case_sixty(self, driver):
        print(Fore.BLUE, "Moving to the last-name Input Special Characters")
        time.sleep(5)
        driver.execute_script(
            "alert('Last name Input of Giving the Special Characters length less than 5')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys("#$%^")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(2)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)

    @pytest.mark.run(order=61)
    def test_case_sixty_one(self, driver):
        print(Fore.BLUE, "Moving to the last-name Input Special Characters")
        time.sleep(5)
        driver.execute_script(
            "alert('Last name Input of Giving the Special Characters length Greater than 5')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys("#$%^$%^&*(")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(3)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)

    @pytest.mark.run(order=62)
    def test_case_sixty_two(self, driver):
        print(Fore.BLUE, "Moving to the last-name Input Special & Small Characters")
        time.sleep(5)
        driver.execute_script(
            "alert('Last name Input of Giving the Special & Small  Characters length less than 10')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys("#$%uhdiudh")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(2)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)

    @pytest.mark.run(order=63)
    def test_case_sixty_three(self, driver):
        print(Fore.BLUE, "Moving to the last-name Input Special & Small Characters")
        time.sleep(5)
        driver.execute_script(
            "alert('Last name Input of Giving the Special & Small  Characters length Greater than 10')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys("#$%uhd$%^ud#@#iudh")
        time.sleep(2)
        driver.execute_script("alert('Checking moving to next page or Not By clicking the Continue Button')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(3)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys(Keys.BACKSPACE)
        time.sleep(2)

    @pytest.mark.run(order=64)
    def test_case_sixty_four(self, driver):
        print(Fore.BLUE, "Moving to the Input of the Postal-code")
        time.sleep(5)
        entering_the_last_name=driver.find_element(By.XPATH,self.last_name_input).send_keys("Users")
        time.sleep(2)
        driver.execute_script(
            "alert('Giving the Characters (Alphabets) as a Input in the Postal-code')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        entering_the_values_on_postal_code=driver.find_element(By.XPATH,self.postal_code_input).send_keys("a")
        time.sleep(2)

    @pytest.mark.run(order=65)
    def test_case_sixty_five(self, driver):
        time.sleep(2)
        driver.execute_script(
            "alert('There is No Validation for the Postal Code.')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)

    @pytest.mark.run(order=66)
    def test_case_sixty_six(self, driver):
        print(Fore.MAGENTA,"In the Total Page (Items and Its prices")
        time.sleep(2)
        click_on_cancel_button=driver.find_element(By.XPATH,self.Cancel_button).click()
        time.sleep(2)
        driver.execute_script(
            "alert('Cancel button is get Clicked......')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(5)
        driver.execute_script(
            "alert('It get moved to the Login page... Expected Behaviour..')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(4)
        entering_the_user_name=driver.find_element(By.XPATH,self.email_input).send_keys("error_user")
        time.sleep(3)
        entering_the_password=driver.find_element(By.XPATH,self.password_input).send_keys("secret_sauce")
        time.sleep(4)
        click_on_login_button=driver.find_element(By.XPATH,self.login_button).click()
        time.sleep(3)

    @pytest.mark.run(order=67)
    def test_case_sixty_seven(self, driver):
        print(Fore.GREEN,"Again clicking on the cart Button")
        time.sleep(2)
        clicking_on_the_cart_selected=driver.find_element(By.XPATH,self.clicked_on_cart_selected).click()
        time.sleep(3)
        print(Fore.BLACK,"Clicking on Check-out this Item")
        time.sleep(3)
        click_on_check_out=driver.find_element(By.XPATH,self.check_out).click()
        time.sleep(3)
        driver.execute_script(
            "alert('In the Check-out page --> Filling the details')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)

    @pytest.mark.run(order=68)
    def test_case_sixty_eight(self, driver):
        print(Fore.CYAN,"Filling the Inputs of the First & Last name")
        time.sleep(3)
        entering_first_name=driver.find_element(By.XPATH,self.first_name_input).send_keys("DEMO_USER")
        time.sleep(3)
        entering_last_name=driver.find_element(By.XPATH,self.last_name_input).send_keys("hded")
        time.sleep(3)
        entering_postal_code=driver.find_element(By.XPATH,self.postal_code_input).send_keys("12345")
        time.sleep(3)
        click_on_continue_button=driver.find_element(By.XPATH,self.continue_button_on_check_out).click()
        time.sleep(3)
        print(Fore.LIGHTMAGENTA_EX,"Now Clicking on the Cancel Button")
        time.sleep(3)
        driver.execute_script(
            "alert('Clicking the Cancel Button..')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(4)
        click_on_cancel_button=driver.find_element(By.XPATH,self.Cancel_button).click()
        time.sleep(3)

    @pytest.mark.run(order=69)
    def test_case_sixty_nine(self, driver):
        print(Fore.LIGHTYELLOW_EX,"Again Clicking on the Cart Container...")
        time.sleep(4)
        driver.execute_script(
            "alert('Clicking on the Cart Container...')")
        time.sleep(2)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        click_on_check_out=driver.find_element(By.XPATH,self.check_out).click()
        time.sleep(3)

    @pytest.mark.run(order=70)
    def test_case_sixty_nine(self, driver):
        time.sleep(4)
        entering_first_name = driver.find_element(By.XPATH, self.first_name_input).send_keys("DEMO_USER")
        time.sleep(3)
        entering_last_name = driver.find_element(By.XPATH, self.last_name_input).send_keys("hded")
        time.sleep(3)
        entering_postal_code = driver.find_element(By.XPATH, self.postal_code_input).send_keys("12345")
        time.sleep(3)
        click_on_continue_button = driver.find_element(By.XPATH, self.continue_button_on_check_out).click()
        time.sleep(3)
        print(Fore.BLACK,"Clicked the Continue Button")













































































    # @pytest.mark.run(order=42)
    # def test_case_forty_two(self, driver):
    #     print("Adding the Values")
    #     clicked_on_three_lines=driver.find_element(By.XPATH,self.click_on_three_dots).click()
    #     time.sleep(2)
    #     clicked_on_about=driver.find_element(By.XPATH,self.click_on_about).click()
    #     time.sleep(3)
    #
    # @pytest.mark.run(order=43)
    # def test_case_forty_three(self, driver):
    #     print(Fore.MAGENTA,"clicked on Web Testing")
    #     time.sleep(2)
    #     driver.execute_script("alert('Clicked on the web Testing')")
    #     time.sleep(3)
    #     alert = driver.switch_to.alert
    #     time.sleep(2)
    #     alert.accept()
    #     time.sleep(3)
    #     clicked_on_web_testing=driver.find_element(By.XPATH,self.clicked_on_Web_testing)
    #     time.sleep(2)
    #
    # @pytest.mark.run(order=44)
    # def test_case_forty_four(self, driver):
    #     print(Fore.MAGENTA, "clicked on AI Powered Insights")
    #     time.sleep(2)
    #     driver.execute_script("alert('Clicked on the AI Powered Insights')")
    #     time.sleep(3)
    #     alert = driver.switch_to.alert
    #     time.sleep(2)
    #     alert.accept()
    #     time.sleep(3)
    #     clicked_on_AI_Powered_Insights=driver.find_element(By.XPATH,self.clicked_on_AI_Powered_Insights).click()
    #     time.sleep(2)
    #
    # @pytest.mark.run(order=45)
    # def test_case_forty_five(self, driver):
    #     print(Fore.MAGENTA, "clicked on Mobile App Testing")
    #     time.sleep(2)
    #     driver.execute_script("alert('Clicked on the Mobile App Testing')")
    #     time.sleep(3)
    #     alert = driver.switch_to.alert
    #     time.sleep(2)
    #     alert.accept()
    #     time.sleep(3)
    #     clicked_on_Mobile_App_Testing=driver.find_element(By.XPATH,self.clicked_on_Mobile_App_Testing).click()
    #     time.sleep(2)
    #
    # @pytest.mark.run(order=46)
    # def test_case_forty_six(self, driver):
    #     print(Fore.MAGENTA, "clicked on Mobile App Distribution")
    #     time.sleep(2)
    #     driver.execute_script("alert('Clicked on the Mobile App Distribution')")
    #     time.sleep(3)
    #     alert = driver.switch_to.alert
    #     time.sleep(2)
    #     alert.accept()
    #     time.sleep(3)
    #     clicked_on_Mobile_App_Distribution=driver.find_element(By.XPATH,self.clicked_on_Mobile_App_Distribution).click()
    #     time.sleep(2)
    #
    # @pytest.mark.run(order=47)
    # def test_case_forty_seven(self, driver):
    #     print(Fore.BLUE,"")


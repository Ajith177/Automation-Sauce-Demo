import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from colorama import Fore
from Login_Module.test_login_helper import LoginHelper
import shutil
import os
import pytest
from urllib3.poolmanager import key_fn_by_scheme
from Login_Module.test_login_helper import LoginHelper


class Test_Swag:
    target_folder = r'C:\Users\AJITH\PycharmProjects\PythonProject\Sauce-demo\Screenshots\Swag_lab'
    click_on_three_dots="//button[contains(@id,'react-burger-menu-btn')]"
    click_on_all_items="//a[contains(text(),'All Items')]"
    click_on_about="//a[contains(text(),'About')]"
    click_on_Log_out="//a[contains(text(),'Logout')]"
    click_on_reset_app_state="//a[contains(text(),'Reset')]"
    close_btn_side_bar="//button[contains(@id,'react-burger-cross-btn')]"

    # sauce_labs_back_pack="(//button[contains(text(),'Add to cart')])[1]"
    # sauce_labs_bike_light="(//button[contains(text(),'Add to cart')])[2]"
    # sauce_labs_bolt_t_shirt="(//button[contains(text(),'Add to cart')])[3]"
    # sauce_labs_fleece_jacket="(//button[contains(text(),'Add to cart')])[4]"
    # sauce_labs_onesie="(//button[contains(text(),'Add to cart')])[5]"
    # sauce_labs_red_t_shirt="(//button[contains(text(),'Add to cart')])[6]"

    sauce_labs_back_pack = "//button[contains(@id,'add-to-cart-sauce-labs-backpack')]"
    sauce_labs_bike_light = "//button[contains(@id,'add-to-cart-sauce-labs-bike-light')]"
    sauce_labs_bolt_t_shirt = "//button[contains(@id,'add-to-cart-sauce-labs-bolt-t-shirt')]"
    sauce_labs_fleece_jacket = "//button[contains(@id,'add-to-cart-sauce-labs-fleece-jacket')]"
    sauce_labs_onesie = "//button[contains(@id,'add-to-cart-sauce-labs-onesie')]"
    sauce_labs_red_t_shirt = "add-to-cart-test.allthethings()-t-shirt-(red)"

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
        driver.execute_script("alert('Clicked the Add to Cart Button in the Backpack')")
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
        driver.execute_script("alert('Clicked the Add to Cart Button in the Bike_Light')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        clicked_the_cart_button_back_pack = driver.find_element(By.XPATH, self.sauce_labs_bike_light).click()
        time.sleep(3)
        screenshot_file = "Testcase_30.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=32)
    def test_case_thirty_two(self, driver):
        print("Clicked on the Add to Cart of the Bolt_t_shirt")
        time.sleep(2)
        driver.execute_script("alert('Clicked the Add to Cart Button in the Bolt_t_shirt')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(10)
        clicked_the_cart_button_back_pack = driver.find_element(By.XPATH, self.sauce_labs_bolt_t_shirt).click()
        time.sleep(3)
        screenshot_file = "Testcase_32.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=33)
    def test_case_thirty_three(self, driver):
        print("Clicked on the Add to Cart of the Fleece_jacket")
        time.sleep(2)
        driver.execute_script("alert('Clicked the Add to Cart Button in the Fleece_Jacket')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(10)
        clicked_the_cart_button_back_pack = driver.find_element(By.XPATH, self.sauce_labs_fleece_jacket).click()
        time.sleep(3)
        screenshot_file = "Testcase_33.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=34)
    def test_case_thirty_four(self, driver):
        print("Clicked on the Add to Cart of the One_Sie")
        time.sleep(2)
        driver.execute_script("alert('Clicked the Add to Cart Button in the One_Sie')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        clicked_the_cart_button_back_pack = driver.find_element(By.XPATH, self.sauce_labs_onesie).click()
        time.sleep(3)
        screenshot_file = "Testcase_34.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=35)
    def test_case_thirty_five(self, driver):
        print("Clicked on the Add to Cart of the Red_t_shirt")
        time.sleep(2)
        driver.execute_script("alert('Clicked the Add to Cart Button in the Red_t_Shirt')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(10)
        clicked_the_cart_button_back_pack = driver.find_element(By.XPATH, self.sauce_labs_red_t_shirt).click()
        time.sleep(3)
        screenshot_file = "Testcase_35.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)

    @pytest.mark.run(order=36)
    def test_case_thirty_six(self, driver):
        print("Clicked on the Back-pack Product")
        time.sleep(2)
        driver.execute_script("alert('Clicked on the Back-pack Product')")
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
        driver.execute_script("alert('Clicked on the Bike_light Product')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        clicked_the_cart_button_back_pack = driver.find_element(By.XPATH, self.click_on_Bike_Light).click()
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
        driver.execute_script("alert('Clicked on the Bolt_t_shirt Product')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        clicked_the_cart_button_back_pack = driver.find_element(By.XPATH, self.click_on_Bolt_T_shirt).click()
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
        driver.execute_script("alert('Clicked on the fleece_jacket Product')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        clicked_the_cart_button_back_pack = driver.find_element(By.XPATH, self.click_on_fleece_jacket).click()
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
        print("Clicked on the fleece_jacket Product")
        time.sleep(2)
        driver.execute_script("alert('Clicked on the fleece_jacket Product')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        clicked_the_cart_button_back_pack = driver.find_element(By.XPATH, self.click_on_fleece_jacket).click()
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
        print("Clicked on the One_sie Product")
        time.sleep(2)
        driver.execute_script("alert('Clicked on the One_sie Product')")
        time.sleep(3)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        clicked_the_cart_button_back_pack = driver.find_element(By.XPATH, self.click_on_One_sie).click()
        time.sleep(3)
        screenshot_file = "Testcase_41.png"
        driver.save_screenshot(screenshot_file)
        shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
        time.sleep(2)
        clicked_on_the_back_button = driver.find_element(By.XPATH, self.click_on_back_to_products).click()
        time.sleep(2)
        print("Moving Back to Product Listing Module")
        time.sleep(2)

    @pytest.mark.run(order=42)
    def test_case_forty_two(self, driver):
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

    @pytest.mark.run(order=43)
    def test_case_forty_three(self, driver):
        print("Adding the Values")
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
    target_folder = r'C:\Users\ZCSU040\Pictures\Sauce\Sauce_Automation\Screenshots\Swag_Labs'
    click_on_three_dots="//button[contains(@id,'react-burger-menu-btn')]"
    click_on_all_items="//a[contains(text(),'All Items')]"
    click_on_about="//a[contains(text(),'About')]"
    click_on_Log_out="//a[contains(text(),'Logout')]"
    click_on_reset_app_state="//a[contains(text(),'Reset')]"
    close_btn_side_bar="//button[contains(@id,'react-burger-cross-btn')]"

    sauce_labs_back_pack="(//button[contains(text(),'Add to cart')])[1]"
    sauce_labs_bike_light="(//button[contains(text(),'Add to cart')])[2]"
    sauce_labs_bolt_t_shirt="(//button[contains(text(),'Add to cart')])[3]"
    sauce_labs_fleece_jacket="(//button[contains(text(),'Add to cart')])[4]"
    sauce_labs_onesie="(//button[contains(text(),'Add to cart')])[5]"
    sauce_labs_red_t_shirt="(//button[contains(text(),'Add to cart')])[6]"

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
        login_helper = LoginHelper(driver)
        login_helper.ensure_logged_in()
        time.sleep(2)
        driver.refresh()
        login_helper.ensure_logged_in()
        try:
            driver.execute_script("alert('View the Sidebar in the UI')")
            time.sleep(3)
            alert = driver.switch_to.alert
            time.sleep(2)
            alert.accept()
            time.sleep(2)
            three_lines_on_side_bar=driver.find_element(By.XPATH,self.click_on_three_dots).click()
            time.sleep(2)
            print("Side-bar is Opened in the UI")
            time.sleep(3)
            screenshot_file = "Testcase_27.png"
            driver.save_screenshot(screenshot_file)
            shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
            time.sleep(2)

        except Exception as e:
            print(f"Exception occurred: {e}")
            login_helper.ensure_logged_in()

    @pytest.mark.run(order=28)
    def test_case_twenty_eight(self, driver):
        print("Clicked on the All Items")
        login_helper = LoginHelper(driver)
        login_helper.ensure_logged_in()
        time.sleep(2)
        driver.refresh()
        login_helper.ensure_logged_in()
        try:
            driver.execute_script("alert('View the Sidebar in the UI')")
            time.sleep(3)
            alert = driver.switch_to.alert
            time.sleep(2)
            alert.accept()
            time.sleep(2)
            three_lines_on_side_bar=driver.find_element(By.XPATH,self.click_on_all_items).click()
            time.sleep(2)
            print("Clicked on the All Items in the UI")
            time.sleep(3)
            screenshot_file = "Testcase_28.png"
            driver.save_screenshot(screenshot_file)
            shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
            time.sleep(2)

        except Exception as e:
            print(f"Exception occurred: {e}")
            login_helper.ensure_logged_in()

    @pytest.mark.run(order=29)
    def test_case_twenty_nine(self, driver):
        print("Clicked on the Closed Icon and closed the Sidebar")
        login_helper = LoginHelper(driver)
        login_helper.ensure_logged_in()
        time.sleep(2)
        driver.refresh()
        login_helper.ensure_logged_in()
        try:
            driver.execute_script("alert('Clicked on the Closed Icon by clicking the Close Button')")
            time.sleep(3)
            alert = driver.switch_to.alert
            time.sleep(2)
            alert.accept()
            time.sleep(2)
            three_lines_on_side_bar = driver.find_element(By.XPATH, self.click_on_all_items).click()
            time.sleep(2)
            print("Clicked on the Closed Icon by Clicking the Close Button")
            time.sleep(3)
            screenshot_file = "Testcase_28.png"
            driver.save_screenshot(screenshot_file)
            shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
            time.sleep(2)
        except Exception as e:
            print(f"Exception occurred: {e}")
            login_helper.ensure_logged_in()

    @pytest.mark.run(order=30)
    def test_case_thirty(self, driver):
        print("Clicked on the Add to Cart of the Backpack")
        time.sleep(2)
        login_helper = LoginHelper(driver)
        login_helper.ensure_logged_in()
        time.sleep(2)
        driver.refresh()
        login_helper.ensure_logged_in()
        try:
            driver.execute_script("alert('Clicked the Add to Cart Button in the Backpack')")
            time.sleep(3)
            alert = driver.switch_to.alert
            time.sleep(2)
            alert.accept()
            time.sleep(2)
            clicked_the_cart_button_back_pack=driver.find_element(By.XPATH,self.sauce_labs_back_pack).click()
            time.sleep(2)
            print("Clicked on the Cart button of Back_pack")
            time.sleep(3)
            screenshot_file = "Testcase_30.png"
            driver.save_screenshot(screenshot_file)
            shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
            time.sleep(2)
        except Exception as e:
            print(f"Exception occurred: {e}")
            login_helper.ensure_logged_in()

    @pytest.mark.run(order=31)
    def test_case_thirty(self, driver):
        print("Clicked on the Add to Cart of the Bike_light")
        time.sleep(2)
        login_helper = LoginHelper(driver)
        login_helper.ensure_logged_in()
        time.sleep(2)
        driver.refresh()
        login_helper.ensure_logged_in()
        try:
            driver.execute_script("alert('Clicked the Add to Cart Button in the BackLight')")
            time.sleep(3)
            alert = driver.switch_to.alert
            time.sleep(2)
            alert.accept()
            time.sleep(2)
            clicked_the_cart_button_back_pack = driver.find_element(By.XPATH, self.sauce_labs_back_pack).click()
            time.sleep(3)
            screenshot_file = "Testcase_30.png"
            driver.save_screenshot(screenshot_file)
            shutil.move(screenshot_file, os.path.join(self.target_folder, os.path.basename(screenshot_file)))
            time.sleep(2)
        except Exception as e:
            print(f"Exception occurred: {e}")
            login_helper.ensure_logged_in()
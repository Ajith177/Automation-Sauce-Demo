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
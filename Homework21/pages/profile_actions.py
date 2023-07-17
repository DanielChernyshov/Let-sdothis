import string
import time
import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def random_char(char_num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))

class ProfileActions:
    def __init__(self, driver):
        self.driver = driver

    def profile_create(self,driver):
        driver.find_element(By.XPATH, "//button[@class='btn btn-outline-white header_signin']").click()
        driver.find_element(By.XPATH,
                            "//div[@class='modal-footer d-flex justify-content-between']//button[@class='btn btn-link']").click()
        driver.find_element(By.ID, "signupName").send_keys("Vasyl")
        driver.find_element(By.ID, "signupLastName").send_keys("Holoborodko")
        driver.find_element(By.ID, "signupEmail").send_keys(random_char(7) + "@gmail.com")
        driver.find_element(By.ID, "signupPassword").send_keys("Iamgod2009")
        driver.find_element(By.ID, "signupRepeatPassword").send_keys("Iamgod2009")
        driver.find_element(By.XPATH, "//div[@class='modal-footer']//button").click()

    def profile_name_check(self, driver):
        driver.find_element(By.XPATH, "//a[@routerlink='profile']").click()
        time.sleep(3)
        profile_name = driver.find_element(By.XPATH, "//p[@class='profile_name display-4']")
        assert profile_name.text == "Vasyl Holoborodko"

    def create_car(self, driver):
        driver.find_element(By.XPATH,"//div[@class='panel-page']//button").click()
        time.sleep(3)
        driver.find_element(By.ID, "addCarMileage").send_keys(1)
        driver.find_element(By.XPATH,"//div[@class='modal-content']//button[@class='btn btn-primary']").click()

    def add_expense(self, driver):
         driver.find_element(By.XPATH,"//button[@class='car_add-expense btn btn-success']").click()
         new_mileage = driver.find_element(By.ID, "addExpenseMileage")
         new_mileage.clear()
         new_mileage.send_keys(15)
         time.sleep(3)
         driver.find_element(By.ID, "addExpenseLiters").send_keys(random.randrange(2, 20))
         driver.find_element(By.ID, "addExpenseTotalCost").send_keys(random.randrange(2, 20))
         driver.find_element(By.XPATH, "//div[@class='modal-content']//button[@class='btn btn-primary']").click()
         time.sleep(3)

    def delete_profile(self, driver):
        driver.find_element(By.XPATH, "//a[@routerlink='settings']").click()
        driver.find_element(By.XPATH, "//button[@class='btn btn-danger-bg']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()

    def guest_log_in(self,driver):
        driver.find_element(By.XPATH, "//button[@class='header-link -guest']").click()
        header_guest = driver.find_element(By.XPATH, "//p[@class='header_bar']")
        assert header_guest.text == "Logged in as guest, any changes will be lost!"

    def go_to_garage(self,driver):
        driver.find_element(By.XPATH, "//div[@class='app-content']//a[@href='/panel/garage']").click()

    def check_max_cap(self,driver):
        driver.find_element(By.XPATH,"//div[@class='panel-page']//button").click()
        driver.find_element(By.ID, "addCarMileage").send_keys(1)
        driver.find_element(By.XPATH, "//div[@class='modal-content']//button[@class='btn btn-primary']").click()
        time.sleep(3)
        max_cap_message = driver.find_element(By.XPATH, "//p[@class='alert alert-danger']")
        assert max_cap_message.text == "Cars number limit exceeded. You can create maximum 5 cars in guest mode."
        print("Maximum 5 cars!")






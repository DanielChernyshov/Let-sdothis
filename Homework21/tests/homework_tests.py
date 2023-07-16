import random
import string
import time
import pytest
from selenium import webdriver
from pages.home_page import Homepage
from pages.profile_actions import ProfileActions


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    return browser


def random_char(char_num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))


def test_number_1(browser):
    home_page = Homepage(browser)
    home_page.open()
    profile_action = ProfileActions(browser)
    profile_action.profile_create(browser)
    time.sleep(3)
    profile_action.profile_name_check(browser)
    profile_action.go_to_garage(browser)
    profile_action.create_car(browser)
    time.sleep(3)
    profile_action.add_expense(browser)
    profile_action.delete_profile(browser)



def test_number_2(browser):
    home_page = Homepage(browser)
    home_page.open()
    profile_action = ProfileActions(browser)
    profile_action.guest_log_in(browser)
    for _ in range(5):
        profile_action.create_car(browser)
        time.sleep(1)
    profile_action.check_max_cap(browser)
    time.sleep(3)


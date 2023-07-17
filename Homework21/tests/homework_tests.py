import pytest
from selenium import webdriver
from pages.home_page import Homepage
from pages.profile_actions import ProfileActions


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    return browser


def test1_profile_creation(browser):
    home_page = Homepage(browser)
    home_page.open()
    profile_action = ProfileActions(browser)
    profile_action.create_profile(browser, "Vasyl", "Holobordko")
    profile_action.assert_profile_name(browser, "Vasyl Holobordko")
    profile_action.go_to_garage(browser)
    profile_action.create_cars(browser, 1, 1)
    profile_action.add_expense(browser, 15, 13, 17)
    profile_action.delete_profile(browser)


def test2_guest_check_max_cap(browser):
    home_page = Homepage(browser)
    home_page.open()
    profile_action = ProfileActions(browser)
    profile_action.log_in_guest(browser)
    profile_action.create_cars(browser, 5, 2)
    profile_action.check_max_cap_guest(browser, 3)

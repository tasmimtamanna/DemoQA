import faker
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from faker import Faker


@pytest.fixture()

def browser_config():
    global driver

    global fake

    fake = Faker()

    driver = webdriver.Firefox()

    driver.get('https://demoqa.com/')
    time.sleep(5)

    elements = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
    driver.execute_script("arguments[0].scrollIntoView();", elements)
    elements.click()
    time.sleep(5)

    textbox = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']//div[@class='accordion']/div[1]/div/ul[@class='menu-list']/li[1]")
    textbox.click()
    time.sleep(5)


def test_browser_config():
    print("Browser Launch Sucessfully")


def Full_name():
    full_name = driver.find_element(By.XPATH, "/html//input[@id='userName']")
    full_name.clear()
    full_name.send_keys("Tasmim")


def Email():
    email_field = driver.find_element(By.XPATH, "/html//input[@id='userEmail']")
    driver.execute_script("arguments[0].scrollIntoView();", email_field)
    email_field.clear()
    email_field.send_keys(fake.email())
    time.sleep(3)


def Current_address():
    current_address = driver.find_element(By.XPATH, "/html//textarea[@id='currentAddress']")
    driver.execute_script("arguments[0].scrollIntoView();", current_address)
    current_address.clear()
    current_address.send_keys("This is test")
    time.sleep(5)


def Permanent_adress():
    permanent_address = driver.find_element(By.XPATH, "/html//textarea[@id='permanentAddress']")
    driver.execute_script("arguments[0].scrollIntoView();", permanent_address)
    permanent_address.clear()
    permanent_address.send_keys("j")
    time.sleep(5)


def Submit():
    submit_button = driver.find_element(By.XPATH, "/html//button[@id='submit']")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    submit_button.click()
    time.sleep(3)


def test_Full_name(browser_config):
    Full_name()


def test_Email(browser_config):
    Email()


def test_Current_address(browser_config):
    Current_address()


def test_Permanent_address(browser_config):
    Permanent_adress()


def test_Submit(browser_config):
    Submit()


def test_textbook(browser_config):
    Full_name()
    Email()
    Current_address()
    Permanent_adress()
    Submit()

import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser_config():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/')
    driver.maximize_window()
    time.sleep(3)

    elements = driver.find_element(By.XPATH,  '//*[@id="app"]/div/div/div[2]/div/div[1]')
    driver.execute_script("arguments[0].scrollIntoView();", elements)
    elements.click()
    time.sleep(3)

    checkbox = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']//"
                                             "div[@class='accordion']/div[1]/div/ul[@class='menu-list']/li[2]")
    checkbox.click()
    time.sleep(3)


def test_browser(browser_config):
    print("Browser Launch")


def home():
    home_checkbox = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol/li"
                                                  "//span[@class='rct-checkbox']")
    driver.execute_script("arguments[0].scrollIntoView();", home_checkbox)
    home_checkbox.click()
    time.sleep(3)


def test_home(browser_config):
    home()


def test_arrow_button(browser_config):
    arrow = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol//button[@title='Toggle']")
    driver.execute_script("arguments[0].scrollIntoView();", arrow)
    arrow.click()
    time.sleep(3)



def test_expand_arrow1(browser_config):
    arrow = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol//button[@title='Toggle']")
    driver.execute_script("arguments[0].scrollIntoView();", arrow)
    arrow.click()
    time.sleep(3)

    arrow1 = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol/li/ol/li[1]/span[@class='rct-text']"
                                           "/button[@title='Toggle']")
    driver.execute_script("arguments[0].scrollIntoView();", arrow1)
    arrow1.click()
    time.sleep(3)


def test_expand_arrow2(browser_config):
    arrow = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol//button[@title='Toggle']")
    driver.execute_script("arguments[0].scrollIntoView();", arrow)
    arrow.click()
    time.sleep(3)

    arrow2 = driver.find_element(By.XPATH, "//div[@id='tree-node']"
                                           "/ol/li/ol/li[2]/span[@class='rct-text']/button[@title='Toggle']")
    driver.execute_script("arguments[0].scrollIntoView();", arrow2)
    arrow2.click()
    time.sleep(3)


def test_expand_arrow3(browser_config):
    arrow = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol//button[@title='Toggle']")
    driver.execute_script("arguments[0].scrollIntoView();", arrow)
    arrow.click()
    time.sleep(3)

    arrow3 = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol/li/ol"
                                           "/li[3]/span[@class='rct-text']/button[@title='Toggle']")
    driver.execute_script("arguments[0].scrollIntoView();", arrow3)
    arrow3.click()
    time.sleep(3)


def test_desktop_checkbox(browser_config):
    arrow = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol//button[@title='Toggle']")
    driver.execute_script("arguments[0].scrollIntoView();", arrow)
    arrow.click()
    time.sleep(3)

    arrow1 = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol/li/ol/li[1]/span[@class='rct-text']"
                                           "/button[@title='Toggle']")
    driver.execute_script("arguments[0].scrollIntoView();", arrow1)
    arrow1.click()
    time.sleep(3)

    desktop = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol/li/ol/"
                                            "li[1]/span[@class='rct-text']/label/span[@class='rct-checkbox']")
    desktop.click()
    time.sleep(3)
    desktop.click()
    time.sleep(3)

    notes = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol/li/ol/li[1]/ol/li"
                                          "[1]/span[@class='rct-text']/label/span[@class='rct-checkbox']")
    notes.click()
    time.sleep(3)
    notes.click()
    time.sleep(3)

    command = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol/li/ol/li[1]/ol/li"
                                            "[2]/span[@class='rct-text']/label/span[@class='rct-checkbox']")
    command.click()
    time.sleep(3)
    command.click()
    time.sleep(3)


def test_document(browser_config):
    test_arrow_button(browser_config)
    document_checkbox = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol/li/ol/li[2]/"
                                                      "span[@class='rct-text']/label/span[@class='rct-checkbox']")
    document_checkbox.click()
    time.sleep(3)
    document_checkbox.click()

    expand_document = driver.find_element(By.XPATH,"//div[@id='tree-node']/ol/li/ol/li"
                                                   "[2]/span[@class='rct-text']/button[@title='Toggle']")
    expand_document.click()
    time.sleep(3)

    workspace_checkbox = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/"
                                                       "span[@class='rct-text']/label/span[@class='rct-checkbox']")
    workspace_checkbox.click()
    time.sleep(3)
    workspace_checkbox.click()
    time.sleep(3)

    office_checkbox = driver.find_element(By.XPATH, "//div[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/"
                                                    "span[@class='rct-text']/label/span[@class='rct-checkbox']")
    office_checkbox.click()
    time.sleep(3)
    office_checkbox.click()
    time.sleep(3)


def test_workspace(browser_config):
    test_expand_arrow2(browser_config)






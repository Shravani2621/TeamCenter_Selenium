# Creating an Item
#Author Sanchita

import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import openpyxl


def wait_for_window(self, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


@pytest.mark.login
def test():
    driver = webdriver.Edge()
    domain = "http://inbr2wks-249497:3000/"
    driver.get(domain)
    time.sleep(2)
    path = r"C:\Users\sss927832\OneDrive - Tata Technologies\Desktop\Book1.xlsx"
    b = openpyxl.load_workbook(path)
    sheet = b.active
    c1 = sheet.cell(row=5, column=1)
    # driver.find_element(By.NAME, "username").send_keys("infodba")
    driver.find_element(By.NAME, "username").send_keys(c1.value)
    # driver.find_element(By.NAME, "password").send_keys("infodba")
    driver.find_element(By.NAME, "password").send_keys(c1.value)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".sw-button.accent-caution").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,
                        ".sw-column.aw-tile-tileContainer.aw-theme-locationsTile.aw-tile-smallSize").click()
    time.sleep(5)
    # driver.find_element(By.CSS_SELECTOR, "aw-commands-commandIconButton.aw-commands-command.aw-commandId"
    #                                      "-Awp0ShowCreateObject.aw-commands-commandWrapperHorizontal").click()
    # driver.find_element(By.CSS_SELECTOR, "aw-commandIcon").click()
    driver.find_element(By.CSS_SELECTOR, ".aw-commands-commandIconButton.aw-commands-command.aw-commandId"
                                         "-Awp0ShowCreateObject.aw-commands-commandWrapperHorizontal").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='sw-lov-container aw-widgets-droppable']/child::input").send_keys(
        "Item")
    # driver.find_element(By.CSS_SELECTOR, ".sw-property.sw-component.aw-widgets-droppable > "
    # ".sw-aria-border").send_keys("Item")
    # driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > .sw-aria-border > .sw-row").
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    # driver.find_element(By.CSS_SELECTOR, ".sw-aria-border.aw-widgets-cellListItem.aw-widgets-cellTop").click()
    time.sleep(5)
    driver.find_element(By.NAME, "object_name").send_keys("Item2")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".aw-panel-footer.sw-row.flex-wrap > .sw-button").click()
    time.sleep(5)

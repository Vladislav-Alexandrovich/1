from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.SafariOptions()
driver = webdriver.Safari()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

driver.fullscreen_window()

driver.find_element(
    By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
driver.find_element(
    By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
driver.find_element(
    By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
driver.find_element(
    By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
driver.find_element(
    By.CSS_SELECTOR, "[name='phone']").send_keys("+798589998787")
driver.find_element(
    By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
driver.find_element(
    By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
driver.find_element(
    By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
driver.find_element(
    By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "button").click()

driver.fullscreen_window()

waiter = WebDriverWait(driver, 4)

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#zip-code"),
                                     "N/A"))

red_color = "rgb(248, 215, 218)"
green_color = "rgb(209, 231, 221)"

first_name_color = driver.find_element(
    By.ID, "first-name").value_of_css_property("background-color")

print(first_name_color)


def test1(): assert first_name_color == green_color


last_name_color = driver.find_element(
    By.ID, "last-name").value_of_css_property("background-color")


def test2(): assert last_name_color == green_color


address_color = driver.find_element(
    By.ID, "address").value_of_css_property("background-color")


def test3(): assert address_color == green_color


address_color = driver.find_element(
    By.ID, "address").value_of_css_property("background-color")


def test4(): assert address_color == green_color


country_color = driver.find_element(
    By.ID, "country").value_of_css_property("background-color")


def test5(): assert country_color == green_color


e_mail_color = driver.find_element(
    By.ID, "e-mail").value_of_css_property("background-color")


def test6(): assert e_mail_color == green_color


phone_number_color = driver.find_element(
    By.ID, "phone").value_of_css_property("background-color")


def test7(): assert phone_number_color == green_color


job_position_color = driver.find_element(
    By.ID, "job-position").value_of_css_property("background-color")


def test8(): assert job_position_color == green_color


company_color = driver.find_element(
    By.ID, "company").value_of_css_property("background-color")


def test9(): assert company_color == green_color


zip_code_color = driver.find_element(
    By.ID, "zip-code").value_of_css_property("background-color")

print(zip_code_color)


def test_form(): assert zip_code_color == red_color


driver.quit()

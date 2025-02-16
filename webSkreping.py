import time
from seleniumbase import SB
import configURL
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def fetch_data_from_url_latvia():
    data = {}

    options = uc.ChromeOptions()
    options.headless = False

    authorisationOfElectronicMoneyInstitutionsUrl = "https://www.lb.lt/en/authorisation-of-electronic-money-institutions"
    authorisationOfPaymentInstitutionsUrl = "https://www.lb.lt/en/authorisation-of-payment-institutions"

    driver = uc.Chrome(options=options)
    driver.get(authorisationOfElectronicMoneyInstitutionsUrl)
    time.sleep(5)

    try:
        for i in range(1, 10):
            element = driver.find_element(By.XPATH, f"//div[contains(@id, 'ex-1-{i}')]")
            element.click()
            time.sleep(2)

            title_element = driver.find_element(By.XPATH, f"/html/body/section/div/div[2]/div/div/div[{i}]/h3")
            title_text = title_element.text

            text_element = driver.find_element(By.XPATH, f"/html/body/section/div/div[2]/div/div/div[{i}]/div")
            text_content = text_element.text

            data[f"element_{i}_title"] = title_text
            data[f"element_{i}_text"] = text_content

        driver.get(authorisationOfPaymentInstitutionsUrl)
        time.sleep(5)

        for i in range(1, 11):
            element = driver.find_element(By.XPATH, f"//div[contains(@id, 'ex-1-{i}')]")
            element.click()
            time.sleep(2)

            title_element = driver.find_element(By.XPATH, f"/html/body/section/div/div[2]/div/div/div[{i}]/h3")
            title_text = title_element.text

            text_element = driver.find_element(By.XPATH, f"/html/body/section/div/div[2]/div/div/div[{i}]/div")
            text_content = text_element.text

            data[f"element_{i}_title_payment"] = title_text
            data[f"element_{i}_text_payment"] = text_content

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()

    return data

   
# fetch_data_from_url_latvia()
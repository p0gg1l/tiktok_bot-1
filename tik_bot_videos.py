import random

from selenium.webdriver import Keys

from auth_data import username, password
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time



def tiktok_auth(url):
    options = webdriver.ChromeOptions()
    options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    )
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(
        executable_path="../chromedriver/chromedriver.exe",
        options=options
    )

    def xpath_check(xpath):
        try:
            driver.find_element(By.XPATH, (xpath))
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    try:
        driver.get(url=url)
        time.sleep(random.randrange(2, 4))

        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/button").click()
        time.sleep(random.randrange(2, 4))

        frame = driver.find_element(By.XPATH,"//iframe[@class='tiktok-tpndsz-IframeLoginSite eaxh4gs3']")
        driver.switch_to.frame(frame)
        time.sleep(3)

        if xpath_check("//div[contains(text(), 'VK')]"):
            driver.find_element(By.XPATH, "//div[contains(text(), 'VK')]").click()
        elif xpath_check("//div[contains(text(), 'Продолжить в VK')]"):
            driver.find_element(By.XPATH, "//div[contains(text(), 'Продолжить в VK')]").click()

        time.sleep(3)

        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)

        number_input = driver.find_element(By.NAME, "email")
        number_input.clear()
        number_input.send_keys(username)
        time.sleep(2)

        password_input = driver.find_element(By.NAME, "pass")
        password_input.clear()
        password_input.send_keys(password, Keys.ENTER)
        time.sleep(20)

        driver.switch_to.window(driver.window_handles[0])



    except Exception as ex:
        print(ex)
    finally:
        pass
        # driver.close()
        # driver.quit()


def main():
    tiktok_auth("https://www.tiktok.com")
    # tiktok_auth("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")



if __name__ == "__main__":
    main()

import random
from selenium import webdriver
import time
import fake_useragent
from selenium.webdriver.common.keys import Keys
from decrypt import links
from start import PASSWORD, USER_NAME


def main():
    user = fake_useragent.UserAgent().random
    url = 'https://www.instagram.com/'

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user}")
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=r'C:\desktop\Followers_project\chromedriver.exe',
                              options=options
                              )

    try:
        driver.get(url=url)

        time.sleep(3)
        # ввод имени
        name_input = driver.find_element_by_name("username")
        name_input.clear()
        name_input.send_keys(USER_NAME)
        print('Ввод имени')

        time.sleep(3)
        # ввод пароля
        pas_input = driver.find_element_by_name("password")
        pas_input.clear()
        pas_input.send_keys(PASSWORD)  # driver.implicitly_wait(10)
        pas_input.send_keys(Keys.ENTER)
        print('Ввод пароля')

        time.sleep(7)
        # получение подписчиков
        driver.get(f'https://www.instagram.com/{USER_NAME}/')

        time.sleep(3)
        followers_click = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()  # клик на окно с подписчиками
        time.sleep(3)
        print('Переход на вкладку с подписичиками')
        followers = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]")

        followers_count = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
        print(f'Количество подписчиков {followers_count}')

        followers_urls = []
        scrl_count = int((int(followers_count) / 12) + 2)

        print(f'Всего скроллов {scrl_count}')

        for i in range(1, scrl_count):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers)
            time.sleep(random.randrange(2, 4))
            print(f'Scroll number #{i}')

        print('Вся страница проскролена')

        all_urls_div = followers.find_elements_by_tag_name("li")
        print('Нахождение всех подписчиков и запись их в файл')

        for url in all_urls_div:
            url = url.find_element_by_tag_name("a").get_attribute("href")
            followers_urls.append(url)
            with open('followers_list.txt', 'w') as file:
                for iurl in followers_urls:
                    el_s = iurl.split('/')[-2]
                    file.write(el_s + "\n")
            links()
        print('Окончание работы')
        time.sleep(2)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

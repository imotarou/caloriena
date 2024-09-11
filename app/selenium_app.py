from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time


class GetCalorie:
    def __init__(self):
        pass

    def meal_serach(self, input_meal):
        # EdgeDriverのパスを指定
        edge_driver_path = 'msedgedriver.exe'
        # Edgeのオプションを設定
        options = Options()
        options.add_argument('--headless')  # ヘッドレスモードで実行する場合

        # EdgeDriverのサービスを設定
        service = Service(executable_path=edge_driver_path)

        # Edgeブラウザのインスタンスを作成
        driver = webdriver.Edge(service=service, options=options)

        # ウェブサイトを開く
        driver.get('https://www.asken.jp/calculate')

        textbox = driver.find_element(By.ID, 'search_input')

        # テキストを入力する
        # input_meal = input('食事をひらがなで入力してください。 >>')
        textbox.send_keys(input_meal)

        button = driver.find_element(By.CLASS_NAME, 'search_btn')

        # ボタンをクリックする
        button.click()
        time.sleep(0.5)

        search_list = driver.find_element(By.ID, 'search_list')
        search_list = search_list.find_elements(By.TAG_NAME, 'div')
        food_list = [food.text for food in search_list]

        driver.quit()

        return food_list

    def meal_list(self, input_meal, select_meal):

        # EdgeDriverのパスを指定
        edge_driver_path = 'msedgedriver.exe'
        # Edgeのオプションを設定
        options = Options()
        options.add_argument('--headless')  # ヘッドレスモードで実行する場合

        # EdgeDriverのサービスを設定
        service = Service(executable_path=edge_driver_path)

        # Edgeブラウザのインスタンスを作成
        driver = webdriver.Edge(service=service, options=options)

        # ウェブサイトを開く
        driver.get('https://www.asken.jp/calculate')

        textbox = driver.find_element(By.ID, 'search_input')

        # テキストを入力する
        # input_meal = input('食事をひらがなで入力してください。 >>')
        textbox.send_keys(input_meal)

        button = driver.find_element(By.CLASS_NAME, 'search_btn')

        # ボタンをクリックする
        button.click()
        time.sleep(0.5)

        search_list = driver.find_element(By.ID, 'search_list')
        search_list = search_list.find_elements(By.TAG_NAME, 'div')
        # food_list = [food.text for food in search_list]

        # meal = input('上記の候補から食事を選択してください。>> ')
        target_element = ''

        for element in search_list:
            if element.text == select_meal:
                target_element = element
                break

        target_element = target_element.find_element(By.TAG_NAME, 'a')
        target_element.click()
        time.sleep(0.5)

        submit_button = driver.find_element(By.ID, 'btn_show_result')
        submit_button.click()
        time.sleep(0.5)

        nutrition_dic = {'food': select_meal}
        nutrition_table = driver.find_element(
            By.ID, 'calculate_eiyo_summary')
        headers = [header.text for header in nutrition_table.find_elements(
            By.TAG_NAME, 'th')]
        rows = nutrition_table.find_elements(By.TAG_NAME, 'td')
        for i, item in enumerate(headers):
            #       nutrition_dic[item] = re.sub(r'[^\d.]','',rows[i].text)
            nutrition_dic[item] = rows[i].text

        # ブラウザを閉じる
        driver.quit()

        return nutrition_dic

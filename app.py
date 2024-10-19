from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Импорт сервиса для ChromeDriver
import json

app = Flask(__name__)

# Загрузка конфигурации
with open('config.json') as config_file:
    config = json.load(config_file)


@app.route('/open_green_api')
def open_green_api():
    # Инициализация Selenium WebDriver через сервис
    service = Service(config['webdriver_path'])  # Указываем путь к драйверу через сервис
    driver = webdriver.Chrome(service=service)  # Инициализация драйвера

    # Открытие страницы
    driver.get(config['selenium_url'])

    # Навигация по вкладкам
    documentation_tab = driver.find_element_by_link_text('Документация API')
    documentation_tab.click()

    send_text_tab = driver.find_element_by_link_text('Отправить текст')
    send_text_tab.click()

    # Пример возврата результата работы
    result = "Opened and navigated to 'Отправить текст'."

    # Закрытие браузера
    driver.quit()

    return jsonify({"message": result})


if __name__ == '__main__':
    app.run(debug=True)

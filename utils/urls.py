# Класс для управления URL-адресами в тестах
class Urls:
    # Домашняя страница Дзен
    DZEN_HOME_PAGE = 'dzen.ru'
    # Домашняя страница Яндекса
    YANDEX_HOME_PAGE = 'ya.ru'
    # Страница капчи Яндекса
    YANDEX_CAPTCHA_PAGE = 'yandex.ru'
    # Главная страница сервиса (на примере сайта с заказом самокатов)
    MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru'
    # Страница для оформления заказа
    ORDER_PAGE = MAIN_PAGE + '/order'
    # Страница отслеживания статуса заказа
    ORDER_STATUS_PAGE = MAIN_PAGE + '/track'

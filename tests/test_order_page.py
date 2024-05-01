#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pytest
import allure
from utils.urls import Urls
from pages.home_page import YaScooterHomePage
from pages.order_page import YaScooterOrderPage
from utils.locators import YaScooterOrderPageLocator
from utils.test_data import YaScooterOrderPageData as order_data


@allure.epic('Эпик для создания заказа')
@allure.parent_suite('Главный набор для заказа')
class TestYaScooterOrderPage:
    @allure.suite('Заполнение информации на странице "Получатель самоката"')
    @allure.feature('Заполнение данных пользователя при создании заказа на странице "Получатель самоката"')
    @allure.story('Проверка неправильного заполнения данных на странице "Получатель самоката"')
    @allure.title('Неправильное введение имени')
    @allure.description('Проверка на появление ошибки при неправильном вводе имени в форме заказа')
    def test_order_page_first_name_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.input_first_name('Вqw')
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_FIRST_NAME_MESSAGE).is_displayed()

    @allure.suite('Заполнение информации на странице "Получатель самоката"')
    @allure.feature('Заполнение данных пользователя при создании заказа на странице "Получатель самоката"')
    @allure.story('Проверка неправильного заполнения данных на странице "Получатель самоката"')
    @allure.title('Неправильная фамилия')
    @allure.description('Проверка на появление ошибки при неправильном вводе фамилии в форме заказа')
    def test_order_page_last_name_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.input_last_name('Вqw')
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_LAST_NAME_MESSAGE).is_displayed()

    @allure.suite('Заполнение информации на странице "Получатель самоката"')
    @allure.feature('Заполнение данных пользователя при создании заказа на странице "Получатель самоката"')
    @allure.story('Проверка неправильного заполнения данных на странице "Получатель самоката"')
    @allure.title('Неправильный адрес')
    @allure.description('Проверка на появление ошибки при неправильном вводе адреса в форме заказа')
    def test_order_page_address_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.input_address('Вqw')
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_ADDRESS_MESSAGE).is_displayed()

    @allure.suite('Заполнение данных на странице "Дополнительная информация"')
    @allure.feature('Заполнение данных пользователя при создании заказа на странице "Дополнительная информация"')
    @allure.story('Проверка негативных сценариев заполнения данных на странице "Дополнительная информация"')
    @allure.title('Пустое поле "Метро"')
    @allure.description('Проверка на появление ошибки при пустом поле "Метро" в форме оформления заказа')
    def test_order_page_subway_input_empty_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_SUBWAY_MESSAGE).is_displayed()

    @allure.suite('Заполнение данных на странице "Дополнительная информация"')
    @allure.feature('Заполнение данных пользователя при создании заказа на странице "Дополнительная информация"')
    @allure.story('Проверка негативных сценариев заполнения данных на странице "Дополнительная информация"')
    @allure.title('Ввод некорректного номера телефона')
    @allure.description('Проверка на появление ошибки при вводе некорректного номера телефона в форме оформления заказа')
    def test_order_page_telephone_number_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.input_telephone_number('Вqw')
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_TELEPHONE_NUMBER_MESSAGE).is_displayed()

    @allure.suite('Заполнение данных на странице "Для кого самокат"')
    @allure.feature('Заполнение данных пользователя при создании заказа на странице "Для кого самокат"')
    @allure.story('Корректный ввод данных на странице "Для кого самокат"')
    @allure.title('Переход с этапа "Для кого самокат" на этап "Про аренду" после заполнения данных')
    @allure.description('Проверка того, что при корректном заполнении данных на странице "Для кого самокат", '
                    'нажатии кнопки "Далее" происходит переход на следующий этап "Про аренду"')
    def test_order_page_go_to_choose_scooter_user_data_correct_open_about_rent(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.fill_user_data(order_data.data_sets['data_set1'])
        ya_scooter_order_page.go_next()
        assert len(ya_scooter_order_page.find_elements(YaScooterOrderPageLocator.ORDER_BUTTON)) > 0

    @allure.suite('Заполнение данных на странице "Про аренду"')
    @allure.feature('Заполнение данных пользователя при создании заказа на странице "Про аренду"')
    @allure.story('Корректный ввод данных на странице "Про аренду"')
    @allure.title('Оформление заказа после заполнения данных на странице "Про аренду"')
    @allure.description('Проверка того, что при корректном заполнении данных на странице "Про аренду", '
                    'нажатии кнопки "Заказать" происходит успешное оформление заказа. '
                    'Открывается модальное окно с номером созданного заказа и подтверждением об успешном оформлении')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_about_rent_input_correct_data_and_order_show_order_number(self, driver, data_set):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.fill_user_data(order_data.data_sets[data_set])
        ya_scooter_order_page.go_next()
        ya_scooter_order_page.fill_rent_data(order_data.data_sets[data_set])
        ya_scooter_order_page.click_order()
        ya_scooter_order_page.click_accept_order()
        assert len(ya_scooter_order_page.find_elements(YaScooterOrderPageLocator.ORDER_COMPLETED_INFO)) > 0

    @allure.suite('Комплексный процесс создания заказа')
    @allure.feature('Основной процесс создания заказа')
    @allure.story('Процедура оформления заказа и его просмотр')
    @allure.title('Успешное оформление заказа и доступ к его странице')
    @allure.description('Тест проверяет отображение заказа на странице "Статус заказа" после его успешного оформления')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_create_order_and_go_order_status(self, driver, data_set):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.fill_user_data(order_data.data_sets[data_set])
        ya_scooter_order_page.go_next()
        ya_scooter_order_page.fill_rent_data(order_data.data_sets[data_set])
        ya_scooter_order_page.click_order()
        ya_scooter_order_page.click_accept_order()
        order_number = ya_scooter_order_page.get_order_number()
        ya_scooter_order_page.click_go_to_status()
        current_url = ya_scooter_order_page.current_url()
        assert (Urls.ORDER_STATUS_PAGE in current_url) and (order_number in current_url)

#!/usr/bin/python
# -*- coding: UTF-8 -*-
from telnetlib import EC

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.locators import BasePageLocator
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import YaScooterHomePageLocator as Locators


class YaScooterHomePage(BasePage):
    # Нажать на кнопку заказа вверху страницы
    @allure.step('Нажать на кнопку заказа вверху страницы')
    def snake_case(self):
        return self.find_element(Locators.TOPORDERBUTTON).click()

    # Нажать на кнопку заказа внизу страницы
    @allure.step('Нажать на кнопку заказа внизу страницы')
    def clicktoporderbutton(self):
        try:
            button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, Locators.TOPORDERBUTTON)))
            button.click()
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        raise TimeoutException("Элемент не был найден на странице")

    # Нажать на вопрос в FAQ по номеру
    @allure.step('Нажать на вопрос в FAQ')
    def clickfaqquestion(self, questionnumber: int):
        elems = self.find_elements(Locators.FAQBUTTONS, 10)
        return elems[questionnumber].click()



    # Дождаться, пока URL не станет отличным от about:blank
    def waiturluntilnotaboutblank(self, time=10):
        return WebDriverWait(self.driver, time).untilnot(EC.urltobe('about:blank'))

    # Нажать на кнопку Yandex
    @allure.step('Перейти на страницу яндекса')
    def clickyandexbutton(self):
        return self.find_element(BasePageLocator.YANDEXSITEBUTTON).click()

    # Нажать на кнопку согласия с куки
    @allure.step('Принять куки')
    def clickcookieaccept(self):
        return self.find_element(BasePageLocator.COOKIEACCEPTBUTTON).click()
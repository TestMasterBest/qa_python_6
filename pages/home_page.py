#!/usr/bin/python
# -*- coding: UTF-8 -*-
import allure
from pages.base_page import BasePage
from utils.locators import BasePageLocator
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import YaScooterHomePageLocator as Locators


class YaScooterHomePage(BasePage):
    # Нажать на кнопку заказа вверху страницы
    @allure.step('Нажать на кнопку заказа вверху страницы')
    def clicktoporderbutton(self):
        return self.findelement(Locators.TOPORDERBUTTON).click()

    # Нажать на кнопку заказа внизу страницы
    @allure.step('Нажать на кнопку заказа внизу страницы')
    def clickbottomorderbutton(self):
        return self.findelement(Locators.BOTTOMORDERBUTTON).click()

    # Нажать на вопрос в FAQ по номеру
    @allure.step('Нажать на вопрос в FAQ')
    def clickfaqquestion(self, questionnumber: int):
        elems = self.findelements(Locators.FAQBUTTONS, 10)
        return elems[questionnumber].click()

    # Переключиться на определенное окно
    @allure.step('Переключиться на вкладку браузера')
    def switchwindow(self, windownumber: int = 1):
        return self.driver.switchto.window(self.driver.windowhandleswindow_number)

    # Дождаться, пока URL не станет отличным от about:blank
    def waiturluntilnotaboutblank(self, time=10):
        return WebDriverWait(self.driver, time).untilnot(EC.urltobe('about:blank'))

    # Нажать на кнопку Yandex
    @allure.step('Перейти на страницу яндекса')
    def clickyandexbutton(self):
        return self.findelement(BasePageLocator.YANDEXSITEBUTTON).click()

    # Нажать на кнопку согласия с куки
    @allure.step('Принять куки')
    def clickcookieaccept(self):
        return self.findelement(BasePageLocator.COOKIEACCEPTBUTTON).click()
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

__author__ = 'Давыдов'

from unittest import TestCase
from selenium import webdriver
from page import Page
from yandex import Search_bar
import unittest


class SeleniumTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.page.open("http://www.yandex.ru")

    def testEntering(self):
        self.page.search_bar.get_attribute()

    def testTitle(self):
        self.page.set_Text("Тестирование").input()
        self.assertIn('Тестирование', self.page.get_title(), "Неверное значение")

    def testTitle2(self):
        self.page.set_Text("").input()
        self.assertEqual("Яндекс: задан пустой поисковый запрос",self.page.get_title(), "Неверное значение")



    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

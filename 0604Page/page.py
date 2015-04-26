__author__ = 'Давыдов'
from yandex import YaTest
class Page():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)


    def open(self, url):
        self.driver.get(url)
        return self

    def get_title(self):
        return self.driver.title

    def set_Text(self,text):
        self.text_ = text
        return self

    def input(self):
        self.ya_test = YaTest(self.driver)
        self.ya_test.entering(self.text_)



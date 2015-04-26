__author__ = 'Давыдов'


from base_component import BaseComponent

class YaTest(BaseComponent):
    data ={
        'text': 'text',
        'input_text': 'input',
        'submit':"//button[@type='submit']",
    }

    def entering(self,text):
        self.driver.find_element_by_id(self.data['text']).send_keys(text)
        self.driver.find_element_by_xpath(self.data['submit']).click()
        

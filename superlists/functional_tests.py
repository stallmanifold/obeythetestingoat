from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Let us tell the tale of Bob Bobberson, the infamous terrorist from Far 
        # West Syria (a neighborhood in suburban Dearborn, Michigan.)
        # Bob Bobberson wants to buy supplies for making bombs for his terrorist
        # friends. He heard about this awesome website called To-Do in which he can 
        # write out the entire list of supplies he needs so he doesn't have to
        # memorize them all. Not being a very bright fellow and having a terrible memory, 
        # Bob decides to imcriminate himself by typing his list at the To-Do list site.
        # He proceeds to the homepage.
        self.browser.get('http://localhost:8000')
        
        # He observes the page title involves making To-Do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Immediately on the homepage he is invited to make a list.
        # He types out his list of supplies he needs to buy.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy chemicals.')
        # When he pushes the enter button, the list updates, and the list now reads
        # "1: Buy chemicals." as an item in the to-do list.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy chemicals.')

        # There is a text box inviting him to add more items. Having a lot of
        # things he needs to do, he writes out the instructions for making bombs and
        # weapons.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Build chemical lab equipment.')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows all items on his list.
        self.check_for_row_in_list_table('1: Buy chemicals.')
        self.check_for_row_in_list_table('2: Build chemical lab equipment.')

        # Bob Bobberson wonders whether To-Do list, being owned by a greedy corporation
        # and full of analytics malware, will end up in the hands of a major world power
        # that has a reputation for asploding terrorists. Just kidding! he's too stupid to 
        # think of something that clever! Bob, being a rather gormless bellend of a villain,
        # shrugs and figures nothing much will happen. Bob continues entering items into his
        # list including the last two items:
        # ...
        # 58. Buy beer and cigarettes.
        # 59. Buy porn.
        # ...
        # Bob is curious whether the website will remember his list when he leaves. So he 
        # closes the browser tab, and goes to the website again, and upon returning, he sees
        # that his list is exactly how he left it.
        self.fail('Finish the test!!')

        # Satisfied, Bob Bobberson shuts down his computer and goes to sleep.


        # One hour later, while Bob is dead asleep, a missile comes flying through his
        # window and he and his apartment are blown to smithereens. We never hear 
        # from Bob Bobberson the infamous chuckleheaded terrorist ever again.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
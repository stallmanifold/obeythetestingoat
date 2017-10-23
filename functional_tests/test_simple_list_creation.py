from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):
        # Let us tell the tale of Bob Bobberson, the infamous terrorist from Far 
        # West Syria (a neighborhood in suburban Dearborn, Michigan.)
        # Bob Bobberson wants to buy supplies for making bombs for his terrorist
        # friends. He heard about this awesome website called To-Do in which he can 
        # write out the entire list of supplies he needs so he doesn't have to
        # memorize them all. Not being a very bright fellow and having a terrible memory, 
        # Bob decides to imcriminate himself by typing his list at the To-Do list site.
        # He proceeds to the homepage.
        self.browser.get(self.live_server_url)
        
        # He observes the page title involves making To-Do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Immediately on the homepage he is invited to make a list.
        # He types out his list of supplies he needs to buy.
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy chemicals.')
        # When he pushes the enter button, the list updates, and the list now reads
        # "1: Buy chemicals." as an item in the to-do list.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.wait_for_row_in_list_table('1: Buy chemicals.')

        # There is a text box inviting him to add more items. Having a lot of
        # things he needs to do, he writes out the instructions for making bombs and
        # weapons.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Build chemical lab equipment.')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows all items on his list.
        self.wait_for_row_in_list_table('1: Buy chemicals.')
        self.wait_for_row_in_list_table('2: Build chemical lab equipment.')

        # Bob Bobberson wonders whether To-Do list, being owned by a greedy corporation
        # and full of analytics malware, will end up in the hands of a major world power
        # that has a reputation for asploding terrorists. Just kidding! he's too stupid to 
        # think of something that clever! Bob, being a rather gormless bellend of a villain,
        # shrugs and figures nothing much will happen. Bob continues entering items into his
        # list including the last two items:
        # ...
        # 58. Buy beer.
        # 59. Buy cigarettes.
        # ...
        # Bob is curious whether the website will remember his list when he leaves. So he 
        # closes the browser tab, and goes to the website again, and upon returning, he sees
        # that his list is exactly how he left it.

        # Satisfied, Bob Bobberson shuts down his computer and goes to sleep.


        # One hour later, while Bob is dead asleep, a missile comes flying through his
        # window and he and his apartment are blown to smithereens. We never hear 
        # from Bob Bobberson the infamous chuckleheaded terrorist ever again.
   
    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list.
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She notices that her list has a unique URL.
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, 'lists/.+')

        # Now a new user, Francis, comes along to the site.

        ## We use a new browser session to make sure no information
        ## of Edith's is coming through from cookies, etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page. There is no sign of Edith's
        # list.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique URL.
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep.

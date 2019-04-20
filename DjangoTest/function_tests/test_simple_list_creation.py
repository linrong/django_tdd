from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 功能测试使用LiveServerTestCase实现隔离，django会自动创建测试数据库而不用和之前一样测试数据不隔离
# 不使用真正的数据库，不使用之前的unittest.TestCase
class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_and_retrieve_it_later(self):
        #self.browser.get('http://127.0.0.1:8000/')
        #a访问网站
        self.browser.get(self.server_url)
        #检查页面元素
        self.assertIn('To',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To',header_text)
        
        inputbox=self.get_item_input_box()
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )
        #a输入一些东西
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        edith_list_url=self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')#unittest中的函数，判断字符串是否符合正则表达式
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        #a再次输入一些东西
        inputbox=self.get_item_input_box()
        inputbox.send_keys('hhhhhhhhhhh')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: hhhhhhhhhhh')
        
        #b访问访问网站
        self.browser.quit()
        self.browser=webdriver.Chrome()
        #b查看页面,是否可以看到a输入的内容
        self.browser.get(self.server_url)
        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('hhhhh',page_text)
        #b自己输入一些内容
        inputbox=self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        #b获得自己的url
        b_lsit_url=self.browser.current_url
        self.assertRegex(b_lsit_url,'/lists/.+')
        self.assertNotEqual(b_lsit_url,edith_list_url)
        #再次判断下页面上显示的内容
        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertIn('Buy milk',page_text)
        #self.fail('finish the test!')
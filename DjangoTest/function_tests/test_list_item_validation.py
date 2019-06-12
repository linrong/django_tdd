from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url) # 访问网页
        self.get_item_input_box().send_keys('\n') # 按下回车键

        # 使用了ModelForm之后表单为空的话不能提交，相当于什么都没有做，所以不会跳转，所以不能读取类名
        # 这个在目前的使用中情况可能和书上的不太一样，可能是浏览器更新的原因
        #error=self.browser.find_element_by_css_selector('.has-error')# 通过bootstrap提供的css类.has-error标记错误文本
        #self.assertEqual(error.text,"You can't have an empty list item")# 判断错误信息是否和预先的一致

        self.get_item_input_box().send_keys('Buy milk\n')# 输入文字并且按下回车
        self.check_for_row_in_list_table('1: Buy milk')

        self.get_item_input_box().send_keys('\n') # 不输入文字按下回车键
         
        self.check_for_row_in_list_table('1: Buy milk')# 再一次检查lsit文字
        # error=self.browser.find_element_by_css_selector('.has-error')# 通过bootstrap提供的css类.has-error标记错误文本
        # self.assertEqual(error.text,"You can't have an empty list item")# 判断错误信息是否和预先的一致

        self.get_item_input_box().send_keys('Make tea\n')# 输入文字并且按下回车
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
    
    def test_cannot_add_duplicate_items(self):
        # A访问首页，创建一个清单
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        # 然后不小心输入一个重复的
        self.get_item_input_box().send_keys('Buy wellies\n')

        # A看到一条有帮助的错误信息
        self.check_for_row_in_list_table('1: Buy wellies')
        error=self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text,"You're already got this in your list")
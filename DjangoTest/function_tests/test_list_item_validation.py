from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url) # 访问网页
        self.get_item_input_box().send_keys('\n') # 按下回车键

        error=self.browser.find_element_by_css_selector('.has-error')# 通过bootstrap提供的css类.has-error标记错误文本
        self.assertEqual(error.text,"You can't have an empty list item")# 判断错误信息是否和预先的一致

        self.get_item_input_box().send_keys('Buy milk\n')# 输入文字并且按下回车
        self.check_for_row_in_list_table('1: Buy milk')

        self.get_item_input_box().send_keys('\n') # 不输入文字按下回车键
         
        self.check_for_row_in_list_table('1: Buy milk')# 再一次检查lsit文字
        error=self.browser.find_element_by_css_selector('.has-error')# 通过bootstrap提供的css类.has-error标记错误文本
        self.assertEqual(error.text,"You can't have an empty list item")# 判断错误信息是否和预先的一致

        self.get_item_input_box().send_keys('Make tea\n')# 输入文字并且按下回车
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('1: Make tea')

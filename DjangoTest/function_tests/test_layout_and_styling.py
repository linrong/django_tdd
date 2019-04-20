from .base import FunctionalTest

class LayoutAndStyingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # a访问首页
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768) # 设置查看固定大小

        # 查看输入框是否据中
        inputbox=self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x']+inputbox.size['width']/2,
            512,
            delta=10 # 误差正负5像素
        )
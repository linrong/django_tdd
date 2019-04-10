from django.test import TestCase
from test1.forms import ItemForm

class ItemFormTest(TestCase):
    def  test_form_renders_item_text_input(self):
        form=ItemForm()
        self.fail(form.as_p())# form.as_p()作用是把表单渲染成html
        # self.fail 探索性编程，会显示错误和打印信息？

from django.test import TestCase
from test1.forms import ItemForm,EMPTY_LIST_ERROR
from unittest import skip
class ItemFormTest(TestCase):
    @skip
    def  test_form_renders_item_text_input(self):
        form=ItemForm()
        self.fail(form.as_p())# form.as_p()作用是把表单渲染成html
        # self.fail 探索性编程，会显示错误和打印信息？
    
    def test_form_item_input_has_placeholder_and_css_classes(self):
        form=ItemForm()
        self.assertIn('placeholder="Enter a to-do item"',form.as_p())
        self.assertIn('class="form-control input-lg"',form.as_p())
    
    def test_form_validation_for_blank_items(self):
        form=ItemForm(data={'text':''})
        self.assertFalse(form.is_valid())# form.isvalid()返回验证True或者Flase,如果错误则生成error属性，是字典类型
        self.assertEqual(
            form.errors['text'],
            [EMPTY_LIST_ERROR]
        )
from django.test import TestCase
from test1.models import Item,List
from django.core.exceptions import ValidationError

class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_=List()
        list_.save()
    
        first_item=Item()
        first_item.text='first item'
        first_item.list=list_
        first_item.save()
        
        second_item=Item()
        second_item.text='second item'
        second_item.list=list_
        second_item.save()
        
        saved_list=List.objects.first()
        self.assertEqual(saved_list,list_)
        
        saved_items=Item.objects.all()
        self.assertEqual(saved_items.count(),2)
        
        first_saved_item=saved_items[0]
        second_saved_item=saved_items[1]
        self.assertEqual(first_saved_item.text,'first item')
        self.assertEqual(first_saved_item.list,list_)
        self.assertEqual(second_saved_item.text,'second item')
        self.assertEqual(second_saved_item.list,list_)
    
    def test_cannot_save_empty_list_items(self):
        list_ =List.objects.create()
        item =Item(list=list_,text='')
        with self.assertRaises(ValidationError):
            item.save()
            # django的模型不会运行全部验证，使用下面的代码可以运行全部验证
            item.full_clean()
        # with结合上下文管理器,包装一段代码,也可以写成:
        # try:
        #     item.save()
        #     self.fail('The save should have raised an exception')
        # except ValidationError:
        #     pass
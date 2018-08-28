from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from test1.views import home_page
from test1.models import Item,List

# Create your tests here.
class SmokeTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        request =HttpRequest()
        response =home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>',response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
                                
      
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
        
class ListViewTest(TestCase):
    def test_displays_only_items_for_that_list(self):
        correct_list=List.objects.create()
        Item.objects.create(text='itemey 1',list=correct_list)
        Item.objects.create(text='itemey 2',list=correct_list)
        
        other_list=List.objects.create()
        Item.objects.create(text='other list item 1',list=other_list)
        Item.objects.create(text='other list item 2',list=other_list)
        #TestCase自带的测试客户端self.client
        response=self.client.get('/lists/%d/'%(correct_list.id,))
        self.assertContains(response,'itemey 1')  
        self.assertContains(response,'itemey 2')   
        self.assertNotContains(response,'other list item 1')
        self.assertNotContains(response,'other list item 2')
    #检查是否使用list.html模板   
    def test_uses_list_template(self):
        list_=List.objects.create()
        response=self.client.get('/lists/%d/'%(list_.id,))
        self.assertTemplateUsed(response,'list.html')
        
        
class NewListTest(TestCase):
    
    def test_saving_a_POST_request(self):
        self.client.post(
        '/lists/new',
        data={'item_text':'A new list item'}
        )
        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')    
        
        
    def test_redirects_after_POST(self):
        response=self.client.post(
        '/lists/new',
        data={'item_text':'A new list item'}
        )
        self.assertEqual(response.status_code,302)
        new_list=List.objects.first()
        self.assertRedirects(response,'/lists/%d/'%(new_list.id,))
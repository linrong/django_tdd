 # pylint: disable=no-member
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from test1.models import Item,List
from django.core.exceptions import ValidationError


# Create your views here.
def home_page(request):
    #return HttpResponse('<html><title>To-Do lists</title></html>')
    
    #item=Item()
    #item.text=request.POST.get('item_text','')
    #item.save()
    #return render(request,'home.html',{
    #   'new_item_text':item.text
    #})
    
    #if request.method=='POST':
    #    new_item_text=request.POST['item_text']
    #    Item.objects.create(text=new_item_text)
    #else:
    #    new_item_text=''
    #return render(request,'home.html',{
    #'new_item_text':new_item_text,
    #})
    
    #if request.method=='POST':
    #    Item.objects.create(text=request.POST['item_text'])
    #    return redirect('/lists/the-only-list-in-the-world/')
    #items=Item.objects.all()
    return render(request,'home.html')

def new_list(request):
    list_=List.objects.create()
    item=Item(text=request.POST['item_text'],list=list_)
    try:
        item.full_clean()# 进行验证
        item.save()
    except ValidationError:
        list_.delete()
        error="You can't have an empty list item"
        return render(request,'home.html',{"error":error})
    return redirect('/lists/%d/'%(list_.id,))

def view_list(request,list_id):
    list_=List.objects.get(id=list_id)
    if request.method =='POST':
        Item.objects.create(text=request.POST['item_text'],list=list_)
        return redirect('/lists/%d/'%(list_.id,))
    return render(request,'list.html',{'list':list_})
    
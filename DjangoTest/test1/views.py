 # pylint: disable=no-member
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from test1.models import Item,List
from test1.forms import ItemForm
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
    return render(request,'home.html',{'form':ItemForm()})

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_=List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request,'home.html',{"form":form})

def view_list(request,list_id):
    list_=List.objects.get(id=list_id)
    form=ItemForm()
    if request.method =='POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(for_list=list_)
            return redirect(list_)
    return render(request,'list.html',{'list':list_,'form':form})
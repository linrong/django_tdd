from django import forms
from test1.models import Item
from django.core.exceptions import ValidationError
# 创建表单类
EMPTY_LIST_ERROR="You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You're already got this in your list"
class ItemForm(forms.models.ModelForm):
    class Meta:
        # 指明表单用于那个模型，使用那些字段
        model=Item
        fields=('text',)
        widgets={
            'text':forms.fields.TextInput(attrs={
                'placeholder':'Enter a to-do item',
                'class':'form-control input-lg',
            }),
        }
        error_messages={
            'text':{'required':EMPTY_LIST_ERROR}
        }

    def save(self,for_list):
        self.instance.list=for_list # 表单的.instance属性是将要修改或创建的数据库对象,目前这个是Item？
        return super().save()

class ExistingListItemForm(ItemForm):
    def __init__(self,for_list,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.instance.list=for_list

    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict={'text':[DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)
            
    # 不使用父类的保存方法
    def save(self):
        return forms.models.ModelForm.save(self)
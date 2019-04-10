from django import forms
from test1.models import Item
# 创建表单类
EMPTY_LIST_ERROR="You can't have an empty list item"
class ItemForm(forms.models.ModelForm):
    class Meta:
        # 指明表单用于那个模型，使用那些字段
        model=Item
        fields=('text',)
        widgets={
            'text':forms.fields.TextInput(attrs={
                'placeholder':'Enter a to-do item',
                'class':'form-control input-lg',
            })
        }
        error_messages={
            'text':{'required':EMPTY_LIST_ERROR}
        }
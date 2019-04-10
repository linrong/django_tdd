from django import forms
from test1.models import Item
# 创建表单类
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
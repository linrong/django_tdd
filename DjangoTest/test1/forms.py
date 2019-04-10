from django import forms
# 创建表单类
class ItemForm(forms.Form):
    item_text=forms.CharField()
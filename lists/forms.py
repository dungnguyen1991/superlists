from django import forms
from django.forms import fields, widgets 

from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"

class ItemForm(forms.models.ModelForm):
    
    class Meta:
        model = Item
        fields = ('text', )
        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            })
        }
        error_messages = {
            'text': {
                'required': EMPTY_ITEM_ERROR
            }
        }
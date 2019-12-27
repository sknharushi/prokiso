from django import forms
from .models import Item
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','image', 'type', 'memo')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '記入例：黒の財布'}),

            'type': forms.RadioSelect(),
            'memo': forms.Textarea(attrs={'rows': 4}),
        }

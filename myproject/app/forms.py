from django import forms
from .models import ModelA, ModelB, ModelC


class UniversalModelForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(UniversalModelForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = 'width: 250px;'


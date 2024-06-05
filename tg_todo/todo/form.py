from django import forms
from .models import *


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)

        for i in self.fields:
            self.fields[i].widget.attrs['placeholder'] = self.fields[i].label


class DateForm(forms.ModelForm):
    timer = forms.DateField(
        input_formats=['%Y/%m/%d'],
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Date
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DateForm, self).__init__(*args, **kwargs)

        for i in self.fields:
            self.fields[i].widget.attrs['placeholder'] = self.fields[i].label

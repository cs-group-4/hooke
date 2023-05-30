from django import forms
from . import models

class Profile_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['date_of_birth'].widget.attrs['id'] = 'date'
        self.fields['date_of_birth'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'
                }
            )

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            # visible.field.widget.attrs['placeholder'] = visible.field.label
    class Meta:
        model = models.Profile
        fields = ['first_name', 'last_name', 'phone_number', 'bio', 'date_of_birth', 'nationality', 
                  'hostel', 'school', 'program', 'year', 'profile_photo']
        



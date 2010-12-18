from django import forms
from models import Settings

class SettingsForm(forms.ModelForm):
    cms_pass = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Settings


    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['email'].widget.attrs['readonly'] = True


class CMSUploadForm(forms.Form):
    post_file = forms.FileField()
    status = forms.CharField()
    layout = forms.CharField()
    dir_structure = forms.CharField()
   
class WPUploadForm(CMSUploadForm):
    image_file = forms.FileField(required=False)
    category = forms.CharField()
    date = forms.DateTimeField()
    tags = forms.CharField(required=False)

class FileUploadForm(forms.Form):
    post_file = forms.FileField()
    image_file = forms.FileField(required=False)
    category = forms.CharField(required=False)
    status = forms.CharField()
    date = forms.DateTimeField(required=False)
    tags = forms.CharField(required=False)
    layout = forms.CharField()
    dir_structure = forms.CharField()
    

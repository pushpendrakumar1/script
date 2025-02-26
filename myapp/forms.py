from django import forms
from .models import UploadedFolders

class UploadFoldersForm(forms.ModelForm):
    class Meta:
        model = UploadedFolders
        fields = ['folder_name1', 'enter_id1', 'folder_name2', 'enter_id2']

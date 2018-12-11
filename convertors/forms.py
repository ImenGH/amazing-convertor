from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


class TypeFileForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

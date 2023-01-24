from django import forms
from .models import Comment

class CForm(forms.ModelForm):
    def __init__(self, *a, **b):
        super(CForm, self).__init__(*a, **b)
        for fields in self.fields:
            self.fields[fields].widget.attrs["class"]="form-control"
            self.fields[fields].widget.attrs["placeholder"]= " Your "+fields.capitalize()+"*"
    class Meta:
        model = Comment
        exclude = ("post", )

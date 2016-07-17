from django import forms
from mysite.models import notes


class NewNoteForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = ["title",
                  "content",
                  "draft_staus",
                  ]
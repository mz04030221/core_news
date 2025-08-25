from django import forms
from issues.models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            "title",
            "edition",
            "cover",
        ]

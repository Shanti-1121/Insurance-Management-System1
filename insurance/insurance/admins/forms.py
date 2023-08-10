from django import forms
from . import models

class ContactForm(forms.Form):
    Name = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
    Email = forms.EmailField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


class CategoryForm(forms.ModelForm):
    class Meta:
        model=models.Category
        fields=['category_name']

class PolicyForm(forms.ModelForm):
    category=forms.ModelChoiceField(queryset=models.Category.objects.all(),empty_label="Category Name", to_field_name="id")
    class Meta:
        model=models.Policy
        fields=['policy_name','sum_assurance','premium','tenure']

class QuestionForm(forms.ModelForm):
    class Meta:
        model=models.Question
        fields=['description']
        widgets = {
        'description': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }
from django import forms
from .models import Feedback

class FeedbackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'class2', 'id':'id2'}), required=True, error_messages={'required':'you forgot to add your name'})
    rating = forms.IntegerField(widget=forms.NumberInput({'class':'class3', 'id':'id3'}), min_value=1, max_value=5)
    text = forms.CharField(label='Your feedback', widget=forms.Textarea(attrs={'class':'class1', 'id':'id1', 'rows':3}), max_length=200)

    class Meta:
        model = Feedback
        fields = ['name', 'rating', 'text']



    # label='Full Name': To change the label in html form 
    #name = forms.CharField(required=True, label='Full Name', help_text='Enter your name')
    #name = forms.CharField(max_length=5, required=True, error_messages={'required':'you forgot to add your name', 'max_length':'this name is too long make it shorter :)' })
    #date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))

    # To assign an id and class to the fields of a form and to reduce the side of the (text area: 'rows':3)
    #name = forms.CharField(widget=forms.TextInput(attrs={'class':'class2', 'id':'id2'}), required=True, error_messages={'required':'you forgot to add your name'})
    #rating = forms.IntegerField(widget=forms.NumberInput({'class':'class3', 'id':'id3'}), min_value=1, max_value=5)
    #text = forms.CharField(label='Your feedback', widget=forms.Textarea(attrs={'class':'class1', 'id':'id1', 'rows':3}), max_length=200)
